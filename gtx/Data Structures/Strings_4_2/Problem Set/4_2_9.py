#This one is a challenge. There's a lot going on: splitting
#up strings, removing unnecessary characters, converting to
#integers, and running a big conditional. Our solution to
#this is 34 lines -- you can do it!
#
#In web development, it is common to represent a color like 
#this:
#
#  rgb(red_val, green_val, blue_val)
#
#where red_val, green_val and blue_val would be substituted 
#with values from 0-255 telling the computer how much to 
#light up that portion of the pixel. For example:
#
# - rgb(255, 0, 0) would make a color red. 
# - rgb(255, 255, 0) would make yellow, because it is equal 
#   parts red and green. 
# - rgb(0, 0, 0) would make black, the absence of all color.
# - rgb(255, 255, 255) would make white, the presence of all
#   colors equally.
#
#Don't let the function-like syntax here confuse you: here,
#these are just strings. The string "rgb(0, 255, 0)"
#represents the color green.
#
#Write a function called "find_color" that accepts a single 
#argument expected to be a string as just described. Your
#function should return a simplified version of the color
#that is represented according to the following rules:
#
# If there is more red than any other color, return "red".
# If there is more green than any other color, return "green".
# If there is more blue than any other color, return "blue".
# If there are equal parts red and green, return "yellow".
# If there are equal parts red and blue, return "purple".
# If there are equal parts green and blue, return "teal".
# If there are equal parts red, green, and blue, return "gray".
# (even though this might be white or black).


#Write your function here!
def find_color(rgb): 
    tup = rgb[4:-1].split(", ")
    r = int(tup[0])
    g = int(tup[1])
    b = int(tup[2])

    if r > g and r > b:
        return "red"
    if g > r and g > b:
        return "green"
    if b > r and b > g:
        return "blue"
    if r == g and b < r:
        return "yellow"
    if b == r and b > g:
        return "purple"
    if b > r and b == g:
        return "teal"
    if b == r and b == g:
        return "gray"
    if r == 0 and g == 0 and b == 0:
        return "black"
    if r == 255 and g == 255 and b == 255:
        return "white"
    
        

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: red, purple, gray, each on their own line.
print(find_color("rgb(125, 50, 75)"))
print(find_color("rgb(125, 17, 125)"))
print(find_color("rgb(217, 217, 217)"))



