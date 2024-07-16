"""
This program loads an image and applies the narok filter
to it by setting "bright" pixels to grayscale values.
"""

from simpleimage import SimpleImage

def compute_luminosity(red, green, blue):
    return (0.299 * red) + (0.587 * green) + (0.114 * blue)

def grayscale(file_name):
    image = SimpleImage(file_name)
    for pixel in image:
        x=pixel.x
        y=pixel.y
        pixel=image.get_pixel(x, y)
        luminosity = compute_luminosity(pixel.red, pixel.green, pixel.blue)
        pixel.red = luminosity
        pixel.green = luminosity
        pixel.blue = luminosity
        image.set_pixel(x, y, pixel)
    return image

def narko_filter(image, gray_image):
    width = image.width
    height = image.height
    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            avg = (pixel.red + pixel.green + pixel.blue)/3
            if avg>153:
                grey_pixel = gray_image.get_pixel(x, y)
                image.set_pixel(x, y, grey_pixel)
    return image

def main():
    image = SimpleImage('images/simba-sq.jpg')
    image.show()
    gray_image = grayscale('images/simba-sq.jpg')
    gray_image.show()
    narko_image = narko_filter(image, gray_image)
    narko_image.show()


if __name__ == '__main__':
    main()