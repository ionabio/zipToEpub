import os
import zipfile
import shutil

def zip_folders_to_epub(source_dir):
    # Ensure the source directory exists
    if not os.path.exists(source_dir):
        print(f"The directory {source_dir} does not exist.")
        return

    # Iterate through all items in the source directory
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        
        # Check if the item is a directory
        if os.path.isdir(item_path):
            # Create a zip file name (same as folder name)
            zip_name = f"{item}.zip"
            epub_name = f"{item}.epub"
            zip_path = os.path.join(source_dir, zip_name)
            epub_path = os.path.join(source_dir, epub_name)
            
            # Create a ZipFile object
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Walk through all files and subdirectories in the folder
                for root, dirs, files in os.walk(item_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        # Calculate the archive name (path relative to the source directory)
                        arcname = os.path.relpath(file_path, item_path)
                        zipf.write(file_path, arcname)
            
            # Rename the zip file to .epub
            shutil.move(zip_path, epub_path)
            print(f"Created {epub_name}")

# Specify the source directory
source_directory = r"C:\path\to\your\folder"  # Replace with your actual path

# Run the function
zip_folders_to_epub(source_directory)