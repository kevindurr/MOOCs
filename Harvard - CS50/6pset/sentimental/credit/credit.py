from cs50 import get_int

cardint = get_int("Number: ")
cardstr = str(cardint)
cardsum, remainder, i = 0, 0, 0

while cardint > 0:
    remainder = cardint % 10
    cardint //= 10
    if i % 2 == 0:
        cardsum += remainder
    else:
        if remainder * 2 >= 10:
            remainder *= 2
            cardsum += remainder % 10
            remainder //= 10
            cardsum += remainder
        else:
            cardsum += remainder * 2
    i += 1

if (cardsum % 10 != 0):
    print("INVALID")
elif (len(cardstr) == 15) and (cardstr[:2] == "34" or cardstr[:2] == "37"):
    print("AMEX")

elif (len(cardstr) == 16) and (cardstr[:2] >= "51" and cardstr[:2] <= "55"):
    print("MASTERCARD")

elif (len(cardstr) == 13 or len(cardstr) == 16) and cardstr[:1] == "4":
    print("VISA")

else:
    print("INVALID")
