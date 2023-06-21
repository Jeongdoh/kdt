from PIL import Image




img = Image.open('newyork.jpg')
# print(img.size)
# print(img.format)
# img.show()

#newyork_size(1200, 864)


#1번
def ccw90(image):
    # width, height = image.size
    # Image.new(mode, size, color)
    new_image = Image.new("RGB", (864, 1200))
    for i in range(0,1200):
        for j in range(0,864):
            new_image.putpixel((j,1199-i),image.getpixel((i,j)))
    new_image.save('newyork-ccw90.jpg')

original = Image.open('newyork.jpg')
ccw90(original)


#2번
def mirror_image(image):
    # width, height = image.size
    # Image.new(mode, size, color)
    new_image = Image.new("RGB", (1200,864))
    for i in range(0,1200):
        for j in range(0,864):
            new_image.putpixel((1199-i,j),image.getpixel((i,j)))
    new_image.save('newyork-mirror.jpg')

original = Image.open('newyork.jpg')
mirror_image(original)
