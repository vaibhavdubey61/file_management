import os
import shutil

def organize_files():
    root_dir = "/path/to/files"
    folders = {
        "images": ["jpg", "png", "gif"],
        "videos": ["mp4", "avi", "mov"],
        "documents": ["docx", "pdf", "txt"]
    }

    for folder, extensions in folders.items():
        folder_path = os.path.join(root_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for file in os.listdir(root_dir):
            file_path = os.path.join(root_dir, file)
            file_ext = os.path.splitext(file)[1][1:]
            if file_ext in extensions:
                shutil.move(file_path, folder_path)

organize_files()  # run the file organizer
