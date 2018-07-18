#!/usr/bin/python

import sqlite3, csv, datetime

dataRoot = '/srv/maze/dataOutput/recent/'

temp = str(datetime.datetime.now())
time = ""

for i in temp:
    if i != "/" :
        time += i
    else :
        time += "-"


db = sqlite3.connect('/srv/sqlite/data/gameData')
cursor = db.cursor()
db.commit()

data = cursor.execute("SELECT * FROM LevelData")
levelOut = "levelOutput " + time + ".csv"
with open(dataRoot + levelOut, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['rowID', 'userName', 'currentLevel', 'trackCount', 'crashCount',
                     'stepCount', 'timeElapsed', 'totalEchoes', 'startTime', 'endTime', 'exitAttempts', 'asciiLevelRep',
                     'levelRecord', 'serverDateTimeStamp'])
    writer.writerows(data)

data = cursor.execute("SELECT * FROM EchoData")
echoOut = "echoOutput " + time + ".csv"
with open(dataRoot + echoOut, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['rowID', 'userName', 'currentLevel', 'trackCount', 
                     'echoLocation', 'postEchoAction', 'correctAction', 'dateTimeStamp'])
    writer.writerows(data)

data = cursor.execute("SELECT * FROM CrashData")
crashOut = "crashOutput " + time + ".csv"
with open(dataRoot + crashOut, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['rowID', 'userName', 'currentLevel', 'trackCount',  'crashNumber',
'crashLocation', 'dateTimeStamp'])
    writer.writerows(data)

data = cursor.execute("SELECT * FROM SurveyData")
surveyOut = "surveyOutput " + time + ".csv"
with open(dataRoot + surveyOut, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['rowID', 'surveyID', 'enjoy', 'playmore', 'easy', 'lost', 'understandecho', 
                     'frustrating', 'tutorial', 'tutorialhelp', 'hints', 'instructions', 
                    'controls', 'look', 'echonavigate', 'visuallyimpaired', 'hearingimpaired', 
                    'dateTimeStamp'])
    writer.writerows(data)

data = cursor.execute("SELECT * FROM SurveyIDData")
surveyIDOut = "surveyIDOutput " + time + ".csv"
with open(dataRoot + surveyIDOut, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['rowID', 'userName', 'surveyID', 'dateTimeStamp'])
    writer.writerows(data)

data = cursor.execute("SELECT * FROM ConsentIDData")
ConsentIDOut = "consentIDOutput " + time + ".csv"
with open(dataRoot + ConsentIDOut, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['rowID', 'userName', 'consentID', 'dateTimeStamp'])
    writer.writerows(data)

db.close()

print "Script Completed."

"""
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Generate CSVs</title>"
print "</head>"
print "<body>"
print "<h1> Success!</h1>"
print "</body>"
print "</html>"
"""
