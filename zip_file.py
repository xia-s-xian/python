# importing required modules 
from zipfile import ZipFile 
import os 
  
def get_all_file_paths(directory): 
  
    # initializing empty file paths list 
    file_paths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
  
    # returning all file paths 
    return file_paths         
  
def main(): 
    # path to folder which needs to be zipped 
    #directory = '../../python_files'
    #directory
    directory_f=r'../FlashUpgradeTool'
    #path=os.getcwd()
    #directory =r"C:/Users/DELL/Desktop/"+r'FlashUpgradeTool'
    #print(directory)
    # calling function to get all file paths in the directory 
    file_paths = get_all_file_paths(directory_f) 
  
    # printing the list of all files to be zipped 
    print('Following files will be zipped:') 
    for file_name in file_paths: 
        print(file_name) 
  
    # writing files to a zipfile
    des=r'C:\Users\DELL\Desktop\my_python_files.zip'
    with ZipFile(des,'w') as zip: 
        # writing each file one by one 
        for file in file_paths:
            zip.write(file) 
  
    print('All files zipped successfully!')         
  
  
if __name__ == "__main__": 
    main()
    print( os.getcwd())
