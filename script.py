import os

def delete_sh_files_in_directory(directory_path):
   try:
     files = os.listdir(directory_path)
     for file in files:
       file_path = os.path.join(directory_path, file)
       if os.path.isfile(file_path) and file.endswith(".sh"):
         os.remove(file_path)
     print("All .sh files deleted successfully.")
   except OSError:
     print("Error occurred while deleting .sh files.")

# Usage
directory_path = '/home/musili/Desktop/devops-assesment'
delete_sh_files_in_directory(directory_path)