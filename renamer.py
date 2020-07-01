# Author : Kalim M Puthawala
# Contact: @kalimputhawala on twitter
# Description : This is a bulk file renamer, can rename more than million files at your wish in your format.

import os
# change the file path to /home/kalim/Desktop/thatdirectory/  if you are on linux 
filepath = 'C:\\Users\\kalim\\Desktop\\thatdirectory\\'

custom_file_name = "sameFile.txt"

for root, dirs, files in os.walk("."):
    
    path = root.split(os.sep)
    dirname = os.path.basename(root)
    working_dir = (filepath+dirname)
	# This is how you give custom file name if for example, you need to increment.
    # x=0    
	# custom_file_name = str(x) + ".txt"

    for file in files:
    
        if(file=="renamer.py"):
            continue
        else:
            new_filename = custom_file_name
            old_path = os.path.join(working_dir,file)
            new_path = os.path.join(working_dir,new_filename)
            print(old_path,new_path)
            os.rename(old_path,new_path)
        # x=x+1  

