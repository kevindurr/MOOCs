#Write a function called "load_file" that accepts one 
#parameter: a filename. The function should open the
#file and return the contents.#
#
# - If the contents of the file can be interpreted as
#   an integer, return the contents as an integer.
# - Otherwise, if the contents of the file can be
#   interpreted as a float, return the contents as a
#   float.
# - Otherwise, return the contents of the file as a
#   string.
#
#You may assume that the file has only one line.
#
#Hints:
#
# - Don't forget to close the file when you're done!
# - Remember, anything you read from a file is
#   initially interpreted as a string.


#Write your function here!
def load_file(fileName):
    myFile = open(fileName, "r")
    ret = myFile.readline().strip()
    myFile.close()
    if ret.count("-") == 1 or ret.count(".") == 1 or ret.isdigit():
        tmp = ret.replace("-","")
        if tmp.isdigit():
            return int(ret)
        if ret.count(".") == 1:
            tmp = tmp.replace(".","")
            if tmp.isdigit():
                return float(ret)
    return ret
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 123, followed by <class 'int'>.
contents = load_file("LoadFromFileInput.txt")
print(contents)
print(type(contents))




