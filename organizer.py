import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}


def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    moved_files = 0

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(file)

        moved = False

        for category, extensions in FILE_TYPES.items():
            if extension.lower() in extensions:

                category_folder = os.path.join(folder_path, category)

                os.makedirs(category_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(category_folder, file)
                )

                moved_files += 1
                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)

            shutil.move(
                file_path,
                os.path.join(other_folder, file)
            )

            moved_files += 1

    print(f"\nSuccess! {moved_files} files organized.")


def main():
    print("=" * 40)
    print("SMART FILE ORGANIZER")
    print("=" * 40)

    folder = input("\nEnter folder path: ").strip()

    organize_files(folder)


if __name__ == "__main__":
    main()
