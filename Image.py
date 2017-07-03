'''
背景色修改
'''
from PIL import Image

im = Image.open('F:/MachineLearning/6045-1.png')
#im.show()

row,colums = im.size
for i in range(row):
    for j in range(colums):
        values = im.getpixel((i,j))
        print(values)
        if values==255:
            im.putpixel((i,j),0)
        else:
            im.putpixel((i,j),255)
im.show()


im.save("F:/MachineLearning/6045-1.png")


