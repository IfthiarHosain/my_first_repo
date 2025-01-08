import  os 
import shutil
def organise_files(directory):
    file_types={
    "images":[".jpg",".jpeg",".png",".gif",".bmp"],
    "Documents":[".doc",".pdf",".txt",".xlsx",".pptx"],
    "Videos":[".mp4",".avi",".mov",".mkv"],
    "Others":[]
    }
    if not os.path.exists(directory):
        print("Directotry does not exist")
        return
    for item in os.listdir(directory):
        item_path=os.path.join(directory,item)

        if os.path.isdir(item_path):
          continue
        _,ext=os.path.splitext(item)
        catagory="others"
        for key, extentisons in file_types.items():
           if ext.lower() in extentisons :
            category=key
            break
        catagory_folder=os.path.join(directory,catagory)
        os.makedirs(category_folder,exist_ok=True)
        new_path=os.path.join(catagory_folder,item)
        shutil.move(item_path,new_path)
        print(f"moved:{item}-> {catagory}")
    print("file orgainization complete")
directory_path=input("enter the path of a directory to organize")
organise_files=directory_path
