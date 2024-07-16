from simpleimage import SimpleImage
TI = 1.6
image = SimpleImage('images/arjun_02.jpg')
image.show()
w = image.width
h = image.height
blank = SimpleImage.blank(2*w, h)
copy_blank = SimpleImage.blank(w, h)
mirror_blank = SimpleImage.blank(w, h)

for y in range(h):
    for x in range(w):
        pixel = image.get_pixel(x, y)
        copy_blank.set_pixel(x, y, pixel)
        mirror_blank.set_pixel(w-(x+1), y, pixel)

        blank.set_pixel(x, y, pixel)
        blank.set_pixel(2 * w - (x + 1), y, pixel)

copy_blank.show()
mirror_blank.show()
blank.show()
