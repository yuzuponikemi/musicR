import os
import logging
import csv


# Set up logging
log_file_path = r'log.csv'  # replace with your desired path

def find_duplicates(start_path):
    seen_files = {}
    with open(log_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Duplicate Files1', 'Duplicate Files2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for dirpath, dirnames, filenames in os.walk(start_path):
            for filename in filenames:
                if filename.endswith('.mp3'):
                    file_path = os.path.join(dirpath, filename)
                    parent_folder = os.path.basename(dirpath)
                    key = (parent_folder, filename)
                    if key in seen_files:
                        writer.writerow({'Duplicate Files1': file_path, 'Duplicate Files2': seen_files[key]})
                    else:
                        seen_files[key] = file_path

find_duplicates(r'D:\Music')  # replace with your D drive path