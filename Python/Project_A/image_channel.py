from simpleimage import SimpleImage

def darker_channel(main_image):
    """ The darker image"""
    img = SimpleImage(main_image)
    for pixel in img:
        pixel.red = pixel.red // 2
        pixel.green = pixel.green // 2
        pixel.blue = pixel.blue // 2
    return img
def compute_luminosity(red, green, blue):
    return (0.299 * red) + (0.587 * green) + (0.114 * blue)
def gray_channel(main_image):
    """ The gray scaling image """
    image = SimpleImage(main_image)
    for pixel in image:
        luminosity = compute_luminosity(pixel.red, pixel.green, pixel.blue)
        pixel.red = luminosity
        pixel.green = luminosity
        pixel.blue = luminosity
    return image
def red_channel(main_image):
    img = SimpleImage(main_image)
    for pixel in img:
        pixel.blue = 0
        pixel.green = 0
    return img
def blue_channel(main_image):
    img = SimpleImage(main_image)
    for pixel in img:
        pixel.red = 0
        pixel.green = 0
    return img
def green_channel(main_image):
    img = SimpleImage(main_image)
    for pixel in img:
        pixel.red = 0
        pixel.blue = 0
    return img
def red_blue_channel(main_image):  # red_blue and blue_red change green
    img = SimpleImage(main_image)
    for pixel in img:
        pixel.green = 0
    return img
def red_green_channel(main_image): # red_green and green_red change blue
    img = SimpleImage(main_image)
    for pixel in img:
        pixel.blue = 0
    return img
def blue_green_channel(main_image): # blue_green and green_blue change red
    img = SimpleImage(main_image)
    for pixel in img:
        pixel.red = 0
    return img

def main():
    image = SimpleImage("images/green_land.jpg")
    image.show()
    # darker_channel image
    darker_image = darker_channel("images/green_land.jpg")
    darker_image.show()
    # gray_channel image
    gray_image = gray_channel("images/green_land.jpg")
    gray_image.show()
    # red channel image
    red_image = red_channel("images/green_land.jpg")
    red_image.show()
    # blue channel image
    blue_image = blue_channel("images/green_land.jpg")
    blue_image.show()
    # green channel image
    green_image = green_channel("images/green_land.jpg")
    green_image.show()
    # red_blue channel image
    red_blue_image = red_blue_channel("images/green_land.jpg")
    red_blue_image.show()
    # red_green channel image
    red_green_image = red_green_channel("images/green_land.jpg")
    red_green_image.show()
    # blue_green channel image
    blue_green_image = blue_green_channel("images/green_land.jpg")
    blue_green_image.show()

if __name__=='__main__':
    main()
