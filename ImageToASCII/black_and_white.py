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

    return asciiString


def print_seperator():
    print("\033[0m", end = "")
    for i in range (max(2, height//100)): print("\n")

    for i in range (width): print("_", end = "")
    print()

    for i in range (max(2, height//100)): print("\n")


print("Enter 'Quit', 'Exit', or '0' to Terminate...")

newWidth = int(input("Enter resolution (width): "))
if newWidth == 0: terminate()

isDarkMode = input("Using Dark Mode? (Y/n): ")[0]

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~i!lI;:,\"^\'.` "[::-1]
if isDarkMode.lower() == "n":
    chars = chars[::-1]

while True:
    path = path_input()

    if path.lower() in ['quit', 'exit', '0']:
        terminate()

    # noinspection PyBroadException
    try:
        image = Image.open(path)
    except:
        print("\033[0;31mSomething went wrong when opening the file!\033[0m")
        continue

    width, height = image.size
    image = image_resize()
    width, height = image.size

    # converts to grayscale
    image = image.convert("L")

    # pixels to ASCII
    # getdata() returns the brightness in 0 - 255 for grayscale images
    pixels = image.getdata()  # for each pixel the iterable returned by getdata(), add to the list
    output = pixels_to_ascii()

    # output
    print_seperator()

    rowStart = 0
    for row in range(height):
        print(output[rowStart:rowStart + width])
        rowStart += width

    print_seperator()
