from PIL import Image
#from python image library
def get_image_hex_colors(image_path):
    #open tha image
    image = Image.open(image_path)
    #easier variable

    #get the super cool (229 x 255) dimensions of the image
    width, height = image.size

    #make empty list to store hex codes
    hex_values = []

    #repeat for each pixel because we dont miss !!!!!!
    for y in range(height):
        for x in range(width):
            #get rgb from image
            r, g, b = image.getpixel((x, y))

            #get hex from rgb
            hex_color = f'{r:02X}{g:02X}{b:02X}'
            hex_values.append(hex_color)

    return hex_values


image_path = "itto.png"
hex_colors = get_image_hex_colors(image_path)

f = open("hex.txt", "r+")
f.write("")
# print the hex codes
for color_code in hex_colors:
    f.write(f.read() + color_code)