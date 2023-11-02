
def color_list():
    import colorgram
    # Load the image file
    image = "image.jpg"
    # Extract 10 colors from the image
    colors = colorgram.extract(image, 100)
    rgb_color_list = []
    # Print the colors as RGB tuples
    for color in colors:
        # rgba.append(color.rgb)
        # rgb = color.rgb # Get the RGB values
        # print(rgb)
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_color_list.append(new_color)
    # print(rgb_color_list)
    # print(len(rgb_color_list))
    return rgb_color_list