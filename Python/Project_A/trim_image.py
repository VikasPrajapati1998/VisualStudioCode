from simpleimage import SimpleImage

def main():
    image = SimpleImage('images/simba.jpg')
    image.show()
    print(image.width, image.height)
    trimmed_img = trim_crop_image(image, 300)
    trimmed_img.show()


def trim_crop_image(original_img, trim_size):
    """
    This function returns a new SimpleImage which is a trimmed and
    cropped version of the original image by shaving trim_sz pixels
    from each side (top, left, bottom, right) of the image. You may
    assume trim_sz is less than half the width of the image.

    Inputs:
        - original_img: The original image to process
        - trim_size: The number of pixels to shave from each side
                   of the original image

    Returns:
        A new SimpleImage with trim_sz pixels shaved off each
        side of the original image
    """
    width = original_img.width
    height = original_img.height
    # Removing top pixels
    for y in range(trim_size+1):
        for x in range(width):
            pixel = original_img.get_pixel(x, y)
            pixel.red = 255
            pixel.green = 255
            pixel.blue = 255
    # Removing bottom pixels
    for y in range(height-trim_size, height):
        for x in range(width):
            pixel = original_img.get_pixel(x, y)
            pixel.red = 255
            pixel.green = 255
            pixel.blue = 255
    # Removing left pixels
    for x in range(trim_size):
        for y in range(height):
            pixel = original_img.get_pixel(x, y)
            pixel.red = 255
            pixel.green = 255
            pixel.blue = 255
    # Removing right pixels
    for x in range(width-trim_size, width):
        for y in range(height):
            pixel = original_img.get_pixel(x, y)
            pixel.red = 255
            pixel.green = 255
            pixel.blue = 255

    return original_img


if __name__ == '__main__':
    main()
