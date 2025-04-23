import os
import time

# clean up function to keep the file count low in the output/data directory
def delete_old_files(directory, days=7):
        seconds = days * 24 * 60 * 60
        now = time.time()
    
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            
            if os.path.isfile(file_path):
                if os.stat(file_path).st_mtime < now - seconds:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")

# was joinging enough file paths in main.py that i created this function
def join_dir_file(dir, file):
    file_path = os.path.join(os.path.dirname(__file__), dir, file)
    return file_path