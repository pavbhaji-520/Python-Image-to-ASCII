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


def print_separator():
    print("\033[0m", end = "")                              # reset color to white
    for i in range (max(2, height//100)): print("\n")

    for i in range (width): print("_", end = "")
    print()

    for i in range (max(2, height//100)): print("\n")


print("Enter 'Quit', 'Exit', or '0' to Terminate...")

newWidth = int(input("Enter resolution (width): "))
if newWidth == 0: terminate()

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
            print(f"\033[38;2;{r};{g};{b}m", end = "") # setting the ANSI rgb color
            print("@", end ="")
        print()

    print_separator()
