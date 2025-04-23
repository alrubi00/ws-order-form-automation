import pandas as pd
import numpy as np
import constants as cs
from datetime import datetime, timedelta

# updates current pricing with a value price point
def value_pricing_update(row):
    update_dict = cs.value_pricing
    key = (row['Inventory ID'], row['Strain/Flavor'])
    return update_dict.get(key, row['Price/EA'])

# convert qtys that can fill at least one of their respective cases but there's a remainder
# round down to case because we don't sell partial cases
# e.g. Qty Available = 168, Case Count = 50, then Qty Available is converted to = 150 
def qty_case_count_conv(df):
    df['Qty Conversion'] = np.nan
    for index, row in df.iterrows():
        if row['Qty. Available'] >= row['Case Count']:
            df.loc[index, 'Qty Conversion'] = row['Qty. Available'] - (row['Qty. Available'] % row['Case Count'])
    return df

# clean up the dupes after merging the 3 dfs from the aip endpoint downloads
def drop_dupe_rows(df):
    df = df.drop_duplicates(subset=['Inventory ID', 'Product Description', 'Strain'])
    return df

# delete rows with 0 value in a specified column (generally used for Qty Available for Sale)
def remove_row_with_zero_qty(df, col):
    df = df[df[f'{col}'] != 0]
    df = df[df[f'{col}'] != '']
    df = df[df[f'{col}'] != ' ']
    return df

# this will function will remove a row with a specified value in a specified column
# this is a separate function from the above with_zero_qty
# because that function accounts for nulls or ''
# the only current use case is to remove reserved strains for
# specific customers that shouldn't be available for wholesale
def remove_row_with_val_in_col(df, col, val):
    df = df[df[f'{col}'] != val]
    return df

# currently in acu the cfx gummy naming doesn't generally combine the flavor
# with it's effect (sleep, focus, etc.) so it's done here leveraging a hardcoded map
def update_cfx_gummies_description(df):
    df['Strain/Flavor'] = df['Strain/Flavor'].map(cs.cfx_gum_map).fillna(df['Strain/Flavor'])
    return df

# this will update the value in a column based on the represented valuesin a dictionary
def add_value_to_col_based_on_other_col(df, col_to_fill, map, based_on_col):
    df[f'{col_to_fill}'] = df[f'{based_on_col}'].map(map).fillna(df[f'{col_to_fill}'])
    return df

# create the main df that will drive the creation of the order form by combining
# the 3 dataframes from the 3 endpoint downloads
def merge_dfs(df1, df2, df3):
    
    merge_keys = ["Inventory ID", "Product Description", "Strain"]

    # merge in df2 into df1 first
    merged_df = pd.merge(
        df1, 
        df2[merge_keys + ['Total THC', 'THCA', 'Total Terpenes', 'TAC', 'Harvest Date']],
        on=merge_keys,
        how='left'
    )

    # now merge in df3 in
    merged_df = pd.merge(
        merged_df, 
        df3[merge_keys + ['Total THC', 'THCA', 'Total Terpenes', 'TAC', 'Harvest Date']],
        on=merge_keys,
        how='left',
        suffixes=('', '_in_transit')
    )

    cols_to_merge = ['Total THC', 'THCA', 'Total Terpenes', 'TAC', 'Harvest Date']

    # now drop the _y columns (from df3), and rename _x columns (from df2) back to normal
    for col in cols_to_merge:
        if f"{col}_x" in merged_df.columns:
            merged_df[col] = merged_df[f"{col}_x"]
        # drop both _x and _y to clean up
        merged_df.drop([f"{col}_x", f"{col}_y"], axis=1, inplace=True, errors='ignore')

    for col in cols_to_merge:
        in_transit_column = f"{col}_in_transit"
        # merge the columns
        merged_df[col] = merged_df[col].combine_first(merged_df[in_transit_column])
        # drop the _in_transit column
        merged_df.drop(columns=[in_transit_column], inplace=True)

    return merged_df

