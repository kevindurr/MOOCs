from sys import argv
from cs50 import get_string

if (len(argv) == 2):
    key = int(argv[1])

    key = key % 26

    word = get_string("plaintext: ")

    print("ciphertext: ", end="")
    for letter in word:
        if(letter.islower()):
            print(chr(ord('a') + ((ord(letter) % 97) + key) % 26 ), end="")
        elif(letter.isupper()):
            print(chr(ord('A') + ((ord(letter) % 65) + key) % 26 ), end="")
        else:
            print(letter, end="")

    print()
else:
    exit(1)