from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.png'
SQUARE_WIDTH = 200

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)
    image.show()
    center_square = SimpleImage.blank(SQUARE_WIDTH, SQUARE_WIDTH)
    w = image.width
    h = image.height
    # width=900 height=559

    # calculate coordinates of top left corner of centered square
    start_x = (w//2)-(SQUARE_WIDTH//2) # (900//2)-(200//2) = 350
    start_y = (h//2)-(SQUARE_WIDTH//2) # (560//2)-(200//2) = 180
    """
    # calculate coordinates of top left corner of centered square
    start_x = (image.width - SQUARE_WIDTH) // 2 # 900-200 = 700//2 = 350
    start_y = (image.height - SQUARE_WIDTH) // 2 # 559-200 = 359//2 = 180

    """
    for x in range(SQUARE_WIDTH):
        for y in range(SQUARE_WIDTH):
            pixel = image.get_pixel(start_x+x, start_y+y)
            center_square.set_pixel(x, y, pixel)
    # Show the image after the transform
    center_square.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
