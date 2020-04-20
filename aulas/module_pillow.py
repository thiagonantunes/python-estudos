from PIL import Image

my_image = Image.open('imgtest.jpg')
new_image = my_image.resize()
new_image.save(r'C:\Users\Thiago\Documents\test.jpg')
