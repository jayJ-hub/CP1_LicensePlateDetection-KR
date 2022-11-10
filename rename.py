import os

cwd = os.getcwd()
path = cwd +'\data_img\img_carWithLicense'
files = os.listdir(path)
# print(files)

for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, str(index)+'.jpg'))


