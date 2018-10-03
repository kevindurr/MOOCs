from sys import argv
from cs50 import get_string

if (len(argv) == 2):

    key = argv[1]
    for letter in key:
        if not letter.isalpha():
            exit(1)

    word = get_string("plaintext: ")
    i = 0

    print("ciphertext: ", end="")
    for letter in word:

        if key[i].isupper():
            cipher = ord(key[i]) % 65
        else:
            cipher = ord(key[i]) % 97

        if(letter.islower()):
            print(chr(ord('a') + ((ord(letter) % 97) + cipher) % 26 ), end="")
            i += 1
        elif(letter.isupper()):
            print(chr(ord('A') + ((ord(letter) % 65) + cipher) % 26 ), end="")
            i += 1
        else:
            print(letter, end="")

        if i == len(key):
            i = 0
    print()
else:
    exit(1)