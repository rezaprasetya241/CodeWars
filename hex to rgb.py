from PIL import ImageColor

def hex_string_to_RGB(hex_string):
    rgb = ImageColor.getrgb(hex_string)
    res = {
        'r': rgb[0],
        'g': rgb[1],
        'b': rgb[2]
    }
    return res

print(hex_string_to_RGB("#ff0000"))