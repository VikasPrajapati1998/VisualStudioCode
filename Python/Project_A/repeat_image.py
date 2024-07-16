from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.png'
NUM_REPEATS = 2

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)
    image.show()
    w = image.width
    h = image.height
    # Create new SimpleImage of correct dimensions
    final_image = SimpleImage.blank(2 * w, h)
    print(image.width, image.height,)
    print(final_image.width, final_image.height)
    for x in range(w):
        for y in range(h):
            pixel = image.get_pixel(x, y)
            final_image.set_pixel(x, y, pixel)
            final_image.set_pixel(w+x, y, pixel)
    # Show the repeated image
    final_image.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
