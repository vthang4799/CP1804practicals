CODE_COLORS = {"DarkGoldenrod": "b8860b", "DarkGoldenrod1": "ffb90f", "DarkGreen": "006400", "DarkKhaki": "bdb76b",
               "chocolate1": "ff7f24", "chartreuse2": "76ee00", "CadetBlue4": "53868b", "azure4": "838b8b",
               "bisque1": "ffe4c4", "BlanchedAlmond": "ffebcd"}
color_name = input("Enter a color name: ")
while color_name != "":
    if color_name in CODE_COLORS:
        print("The code for \"{}\" is {}".format(color_name, CODE_COLORS.get(color_name)))
    else:
        print("Invalid color name")
    color_name = input("Enter a color name: ")
