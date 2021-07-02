import os
import cv2

# out_file = open('out.txt','w')
out_dir = "out\\"
folder_name = 'C:\\Users\\MITO2020\\Desktop\\数学暑期计算'

unify_width = 512
unify_height = 512

for filepath, dirnames, filenames in os.walk(r'C:\Users\MITO2020\Desktop\数学暑期计算'):
    i = 0
    for filename in filenames:
        print(filename)

        filename = os.path.join(folder_name, filename)
