import os
folder_path="path to folder"
prefix="hoga"
for file_name in os.listdir(folder_path):
    old_file_path=os.path.join(folder_path,file_name)
    if os.path.isfile(old_file_path):
        new_file_name=prefix+file_name
        new_file_path=os.path.join(folder_path,new_file_name)
        os.rename(old_file_path,new_file_path)
        print(f"renamed {file_name} to {new_file_name}")
    