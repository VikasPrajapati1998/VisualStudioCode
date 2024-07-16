from simpleimage import SimpleImage


def main():
    arjun = SimpleImage('arjun.jpg')

    # width and height function of image
    width = arjun.width
    height = arjun.height
    print('Width in pixels(x):', width)
    print('Height in pixel(y):', height)

    # getting a particular pixel
    x = 210
    y = 312
    xy = arjun.get_pixel(x, y)
    print(xy)

    # getting a green value of a particular pixel
    xy_green = xy.green
    print('green = ', xy_green)

    avg = xy.red + xy.green + xy.blue
    avg = avg // 3
    print('avg = ', avg)


if __name__ == '__main__':
    main()
