from PIL import Image, ImageFilter

before = Image.open("cat.jpg")
after = before.filter(ImageFilter.BoxBlur(2))
after.save("out.jpg")