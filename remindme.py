import groupy
import os
from time import strftime

#change working directory to directory of file so it can find events.csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Gets the currrent hours, minutes, month, and day
hours = strftime("%H")
minutes = strftime("%M")
month = strftime("%m")
day = strftime("%d")

#Math magic gets a unique single number (sctime) for the current time
sctime = int(hours)*60 + int(minutes)

#Makes currtime the standard time format (HH:MM)
#currtime = hours + ":" +minutes

#Makes currdate the standard date format (MM/DD)
currdate = month + "/" + day

#Initialize return value (Message that will be posted)
returnstring = ""

#Sets active groupchat
for g in groupy.Group.list().filter(name__contains='me'):
    chat = g
    
#Creates a new bot robot with the name 'RemindMe' in the group 'chat'
robot = groupy.Bot.create('RemindMe', chat)

#reads the file 'events.csv' and splits it into an array of lines
lines = [line.rstrip('\n') for line in open('events.csv')]

for i in lines:
    mystring =  i
    #splits the string by '|'
    listevent = mystring.split("|")
    #get the time of the event
    etime = listevent[1].split(":")
    #Math magic from before
    setime = int(etime[0])*60 + int(etime[1])
    #time difference from event and current time
    ctime = setime - sctime
    #If the date matches, and the event is in the next hour period, add the message to returnstring
    if currdate == listevent[0]:
        if ctime > 54 and ctime < 111:
            returnstring = returnstring + listevent[2] + ", "

#if there is something to post, post it
if returnstring != "":
    print(returnstring)
    robot.post(returnstring)
