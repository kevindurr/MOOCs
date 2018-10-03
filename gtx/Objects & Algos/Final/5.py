#A common problem in academic settings is plagiarism
#detection. Fortunately, software can make this pretty easy!
#
#In this problem, you'll be given two files with text in
#them. Write a function called check_plagiarism with two
#parameters, each representing a filename. The function
#should find if there are any instances of 5 or more
#consecutive words appearing in both files. If there are,
#return the longest such string of words (in terms of number
#of words, not length of the string). If there are not,
#return the boolean False.
#
#For simplicity, the files will be lower-case text and spaces
#only: there will be no punctuation, upper-case text, or
#line breaks.
#
#We've given you three files to experiment with. file_1.txt
#and file_2.txt share a series of 5 words: we would expect
#check_plagiarism("file_1.txt", "file_2.txt") to return the
#string "if i go crazy then". file_1.txt and file_3.txt
#share two series of 5 words, and one series of 11 words:
#we would expect check_plagiarism("file_1.txt", "file_3.txt")
#to return the string "i left my body lying somewhere in the
#sands of time". file_2.txt and file_3.txt do not share any
#text, so we would expect check_plagiarism("file_2.txt",
#"file_3.txt") to return the boolean False.
#
#Be careful: there are a lot of ways to do this problem, but
#some would be massively time- or memory-intensive. If you
#get a MemoryError, it means that your solution requires
#storing too much in memory for the code to ever run to
#completion. If you get a message that says "KILLED", it
#means your solution takes too long to run.


#Add your code here!
def check_plagiarism(file1, file2):
    d1 = {}
    f1 = open(file1, "r")

    for line in f1:
        words = line.split()
        for i in range(0, len(words) - 5):
            if words[i] not in d1:
                d1[words[i]] = []
            d1[words[i]].append(words[i+1:i+5])
    f1.close()
    myList = []
    f2 = open(file2, "r")
    for line in f2:
        words = line.split()
        for i in range(0, len(words) - 5):
            if words[i] in d1:
                if words[i+1:i+5] in d1[words[i]]:
                    j = i + 5
                    k = i + 1
                    # print(words[k:j+1],d1[words[k]])
                    while(words[k+1:j+1] in d1[words[k]]):
                        k+=1
                        j+=1
                        if (j == len(words)):
                            break
                    if(len(words[i:j]) > len(myList)):
                        myList = words[i:j] 
    
    f2.close()
    if len(myList) == 0:
        return False
    else:
        return " ".join(myList)

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#if i go crazy then
#i left my body lying somewhere in the sands of time
#False
print(check_plagiarism("file_1.txt", "file_2.txt"))
print(check_plagiarism("file_1.txt", "file_3.txt"))
print(check_plagiarism("file_2.txt", "file_3.txt"))




