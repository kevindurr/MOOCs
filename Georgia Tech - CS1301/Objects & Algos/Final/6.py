#Let's try out a sort of data analysis-style problem. In
#this problem, you're going to have access to a data set
#covering Georgia Tech's all-time football history. The data
#will be a CSV file, meaning that each line will be a comma-
#separated list of values. Each line will describe one game.
#The columns, from left-to-right, are:
#
# - Date: the date of the game, in Year-Month-Day format.
# - Opponent: the name of the opposing team
# - Location: Home, Away, or Neutral
# - Points For: Points scored by Georgia Tech
# - Points Against: Points scored by the opponent
#
#If Points For is greater than Points Against, then Georgia
#Tech won the game. If Points For is less than Points Against,
#then Georgia Tech lost the game. If the two are equal, then
#the game was a tie.
#
#You can see a subsection of this dataset in season2016.csv
#in the top left, but the actual dataset you'll be accessing
#here will have 1237 games.
#
#Write a function called all_time_record. all_time_record
#should take as input a string representing an opposing team
#name. It should return a string representing the all-time
#record between Georgia Tech and that opponent, in the form
#Wins-Losses-Ties. For example, Georgia Tech has beaten
#Clemson 51 times, lost 28 times, and tied 2 times. So,
#all_time_record("Clemson") would return the string "51-28-2".
#
#We have gone ahead and started the function and opened the
#file for you. The first line of the file are headers:
#Date,Opponent,Location,Points For,Points Against. After that,
#every line is a game.


def all_time_record(opponent):
    record_file = open('season2016.csv', 'r')
    myDict = {}
    for line in record_file:
        if line.strip() == "Date,Opponent,Location,Points For,Points Against":
            continue
        game = line.split(",")
        if game[1] not in myDict:
            myDict[game[1]] = [0, 0, 0]
        if int(game[3]) > int(game[4]):
            myDict[game[1]][0] += 1
        elif int(game[3]) < int(game[4]):
            myDict[game[1]][1] += 1
        else:
            myDict[game[1]][2] += 1
    #Add some code here! Don't forget to close the file when 
    #you're done reading from it, before returning.
    record_file.close()
    if opponent in myDict:
        retString = str(myDict[opponent][0]) + "-" + str(myDict[opponent][1]) + "-" + str(myDict[opponent][2])
        return retString
    else:
        return False

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 51-28-2, 51-33-1, and 29-21-3, each on a separate
#line.
print(all_time_record("Clemson"))
print(all_time_record("Duke"))
print(all_time_record("North Carolina"))