# hardcoded drop of columns found in download
def remove_columns(df):

    columns_to_drop = ['Base Price', 'Receipt Date', 'Package Date']
    df.drop(columns_to_drop, axis=1, inplace=True)
    # print(df)
    return df

# certain products, such as stir stix, gummies shouldn't show thc, tac, etc.
# this cleans that up 
def remove_batch_details(df):
    cols_to_remove_batch = cs.prod_desc_with_no_batch_val
    for x in cols_to_remove_batch:
        df['TAC'] = df['TAC'].where(df['Product Description'] != x)

    for x in cols_to_remove_batch:
        df['THC-A'] = df['THC-A'].where(df['Product Description'] != x)    
    
    for x in cols_to_remove_batch:
        df['Total THC'] = df['Total THC'].where(df['Product Description'] != x)    
    
    for x in cols_to_remove_batch:
        df['Total Terpenes'] = df['Total Terpenes'].where(df['Product Description'] != x)   
    
    return df

# remove older dates from a cell - anything older than 4 months
def remove_old_dates(df, col):
    cutoff_date = datetime.now() - timedelta(days=120)
    df[col] = pd.to_datetime(df[col])
    df[col] = df[col].apply(lambda x: '' if pd.isna(x) or x < cutoff_date else x.strftime('%m/%d/%Y'))
    return df    

# remove rows that are samples and not for sale
def remove_sample_rows(df, column_name, value):    
    return df[df[column_name] != value]

# adds specified column and populate with values based on the specified dictionary in constants file
def add_col_with_vals_from_dict(df, column_name, dictionary, new_column_name):
    df[new_column_name] = df[column_name].apply(lambda x: dictionary.get(x))
    return df

# move column
def move_column(df, col_name, new_col_location):
    which_column = df.pop(col_name)
    if new_col_location > len(df.columns):
        new_col_location = len(df.columns)
    df.insert(new_col_location, which_column.name, which_column)
    return df

# convert 'Inventory ID' to categorical with specified order 
# this groups like items together. so all FLWR-3.5-PLUS, PR-1, etc are grouped together
def order_by_inventory_id(df):
    
    df['Inventory ID'] = pd.Categorical(df['Inventory ID'], categories=cs.ordered_ids, ordered=True)

    # sort DataFrame by 'Inventory ID'
    df = df.sort_values(by=['Inventory ID'])
    return df

# add columns to end of df that will eventually get values (some static, some dynamic formulas)
# adding test string so the cells get the subsequent formatting 
def add_columns(df):

    new_columns = {
        'Available (CASE)': ' ',
        'Price/Case': ' ',
        'Order Quantity (CASE)': ' ',
        'Total': ' '
    }

    for column, value in new_columns.items():
        df = df.assign(**{column: value})
        
    return df

# insert separator row with category title (the rows that'll eventually be red, purple, green) 
def insert_start_row(df, cat_by_inventory_id):
    # empty list to hold new rows
    new_rows = []
    
    # iterate through *unique* Inventory IDs
    for inventory_id in df['Inventory ID'].unique():
        # get the category from the dictionary (default to '' if not found)
        category = cat_by_inventory_id.get(inventory_id, '')
        
        # Append the start row with category
        new_rows.append({'Inventory ID': None, 'Product Description': None, 'Strain/Flavor': f'{category}', 'I/S/H': None,
                         'THC-A': None, 'TAC': None, 'Total THC': None,
                         'Total Terpenes': None, 'Harvest Date': None, 'Net Weights/Volumes': None,
                         'Servings': None, 'Price/EA': None, 'Case Count': None, 'Qty. Available': None,
                         'Available (CASE)': None, 'Price/Case': None, 'Order Quantity (CASE)': None, 'Total': None})
        
        # append the rows corresponding to the current Inventory ID
        new_rows.extend(df[df['Inventory ID'] == inventory_id].to_dict(orient='records'))
    
    # create a new DataFrame with the newly added separator rows
    new_df = pd.DataFrame(new_rows)
    
    return new_df
