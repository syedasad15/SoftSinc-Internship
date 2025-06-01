import os
import shutil

def organize():
    folder = input("Enter folder path to organize: ")
    FILE_TYPES = {
        "images": [".jpg", ".jpeg", ".png"],
        "docs": [".pdf", ".txt", ".docx"],
        "videos": [".mp4", ".mov"],
        "music": [".mp3", ".wav"],
        "archives": [".zip", ".tar", ".gz"]
    }

    try:
        for file in os.listdir(folder):
            path = os.path.join(folder, file)
            if os.path.isfile(path):
                ext = os.path.splitext(file)[1].lower()
                for cat, exts in FILE_TYPES.items():
                    if ext in exts:
                        target = os.path.join(folder, cat)
                        os.makedirs(target, exist_ok=True)
                        shutil.move(path, os.path.join(target, file))
                        break
        print("Files organized.")
    except Exception as e:
        print("Error:", e)
