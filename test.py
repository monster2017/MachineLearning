from PIL import Image

im = Image.open('F:/MachineLearning/6043-1-1.png')
im_1 = im.convert("RGBA")

row,colums = im_1.size

for i in range(row):
    for j in range(colums):
        values = im_1.getpixel((i,j))
        print(values)
        if values==(255,255,255,255):
            im_1.putpixel((i,j),(255,255,255,0))
        else:
            im_1.putpixel((i,j),(0,0,0,0))

im_1.show()
im.save("F:/MachineLearning/6043-1-1.png")
