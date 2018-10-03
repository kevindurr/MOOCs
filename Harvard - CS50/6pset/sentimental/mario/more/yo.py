from cs50 import get_int

def drawHash(height):
        print("#" * height, end="")

def drawSpace(space):
    print(" " * space, end="")

def main():
    while True:
        height = get_int("Height is: ")
        if (height >= 0 and height <= 23):
            break
    for i in range(height):
        symbol = i + 1
        space = height - symbol
        drawSpace(space)
        drawHash(symbol)
        print ("  ", end="")
        drawHash(symbol)
        print()

if __name__ == "__main__":
    main()