#Last problem, you wrote a function that generated the all-
#time win-loss-tie record for Georgia Tech against any other
#team.
#
#That dataset had a lot of other information in it. Let's
#use it to answer some more questions. As a reminder, the
#data will be a CSV file, meaning that each line will be a
#comma-separated list of values. Each line will describe one
#game.
#
#The columns, from left-to-right, are:
#
# - Date: the date of the game, in Year-Month-Day format.
# - Opponent: the name of the opposing team
# - Location: Home, Away, or Neutral
# - Points For: Points scored by Georgia Tech
# - Points Against: Points scored by the opponent


record_file = open('season2016.csv', 'r')
myDict = {}
oldest_Date = [100000,0,0]
oldest_opponent, mostPointsOpponent = "",""
home,neutral,away = [0, 0, 0], [0, 0, 0], [0, 0, 0]
wins2009, losses2009, ties2009 = 0, 0, 0
winsOctober, lossesOctober, tiesOctober = 0, 0, 0
winsSEC, lossesSEC, tiesSEC = 0, 0, 0
mostPoints = 0
gooseEgg = 0
for line in record_file:
    if line.strip() == "Date,Opponent,Location,Points For,Points Against":
        continue
    game = line.split(",")

    # find oldest date
    date = game[0].split("-")
    newyear, newmonth, newday = int(date[0]), int(date[1]), int(date[2])
    oldyear, oldmonth, oldday = int(oldest_Date[0]), int(oldest_Date[1]), int(oldest_Date[2])
    # if newyear < oldyear:
    #     oldest_Date = date
    # elif newyear == oldyear:
    #     if newmonth < oldmonth:
    #         oldest_Date = date
    #     elif newmonth == oldmonth:
    #         if newday < oldday:
    #             oldest_Date = date
    #             oldest_opponent = game[1]
        
            
    if game[1] not in myDict:
        myDict[game[1]] = [0, 0, 0, 0, 0]

    # # add to point totals
    myDict[game[1]][3] += int(game[3])
    myDict[game[1]][4] += int(game[4])

    # add to win totals
    if game[1] not in myDict:
        myDict[game[1]] = [0, 0, 0, 0, 0]
    if int(game[3]) > int(game[4]):
        myDict[game[1]][0] += 1
        if game[2] == "Home":
            home[0] += 1
        elif game[2] == "Away":
            away[0] +=1
        else:
            neutral[0] += 1
    elif int(game[3]) < int(game[4]):
        myDict[game[1]][1] += 1
        if game[2] == "Home":
            home[1] += 1
        elif game[2] == "Away":
            away[1] +=1
        else:
            neutral[1] += 1
    else:
        myDict[game[1]][2] += 1
        if game[2] == "Home":
            home[2] += 1
        elif game[2] == "Away":
            away[2] +=1
        else:
            neutral[2] += 1
    
    if newyear == 2009:
        if int(game[3]) > int(game[4]):
            wins2009 += 1
        elif int(game[3]) < int(game[4]):
            losses2009 += 1
        else:
            ties2009 += 1
    if newmonth == 10:
        if int(game[3]) > int(game[4]):
            winsOctober += 1
        elif int(game[3]) < int(game[4]):
            lossesOctober += 1
        else:
            tiesOctober += 1
    if newyear >= 1933 and newyear <= 1963:
        if int(game[3]) > int(game[4]):
            winsSEC += 1
        elif int(game[3]) < int(game[4]):
            lossesSEC += 1
        else:
            tiesSEC += 1

record_file.close()


#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.


# print("Oldest Opponent: ", oldest_opponent)
# print("points has Georgia Tech scored all-time against Auburn: ", myDict["Auburn"][3])
# print("points has Auburn scored all-time against Georgia Tech: ", myDict["Auburn"][4])
# print("Home alltime record: ", home)
# # print("Away alltime record: ", away)
# # print("Neutral alltime record: ", neutral)
# print(wins2009, losses2009, ties2009)
# print(winsOctober, lossesOctober, tiesOctober)
# print(winsSEC, lossesSEC, tiesSEC)

neverScoredAgainst = []
neverScoredAgainstByTeam = 0
maxScoringDiff = 0.0
maxScoringDiffTeam = ""
maxScoringDiffMin5 = 0.0
maxScoringDiffTeamMin5 = ""
for key,value in myDict.items():
    if value[3] == 0:
        neverScoredAgainst.append(key)
    if value[3] > mostPoints:
        mostPoints = value[3]
        mostPointsOpponent = key
    if value[4] == 0:
        neverScoredAgainstByTeam += 1
        value[4] = 0
    if value[3] - value[4] > maxScoringDiff:
        maxScoringDiffTeam = key
        maxScoringDiff = value[3] - value[4]
    if value[0] + value[1] + value[2] >= 5:
        numofgames = value[0] + value[1] + value[2]
        if (value[3] - value[4]) / numofgames > maxScoringDiffMin5:
            maxScoringDiffTeamMin5 = key
            maxScoringDiffMin5 = (value[3] - value[4]) / numofgames

print("Georgia Tech scored the most points", mostPointsOpponent)
print("How many teams has played Georgia Tech and never scored a point", neverScoredAgainstByTeam)
print("Highest scoring differential:", maxScoringDiffTeam)
print("Highest scoring differential Minimum of 5 games:", maxScoringDiffTeamMin5)