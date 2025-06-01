import os
import shutil
def copyfiles(sourcedir, destdir):
    if not os.path.isdir(sourcedir):
        print(f"Source directory '{sourcedir}' does not exist.")
        return
    if not os.path.exists(destdir):
        os.makedirs(destdir)
        print(f"Created destination directory: {destdir}")
    files = os.listdir(sourcedir)
    txt_csv_files = [f for f in files if f.endswith('.txt') or f.endswith('.csv')]
    if not txt_csv_files:
        print("No .txt or .csv files found.")
        return
    for file_name in txt_csv_files:
        source_path = os.path.join(sourcedir, file_name)
        destination_path = os.path.join(destdir, file_name)
        shutil.copy2(source_path, destination_path)
        print(f"Copied: {file_name}")
    print("All applicable files copied successfully.")
source = input("Enter the source directory path: ")
dest = input("Enter the destination directory path: ")
copyfiles(source, dest)
