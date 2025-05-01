import pandas as pd
import constants as cs
import df_functions as dfuns
import xlsx_functions as xfuns
import functions as funs
import acumatica as acu
# import email_w_attach as ewa
import gmail_w_attach as gwa
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from datetime import datetime
from openpyxl import load_workbook
import os

today = datetime.now()
date_for_file = today.strftime('%m%d%Y%H%M%S')
img_path = '../img'
tmp_path = '../tmp'
data_path = '../data'
logo_file_name = 'hv_logo_sized_201_53.png'
tmp_xlsx_name = 'Wholesale_Order_Form.xlsx'
sheet_name = 'HVVWSGoodsOrderingSheet'
ws_order_form_name = f'Wholesale_Order_Form_{date_for_file}.xlsx'

ws_order_form_output = funs.join_dir_file(data_path, ws_order_form_name)
create_logo_path = funs.join_dir_file(img_path, logo_file_name)
create_tmp_xlsx_path = funs.join_dir_file(tmp_path, tmp_xlsx_name)

img = Image(create_logo_path)
file_name = create_tmp_xlsx_path

# img = Image('img/hv_logo_sized_201_53.png')
# file_name = 'data/Wholesale_Order_Form.xlsx'

wb = Workbook()
ws = wb.active

xfuns.format_white_bg(ws, 'A1:FF550')
ws.add_image(img, 'B2')

ws.title = sheet_name
wb.save(file_name)

# aside from making the login/logout call, below makes 3 calls to generate each report
# and 3 calls download the report in xlsx format
# batch_info_file - WS031733 - FGA Wholesale With Batch Info - CLAEBAvailable
# valid_qty_file -  WS040125 - FGA Wholesale With Valid Qty - FGAWSOF
# in_transit_file - WS040725 - In-Transit Inventory - INTRANSITINV

in_transit_session = acu.login()
in_transit_file = acu.generate_download_report(in_transit_session, 'INTRANSITINV')
in_transit_end_session = acu.close_acumatica_session(in_transit_session)
in_transit_cleaned = funs.join_dir_file(tmp_path, f'in-transit-cleaned-{date_for_file}.xlsx')
clean_in_transit = xfuns.clean_excel_file(in_transit_file, in_transit_cleaned)
df_in_transit = pd.read_excel(clean_in_transit)

batch_session = acu.login()
batch_info_file = acu.generate_download_report(batch_session, 'CLAEBAvailable')
batch_end_session = acu.close_acumatica_session(batch_session)
batch_cleaned = funs.join_dir_file(tmp_path, f'batch-cleaned-{date_for_file}.xlsx')
clean_batch = xfuns.clean_excel_file(batch_info_file, batch_cleaned)
df_batch = pd.read_excel(clean_batch)

qty_session = acu.login()
valid_qty_file = acu.generate_download_report(qty_session, 'FGAWSOF')
qty_end_session = acu.close_acumatica_session(qty_session)
qty_cleaned = funs.join_dir_file(tmp_path, f'qty-cleaned-{date_for_file}.xlsx')
clean_qty = xfuns.clean_excel_file(valid_qty_file, qty_cleaned)
df_qty = pd.read_excel(clean_qty)

# now start building dataframe 
main_df = dfuns.merge_dfs(df_qty, df_batch, df_in_transit)

main_df = dfuns.drop_dupe_rows(main_df)

# main_df = dfuns.qty_case_count_conv(main_df)
# remove row if product has 0 for quantity
main_df = dfuns.remove_row_with_zero_qty(main_df, 'Qty Available for Sale')

# remove the strain DX4 (not for general whoesale)
main_df = dfuns.remove_row_with_val_in_col(main_df, 'Strain', 'DX4')

# sort by Inventory ID and in wanted order
sorted_df = dfuns.order_by_inventory_id(main_df)

# remove unneeded columns by calling remove columns function
sorted_df['Harvest Date'] = sorted_df['Harvest Date'].dt.strftime('%m/%d/%Y')

sorted_df = dfuns.remove_old_dates(sorted_df, 'Harvest Date')

# column header updates
cleaned_cols_df = sorted_df.rename(columns={'Strain': 'Strain/Flavor', 'THCA': 'THC-A', 'Qty Available for Sale': 'Qty. Available'})

# add column with I/S/H value
ish_col_added_df = dfuns.add_col_with_vals_from_dict(cleaned_cols_df, 'Strain/Flavor', cs.ish_dict, 'I/S/H')

# add net weights/volumes column with value
net_col_added_df = dfuns.add_col_with_vals_from_dict(ish_col_added_df, 'Inventory ID', cs.net_weight_vol, 'Net Weights/Volumes')

# add servings column with value
serve_col_added_df = dfuns.add_col_with_vals_from_dict(net_col_added_df, 'Inventory ID', cs.servings, 'Servings')

