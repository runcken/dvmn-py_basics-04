from PIL import Image


image = Image.open('monro.jpg')
red, green, blue = image.split()

red_coordinates = (25, 0, red.width-25, red.height)
red_cropped = red.crop(red_coordinates)
red_shift_coordinates = (50, 0, red.width, red.height)
red_shifted = red.crop(red_shift_coordinates)

red_channel = Image.blend(red_cropped, red_shifted, 0.75)

blue_coordinates = (25, 0, blue.width-25, blue.height)
blue_cropped = blue.crop(blue_coordinates)
blue_shift_coordinates = (0, 0, blue.width-50, blue.height)
blue_shifted = blue.crop(blue_shift_coordinates)

blue_channel = Image.blend(blue_cropped, blue_shifted, 0.75)

green_coordinates = (25, 0, green.width-25, green.height)

green_channel = blue.crop(green_coordinates)

mixed_image = Image.merge('RGB', (red_channel, green_channel, blue_channel))
mixed_image.save('output.jpg')

mixed_image = gthumb

gthumb.thumbnail((80, 80))
gthumb.save('gthumb.jpg')