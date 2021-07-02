# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os

# out_file = open('out.txt','w')
out_dir = "out\\"

unify_width = 512
unify_height = 512

for filepath, dirnames, filenames in os.walk(r'C:\\Document\\test\\Python\\Annotations\\Annotations'):
    i = 0
    for filename in filenames:
        i = i + 1
        print(i)

        out_filename = filename.split(".")[0]
        while out_filename.find("0") == 0:
            out_filename = out_filename[1:]

        filename = "Annotations\\Annotations\\" + filename
        in_file = open(filename, 'r')
        out_file = open(out_dir + out_filename + ".txt", 'w')
        try:
            j = 0
            for line in in_file:
                if line.find("<width>") != -1:
                    width = line.split(">")[1]
                    width = width.split("<")[0]
                    float_width = float(width)
                if line.find("<height>") != -1:
                    height = line.split(">")[1]
                    height = height.split("<")[0]
                    float_height = float(height)

                if line.find("<xmin>") != -1 or line.find("<xmax>") != -1:
                    x = line.split(">")[1]
                    x = x.split("<")[0]
                    float_x = float(x)
                    float_x = float_x / float_width * unify_width
                    print(float_x, file=out_file, end=" ")
                    j = j + 1

                if line.find("<ymin>") != -1 or line.find("<ymax>") != -1:
                    y = line.split(">")[1]
                    y = y.split("<")[0]
                    float_y = float(y)
                    float_y = float_y / float_height * unify_height
                    print(float_y, file=out_file, end=" ")
                    j = j + 1

                if j == 4:
                    print("", file=out_file)
                    j = 0
        finally:
            in_file.close()
            out_file.close()