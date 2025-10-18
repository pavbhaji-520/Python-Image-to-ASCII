from time import sleep
from PIL import Image

def path_input():
    filePath = input("Enter Path of Image: ")

    while filePath.startswith("\""):
        filePath = filePath[1:]

    while filePath.endswith("\""):
        filePath = filePath[:-1]

    return filePath

def terminate():
    print("Terminating", end="")
    for i in range(3):
        print(".", end="")
        sleep(0.4)  # sleep for 0.4s
    exit(0)


def image_resize():
    aspectRatio = height / width
    newHeight = int(newWidth * aspectRatio * 0.5)  # 0.5 to compensate for the characters being taller than they are wide
    return image.resize((newWidth, newHeight))


def pixels_to_ascii():
    factor = 256 / (len(chars) - 1)  # have to convert 0 - 255 brightness into the characters we have

    asciiString = ""
    for pixel in pixels:
        asciiString += chars[int(pixel / factor)]

    #converting the string to a list which contains each row as a separate string
    grid = []
    rowStart = 0
    for row in range(height):
        grid.append(list(asciiString[rowStart:rowStart + width]))
        rowStart += width

    return grid


def print_separator():
    print("\033[0m", end = "")
    for i in range (max(2, height//100)): print("\n")

    for i in range (width): print("_", end = "")
    print()

    for i in range (max(2, height//100)): print("\n")


print("Enter 'Quit', 'Exit', or '0' to Terminate...")

newWidth = int(input("Enter resolution (width): "))
if newWidth in ['quit', 'exit', '0']: terminate()

chars = "`.-\':_\",^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"

while True:
    path = path_input()

    if path.lower() in ['quit', 'exit', '0']:
        terminate()

    try:
        image = Image.open(path)
    except FileNotFoundError:
        print("\033[0;31mProvided File Not Found\033[0m")
        continue
    except:
        print("\033[0;31mSomething went wrong when opening the file!\033[0m")
        continue

    #GETTING THE CHARACTERS TO BE PRINTED:
    width, height = image.size
    image = image_resize()
    width, height = image.size       # updating size to be the new size

    image = image.convert("L")       # converts to grayscale

    pixels = image.getdata()         # for each pixel the iterable returned by getdata(), add to the list
    # getdata() returns the brightness in 0 - 255 for grayscale images
    outputString = pixels_to_ascii()

    #colors
    image = Image.open(path)         # getting the image again to get colours (because we had converted to grayscale)
    image = image.convert("RGB")

    width, height = image.size
    image = image_resize()
    width, height = image.size

    colorPixels = image.load()

    # output
    print_separator()

    for y in range(height):
        for x in range(width):
            r, g, b = colorPixels[(x, y)]
            print(f"\033[38;2;{r};{g};{b}m", end = "")
            print(outputString[y][x], end ="")
        print()

    print_separator()
