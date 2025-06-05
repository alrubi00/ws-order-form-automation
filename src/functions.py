import os
import time
import xlsx_functions as xfuns
import acumatica as acu
import pandas as pd
import df_functions as dfuns

# clean up function to keep the file count low in the output/data directory
# but still preserve recent output
def delete_old_files(directory, days=7):
        file_to_keep = ".gitkeep"
        seconds = days * 24 * 60 * 60
        now = time.time()
    
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            
            if os.path.isfile(file_path):
                if file != file_to_keep:
                    if os.stat(file_path).st_mtime < now - seconds:
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")

# was joinging enough file paths in main.py that i created this function
def join_dir_file(dir, file):
    file_path = os.path.join(os.path.dirname(__file__), dir, file)
    return file_path

def login_generate_download_report_df(report_id):
    start_session = acu.login()
    download_file = acu.generate_download_report(start_session, report_id)
    acu.close_acumatica_session(start_session)
    df = pd.read_excel(download_file, engine='calamine')

    if report_id == 'CLAEBAvailableNoGroup':
        df = dfuns.group_and_sort(df)
    
    return df

# def login_generate_download_report_df(path, date_for_file, report_id):
#     start_session = acu.login()
#     download_file = acu.generate_download_report(start_session, report_id)
#     end_session = acu.close_acumatica_session(start_session)
#     file_path = join_dir_file(path, f'{report_id}-cleaned-{date_for_file}.xlsx')
#     clean_file = xfuns.clean_excel_file(download_file, file_path)
#     df = pd.read_excel(clean_file)

#     if report_id == 'CLAEBAvailableNoGroup':
#         df = dfuns.group_and_sort(df)
    
#     return df

# can be any folder - but this was created with deleting the files in the tmp folder in mind
# once the script is done with them they can be delete to clear space 
def delete_files_from_directory(folder_path):
     file_to_keep = ".gitkeep"
     for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if file != file_to_keep:
            if os.path.isfile(file_path):
                os.remove(file_path)