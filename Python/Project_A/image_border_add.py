from simpleimage import SimpleImage


def main():
    image = SimpleImage('images/simba-sq.jpg')
    bordered_img = add_border(image, 10)
    bordered_img.show()



def add_border(original_img, border_size):
    # add twice the border size since we will have a border on both sides
    new_width = original_img.width + 2*border_size
    new_height = original_img.height + 2*border_size

    # gives us a blank image of size new_width and new_height
    bordered_img = SimpleImage.blank(new_width, new_height)
    for x in range(bordered_img.width):
        for y in range(bordered_img.height):
            if border_pixel(x, y, border_size, bordered_img):
                pixel = bordered_img.get_pixel(x, y)
                pixel.red = 0
                pixel.green = 0
                pixel.blue = 0
            else:
                # need to set pixel originally at (x,y) to shifted new position
                orig_x = x - border_size
                orig_y = y - border_size
                orig_pixel = original_img.get_pixel(orig_x, orig_y)
                bordered_img.set_pixel(x, y, orig_pixel)

    return bordered_img


def border_pixel(x, y, border_size, bordered_img):
    # left border
    if x < border_size:
        return True
    # right border
    if x >= bordered_img.width - border_size:
        return True
    # top border
    if y < border_size:
        return True
    # bottom border
    if y >= bordered_img.height - border_size:
        return True

    return False


if __name__ == '__main__':
    main()

