#-----------------------------------------------------------
#Write a function called align_right. align_right should
#take two parameters: a string (a_string) and an integer
#(string_length), in that order.
#
#The function should return the same string with spaces
#added to the left so that the text is "right aligned" in a
#string. The number of spaces added should make the total
#string length equal string_length.
#
#For example: align_right("CS1301", 10) would return the
#string "    CS1301". Four spaces are added to the left so
#"CS1301" is right-aligned and the total string length is
#10.
#
#HINT: Remember, len(a_string) will give you the number of
#characters currently in a_string.


#Add your function here!
def align_right(s1, x):
    y = x - len(s1)
    return (y * " ") + s1
    # concise solution:
    # return ((x - len(s1)) * " ") + s1

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "    CS1301"
print(align_right("CS1301", 10))

#3/3 points