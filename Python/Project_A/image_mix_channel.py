from simpleimage import SimpleImage

def black_white():
    blank_image = SimpleImage.blank(1000, 700)
    w = blank_image.width
    h = blank_image.height
    for y in range(h):
        for x in range(w):
            pixel = blank_image.get_pixel(x, y)
            pixel.red = x/3.92
            pixel.green = x/3.92
            pixel.blue = x/3.92
            blank_image.set_pixel(x, y, pixel)
    return blank_image
def red_green():
    blank_image = SimpleImage.blank(1000, 700)
    w = blank_image.width
    h = blank_image.height
    for y in range(h):
        for x in range(w):
            pixel = blank_image.get_pixel(x, y)
            pixel.red = x/3.92
            pixel.green = y/2.74
            pixel.blue = 0
            blank_image.set_pixel(x, y, pixel)
    return blank_image
def red_blue():
    blank_image = SimpleImage.blank(1000, 700)
    w = blank_image.width
    h = blank_image.height
    for y in range(h):
        for x in range(w):
            pixel = blank_image.get_pixel(x, y)
            pixel.red = x/3.92
            pixel.green = 0
            pixel.blue = y/2.74
            blank_image.set_pixel(x, y, pixel)
    return blank_image
def green_blue():
    blank_image = SimpleImage.blank(1000, 700)
    w = blank_image.width
    h = blank_image.height
    for y in range(h):
        for x in range(w):
            pixel = blank_image.get_pixel(x, y)
            pixel.red = 0
            pixel.green = x/3.92
            pixel.blue = y/2.74
            blank_image.set_pixel(x, y, pixel)
    return blank_image
def gray_sketch():
    blank_image = SimpleImage.blank(1000, 700)
    w = blank_image.width
    h = blank_image.height
    for y in range(h):
        for x in range(w):
            pixel = blank_image.get_pixel(x, y)
            pixel.red = (x+y)/6.67
            pixel.green = (x+y)/6.67
            pixel.blue = (x+y)/6.67
            blank_image.set_pixel(x, y, pixel)
    return blank_image

def main():
    image1 = black_white()
    image1.show()
    image2 = gray_sketch()
    image2.show()
    image3 = red_green()
    image3.show()
    image4 = red_blue()
    image4.show()
    image5 = green_blue()
    image5.show()

if __name__=='__main__':
    main()
