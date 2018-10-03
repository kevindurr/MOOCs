names_file = open('babynames.csv', 'r')
#-----------------------------------------------------------
#The United States Social Security Administration publishes
#a list of all documented baby names each year, along with
#how often each name was used for boys and for girls. The
#list is used to see what names are most common in a given
#year.
#
#We've grabbed that data for any name used more than 25
#times, and provided it to you in a file called
#babynames.csv. The line below will open the file:


number_of_baby_names = 0
numberOfBirths = 0
mySet = set()
mostQnameNum = 0
mostQname = ""
vowelbabies = 0
myDict = {}

for line in names_file:
    number_of_baby_names += 1
    name, numbers, gender = line.strip().split(",")
    numbers = int(numbers)
    numberOfBirths += numbers
    if name not in myDict:
        myDict[name] = [0, 0]
    if gender == "Boy":
        myDict[name][0] += numbers
    if gender == "Girl":
        myDict[name][1] += numbers
    if name[0] == "Z" and gender == "Boy":
        mySet.add(name)
    elif name[0] == "Q" and gender == "Girl":
        if numbers > mostQnameNum:
            mostQnameNum = numbers
            mostQname = name
    if name[0] in ["A", "E", "I","O","U"] and name[len(name) - 1] in ["a", "e", "i","o","u"]:
        vowelbabies += numbers
leastCommon = 100000000
leastCommonName = ""
mostCommon = 0
mostCommonName = ""
for key,value in myDict.items():
    if value[0] < 25 or value[1] < 25:
        continue
    value = abs(value[0] - value[1])
    if value < leastCommon:
        leastCommon = value
        leastCommonName = key
    if value > mostCommon:
        mostCommon = value
        mostCommonName = key

# print("How many total names are listed in the database?",number_of_baby_names)
# print("How many total births are covered by the names in the database?",numberOfBirths)
# print("How many different boys' names are there that begin with the letter Z?", len(mySet))
# print("What is the most common girl's name that begins with the letter Q?", mostQname)
# print("How many total babies were given names that both start and end with vowels?", vowelbabies)
print("What letter is the least common first letter of a baby's name?", leastCommonName)
print("How many babies were born with names starting with that least-common letter?", leastCommon)
# print("What letter is the most common first letter of a baby's name?", mostCommonName)
# print("How many babies were born with names starting with that most-common letter?", mostCommon)










#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.
names_file.close()





