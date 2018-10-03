#The line below will open a file containing information
#about every pokemon through Generation 7:

pokedex = open('pokedex.csv', 'r')

#We've also provided a sample subset of the data in
#sample.csv.
#
#Each line of the file has 13 values, separated by commas.
#They are: 
#
#
# - Number: The numbered ID of the Pokemon, an integer
# - Name: The name of the Pokemon, a string
# - Type1: The Pokemon's primary type, a string
# - Type2: The Pokemon's secondary type, a string (this
#   may be blank)
# - HP: The Pokemon's HP statistic, an integer in the range
#   1 to 255
# - Attack: The Pokemon's Attack statistic, an integer in
#   the range 1 to 255
# - Defense: The Pokemon's Defense statistic, an integer in
#   the range 1 to 255
# - SpecialAtk: The Pokemon's Special Attack statistic, an
#   integer in the range 1 to 255
# - SpecialDef: The Pokemon's Special Defense statistic, an
#   integer in the range 1 to 255
# - Speed: The Pokemon's Speed statistic, an integer in the
#   range 1 to 255
# - Generation: What generation the Pokemon debuted in, an
#   integer in the range 1 to 7
# - Legendary: Whether the Pokemon is considered "legendary"
#   or not, either TRUE or FALSE
# - Mega: Whether the Pokemon is "Mega" or not, either TRUE
#   or FALSE
#
#Use this dataset to answer the questions below.

regDict = {}
megaDict = {}
tempDict = {}
pokemon = pokedex.readlines()[1:]
maxDef = [0, ""]
lowestSum = [0,""]
megaCount = 0
megaSum2 = 0
regCount = 0
for line in pokemon:
    number, name, type1, type2, hp, attack, defense, specialAtk, specialDef, speed, generation, legendary, mega = line.strip().split(",")
    number, hp, attack, defense, specialAtk, specialDef, speed, generation = int(number), int(hp), int(attack), int(defense), int(specialAtk), int(specialDef), int(speed), int(generation)
    legendary, mega = True if legendary == "TRUE" else False, True if mega == "TRUE" else False
    
    currSum = 0
    currSum += hp + attack + defense + specialAtk + specialAtk + speed

    if mega:
        if number in megaDict:
            megaDict[number] = (megaDict[number] + currSum) /2
        megaDict[number] = 0
        megaDict[number] += currSum
        megaCount += 1
        megaSum2 += currSum
    else:
        if number not in regDict:
            regDict[number] = 0
        regDict[number] += currSum



megaSum = 0
regSum = 0

for k,v in megaDict.items():
    megaSum += v
    regSum += regDict[k]
    print(k)
# newDict = sorted(typeDict.items(), key=lambda kv : kv[1], reverse=True)
diff = round(megaSum / 46) - round(regSum / 46)
print("Difference:", diff)