# add price column with value
price_col_added_df = dfuns.add_col_with_vals_from_dict(serve_col_added_df, 'Inventory ID', cs.price_ea, 'Price/EA')

# this accomodates when the wholesale team wants a product to be on sale or have value pricing
price_col_added_df['Price/EA'] = price_col_added_df.apply(dfuns.value_pricing_update, axis=1)

# add case count column with value
case_count_col_added_df = dfuns.add_col_with_vals_from_dict(price_col_added_df, 'Inventory ID', cs.case_count, 'Case Count')

# convert qty to fit in case count
case_count_col_added_df = dfuns.qty_case_count_conv(case_count_col_added_df)

# the orginal qty available can be removed because it was converted above to a new column
case_count_col_added_df.pop('Qty. Available')

# rename the Conversion column back to Available
case_count_col_added_df = case_count_col_added_df.rename(columns={'Qty Conversion': 'Qty. Available'})

# then move I/S/H column to 3rd column
move_ish_col_added_df = dfuns.move_column(case_count_col_added_df, 'I/S/H', 3)

# then move Available column to 3rd column
move_qty_col_added_df = dfuns.move_column(move_ish_col_added_df, 'Qty. Available', 13)

# remove batch details from edibles
move_qty_col_added_df = dfuns.remove_batch_details(move_qty_col_added_df)

# update cfx gummy strain/flavor to include Sleep-Calm-Focus-Energy
move_qty_col_added_df = dfuns.update_cfx_gummies_description(move_qty_col_added_df)

# add cfx gummy cbd detail
move_qty_col_added_df = dfuns.add_value_to_col_based_on_other_col(move_qty_col_added_df, 'Total THC', cs.cfx_gum_cbds_map, 'Strain/Flavor')

# add tincture/topical thc/cbd values
move_qty_col_added_df = dfuns.add_value_to_col_based_on_other_col(move_qty_col_added_df, 'Total THC', cs.top_tinc_thc_cbd_map, 'Product Description')

# remove rows with nulls in Inventory ID and Qty. Available
final_df = move_qty_col_added_df[move_qty_col_added_df['Inventory ID'].notna()]
final_df = move_qty_col_added_df[move_qty_col_added_df['Qty. Available'].notna()]

# add columns not in df already (NET WEIGHTS/VOLUMES, SERVINGS, etc.)
add_columns_df = dfuns.add_columns(final_df)

# add product descriptor row to separate items (e.g. flower from pre-rolls from hitmakers and so on)
starting_row_cat_insert_df = dfuns.insert_start_row(add_columns_df, cs.cat_by_inventory_id)

# now we can remove the inventory id column - no longer needed
starting_row_cat_insert_df.pop('Inventory ID')

# write the finished dataframe to the excel file
with pd.ExcelWriter(file_name, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
    starting_row_cat_insert_df.to_excel(writer, sheet_name=sheet_name, startrow=6, startcol=1, index=False)

# start a new workbook for the remaining formatting
new_workbook = load_workbook(file_name)
sheet = new_workbook[sheet_name]

# remaining format updates to the sheet
xfuns.grey_headers(sheet)
xfuns.delete_dupe_red_rows(sheet)
xfuns.update_cat_white(sheet)
xfuns.convert_float_percentage(sheet)
xfuns.adjust_column_width(sheet)
xfuns.center_align_columns(sheet)
xfuns.update_value_pricing_bg(sheet)
xfuns.remove_zeros(sheet)
xfuns.available_case(sheet)
xfuns.convert_currency(sheet, 'L')
xfuns.case_price(sheet)
xfuns.item_total(sheet)
xfuns.convert_currency(sheet, 'P')
last_total_row = xfuns.get_max_total_row(sheet)
xfuns.add_borders(sheet, last_total_row)
xfuns.grey_out_cells(sheet, last_total_row)
xfuns.add_separator_row(sheet)
xfuns.add_total_sum(sheet, last_total_row)
xfuns.merge_cells_in_column(sheet, 'B', 9)
xfuns.convert_currency(sheet, 'R')
# widening the Total column so larger totals doesn't
# get converted 'visually' to #### because the column width is too narrow
sheet.column_dimensions['R'].width = 15
xfuns.create_header(sheet)

# freeze first 7 rows so you don't loose column headers
sheet.freeze_panes = 'A8'

# new_workbook.save(f'../data/Wholesale_Order_Form_{date_for_file}.xlsx')
new_workbook.save(ws_order_form_output)

# email the output form
gwa.send_email(ws_order_form_output)

# clean up tmp files
os.remove(file_name)
os.remove(in_transit_file)
os.remove(in_transit_cleaned)
os.remove(batch_info_file)
os.remove(batch_cleaned)
os.remove(valid_qty_file)
os.remove(qty_cleaned)
# clean up old order forms
funs.delete_old_files(data_path)