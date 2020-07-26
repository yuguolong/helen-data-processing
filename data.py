from imutils import paths

imagePaths = list(paths.list_images('../face-data/jpg/')) # 这个实用

print(imagePaths)
png_list = []
for i in imagePaths:
    name = i.split("/")[-1]
    name = name.split(".")[-2]
    png_list.append(name)

with open("./train.txt", "r+") as f:
    for i in png_list:
        i = str(i)
        f.writelines("%s.jpg;%s.jpg"%(i,i) +'\n') #能传入列表i
f.close()