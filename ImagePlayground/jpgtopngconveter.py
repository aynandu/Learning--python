import sys
import os
from PIL import Image

#Executing terminal from C:\Users\nandu\Desktop\Python\ImagePlayground> 
# >python jpgtopngconveter.py Pokedex\ new\

#grab first and second argument with sys
image_folder=sys.argv[1]
output_foder=sys.argv[2]
print(image_folder, output_foder)
#check if new folder created or existed if not create one with os
if not os.path.exists(output_foder):
    os.makedirs(output_foder)

#loop through pokedex using os
for fileName in os.listdir(image_folder):

#Convert images to PNG
    img=Image.open(f'{image_folder}{fileName}')
#Save to the new Folder
    clearName=os.path.splitext(fileName)[0]
    img.save(f'{output_foder}{clearName}.png','png')
    print("all done")






    

