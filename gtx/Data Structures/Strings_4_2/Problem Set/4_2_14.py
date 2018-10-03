#In the previous problem, you wrote a function that would
#convert text like "abcd efgh ijkl" into "AbCd eFgH IjKl".
#
#In the previous problem, you could assume the original
#string would be all lower-case, with no punctuation.
#
#Revise your function so that it no longer makes these
#assumptions. It should leave any punctuation marks or
#numerals unchanged, and it should change the case of
#every letter at an even index. That means if the letter
#is initially uppercase, it should be converted to lower
#case.
#
#For example: mock("Abcd. Efgh.. Ijkl!") would return
#"abCd. efGh.. IJkL!". The even-index letters (A, C, E, g,
#j, l) changed case, all other characters were unchanged.
#
#HINT: Lowercase letters always have an ordinal between
#97 ("a") and 122 ("z"). Uppercase letters always have an
#ordinal between 65 ("A") and 90 ("Z").


#Write your function here!
def mock(s1):
    srr = ""
    for i in range(0,len(s1)):
        if i % 2 == 0 and s1[i].isalpha() and not s1[i].isupper():
            srr += chr(ord(s1[i]) - 32)
        elif i % 2 == 0 and s1[i].isalpha() and s1[i].isupper():
            srr += chr(ord(s1[i]) + 32)
        else:
            srr += s1[i]
    return srr

# if i % 2 == 0 and s1[i].isalpha():
            # srr += chr(ord(s1[i]) - 32) if not s1[i].isupper() else chr(ord(s1[i]) + 32)
            
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "A square with side length 4 has an area of 16".

print(mock("Abcd. Efgh.. Ijkl!"))



