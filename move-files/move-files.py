import os

# Define Paths for Source and Destination Folders
PATH_SOURCE_DIR = '/media/projects/source_folder'
# Example: /media/projects/source_folder'

PATH_DEST_DIR = '/media/projects/dest_folder'
# Example: /media/projects/dest_folder'

my_file = 'test_file.txt'


# def move_file(file_name, source_dir, dest_dir):
#     # Create full file path for source
#     source_path = os.path.join(source_dir, file_name)
#     # Create full file path for destination
#     dest_path = os.path.join(dest_dir, file_name)

#     # Move file
#     os.rename(source_path, dest_path)

# Calling function to move our file
# move_file(my_file, PATH_SOURCE_DIR, PATH_DEST_DIR)


def move_file(file_name, source_dir, dest_dir):

    # Create full file path for source
    source_path = os.path.join(source_dir, file_name)

    if file_name in os.listdir(dest_dir):
        # Separate file name part from its extension
        file_parts = file_name.split('.')
        # Add _01 to file name and combine it back with the extension
        file_name = file_parts[0] + '_01' + '.' + file_parts[1]

    # Create full file path for destination
    dest_path = os.path.join(dest_dir, file_name)
    
    # Move file
    os.rename(source_path, dest_path)


for file in os.listdir(PATH_SOURCE_DIR):
    move_file(file, PATH_SOURCE_DIR, PATH_DEST_DIR)
