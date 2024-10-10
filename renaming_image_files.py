import os

def rename_images_in_directory(folder_path):
    # Ensure the folder path is valid
    if not os.path.isdir(folder_path):
        print(f"The folder path {folder_path} is not valid.")
        return
    
    # Get the directory name
    directory_name = os.path.basename(folder_path)
    
    # Initialize the counter
    i = 1
    
    # Iterate over files in the directory
    for filename in os.listdir(folder_path):
        # Check if the file is a JPEG or WebP
        if filename.lower().endswith(('.jpeg', '.jpg', '.webp', '.png')):
            # Get the file extension
            file_extension = os.path.splitext(filename)[1]
            
            # Construct the new file name
            new_filename = f"{directory_name}_{i}{file_extension}"
            
            # Construct the full file paths
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            
            # Increment the counter
            i += 1
    
    print(f"Renamed {i-1} files in the directory {folder_path}.")

# Specify the folder path
folder_path = "/path/to/your/folder"

# Call the function to rename images
rename_images_in_directory(folder_path)
