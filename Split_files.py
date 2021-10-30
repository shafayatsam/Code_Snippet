#Split file into different folders
#Move file according to their name

import os, os.path, shutil

file_path = "/home/shafayat/Downloads/archive (4)/images"
dest_pat = "/home/shafayat/Downloads/archive (4)/"

images = [f for f in os.listdir(file_path) if os.path.join(file_path, f)]

print(len(images))

for image in images:
    image_name = image.split('.')[0]
    if "train_add_s_" in image_name:
        shutil.move(file_path+'/'+image, dest_pat+'Apple_scab')
    elif 'train_add_r_' in image_name:
        shutil.move(file_path+'/'+image, dest_pat+'Apple_rust')
    elif 'Test_' in image_name:
        shutil.move(file_path+'/'+image, dest_pat+'test')
    else:
        shutil.move(file_path+'/'+image, dest_pat+'Apple_healthy')
        


