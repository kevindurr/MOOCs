#Write a function called get_grade that will read a
#given .cs1301 file and return the student's grade.
#To do this, we would recommend you first pass the
#filename to your previously-written reader() function,
#then use the list that it returns to do your
#calculations. You may assume the file is well-formed.
#
#A student's grade should be 100 times the sum of each
#individual assignment's grade divided by its total,
#multiplied by its weight. So, if the .cs1301 just had
#these two lines:
#
# 1 exam_1 80 100 0.6
# 2 exam_2 30 50 0.4
#
#Then the result would be 72:
#
# (80 / 100) * 0.6 + (30 / 50) * 0.4 = 0.72 * 100 = 72


#Write your function here!
def reader(fileName):
    myFile = open(fileName, "r")
    theList = []
    for line in myFile:
        split = line.split()
        theList.append((int(split[0]),str(split[1]),int(split[2]), int(split[3]), float(split[4])))
    myFile.close()
    return theList

def get_grade(fileName):
    myList = reader(fileName)
    sum = 0
    for myTup in myList:
        sum += (myTup[2] / myTup[3]) * myTup[4]
    return sum * 100


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 91.55 
print(get_grade("sample.cs1301"))





