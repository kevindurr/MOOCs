#Write a function called count_types. count_types
#should take as input a single string, and return a
#dictionary. In the dictionary, the keys should be
#types of characters, and the values should be the
#number of times each type of character appeared in
#the string.
#
#The types of characters that should be handled (and
#thus, the keys in the dictionary) are:
#
# - upper: the count of upper-case or capital letters
# - lower: the count of lower-case letters
# - punctuation: the count of punctuation characters.
#   You may assume this is limited to these punctuation
#   characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# - space: the count of spaces
# - numeral: the count of numerals, 0123456789
#
#Note, however, that any type of character that does
#NOT appear in the string should not be in the dictionary
#at all.
#
#For example:
#
#count_characters("aabbccc") -> 
# {"lower": 7}
#count_characters("ABC 123 doe ray me!") -> 
# {"upper": 3, "lower": 8, "punctuation": 1, "space": 4, "numeral": 3}
#
#Because the first string has only lower-case letters,
#"lower" is the only key in the dictionary.
#
#HINT: If you're sing the ord() function, capitals of
#ordinals between 65 and 90; lower-case letters have
#ordinals between 97 and 122; numerals are between 48
#and 57; spaces are 32; all other numbers between 33
#and 126 are punctuations, and no character will have
#an ordinal outside that range.


#Write your function here!
def count_types(myString):
    upper, lower, punctuation, space, numeral = 0, 0, 0, 0, 0
    puncts = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    for char in myString:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in puncts:
            punctuation += 1
        elif char.isdigit():
            numeral += 1
        else:
            space += 1
    retDict = {}
    if upper > 0:
        retDict["upper"] = upper
    if lower > 0:
        retDict["lower"] = lower
    if punctuation > 0:
        retDict["punctuation"] = punctuation
    if space > 0:
        retDict["space"] = space
    if numeral > 0:
        retDict["numeral"] = numeral
    return retDict

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#
#{"lower": 7}
#{"upper": 3, "lower": 8, "punctuation": 1, "spaces": 4, "numerals": 3}
print(count_types("aabbccc"))
print(count_types("ABC 123 doe ray me!"))



