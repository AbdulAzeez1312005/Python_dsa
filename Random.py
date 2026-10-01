import os
import shutil
from pathlib import Path

def organize_folder(folder_path: str):
    path = Path(folder_path)
    if not path.exists():
        print("Folder does not exist!")
        return

    # Categories mapped to extensions
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
        "Audio": [".mp3", ".wav", ".flac"],
        "Archives": [".zip", ".tar", ".gz", ".7z"],
        "Code": [".py", ".js", ".html", ".css", ".json"]
    }

    for file in path.iterdir():
        if file.is_dir():
            continue

        ext = file.suffix.lower()
        destination_folder = "Others"

        for category, extensions in categories.items():
            if ext in extensions:
                destination_folder = category
                break

        dest_dir = path / destination_folder
        dest_dir.mkdir(exist_ok=True)
        shutil.move(str(file), str(dest_dir / file.name))
        print(f"Moved: {file.name} -> {destination_folder}/")

# Example usage (replace with your folder path)
# organize_folder("./Downloads")
