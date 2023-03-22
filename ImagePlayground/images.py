from PIL import Image , ImageFilter
img=Image.open(r"C:\Users\nandu\Desktop\Python\ImagePlayground\Pokedex\pikachu.jpg")
#print(img)
#print(img.format)
#print(img.size)
#print(img.mode)
#print(dir(img))  #what all the things which Image has given to us.

#blur the image
filter_image =img.filter(ImageFilter.BLUR)
filter_image.save("blur.png",'png')

filter_image =img.filter(ImageFilter.SHARPEN)
filter_image.save("SHARPEN.png",'png')

filter_image =img.filter(ImageFilter.SMOOTH)
filter_image.save("SMOOTH.png",'png')

filter_image =img.convert("L")
filter_image.save("Grey.png",'png')
resze=filter_image.resize((300,300)) #this is a tuple use this inside ()
crooked=filter_image.rotate(90)
box=(100,100,400,400)
crop_region=filter_image.crop(box)
crop_region.save("cropped.png",'png')
#crooked.show()
img2=Image.open(r"C:\Users\nandu\Desktop\Python\ImagePlayground\Pokedex\astro.jpg")
tumbnails=img2.resize((400,400))
tumbnails.save("tumbnailrezized.png",'png')

#if you don't want to squesh the image and get its best aspect ration, 
# like eg. a profile pic for facebook twitter like project use the method below.
img2.thumbnail((400,400))
img2.save("thumnail2.png",'png') 