from cs50 import get_int

def drawHash(height):
        for k in range(height):
            print("#", end="")

def drawSpace(space):
    for j in range(space):
        print(" ", end="")

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