import os

def rename_files_in_folders(root_directory):
    # Loop through each folder in the root directory
    for folder_name in os.listdir(root_directory):
        folder_path = os.path.join(root_directory, folder_name)

        # Check if the item in the directory is a folder
        if os.path.isdir(folder_path):
            # Get the list of files in the folder
            files = os.listdir(folder_path)

            # Loop through each file in the folder
            for file_name in files:
                file_path = os.path.join(folder_path, file_name)

                # Check if the item is a file and not a folder
                if os.path.isfile(file_path):
                    # Get the file extension
                    _, file_extension = os.path.splitext(file_name)

                    # Create the new file name based on the folder name
                    new_file_name = f"{folder_name}{file_extension}"

                    # Construct the new file path
                    new_file_path = os.path.join(folder_path, new_file_name)

                    # Rename the file
                    os.rename(file_path, new_file_path)

if __name__ == "__main__":
    root_directory = r'/path/to/your/directory'  # Replace this with the path to your root directory
    rename_files_in_folders(root_directory)