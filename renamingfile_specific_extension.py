import os
folder_path="folder path"
for file_name in os.listdir(folder_path):
    old_file_path =os.path.join(folder_path,file_name)
    if os.path.isfile(old_file_path) and file_name.endswith("Png"):
        base_name, ext =os.path.splitext(file_name)
        new_file_name=f"{base_name}_renamed{ext}"
        new_file_path=os.path.join(folder_path,new_file_name)
        os.rename(old_file_path,new_file_path)
        print(f"renamed:{file_name} new file name {new_file_name}")

    