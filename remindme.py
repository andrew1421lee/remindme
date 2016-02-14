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
#returnstring = ""
eventlist = []

#Sets active groupchat
for g in groupy.Group.list().filter(name__contains='me'):
    chat = g

#Creates a new bot robot with the name 'RemindMe' in the group 'chat'
robot = groupy.Bot.create('RemindMe', chat)

#reads the file 'events.csv' and splits it into an array of lines
lines = [line.rstrip('\n') for line in open('events.csv')]

eventcount = 0



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
            eventlist.append(listevent[2])
            #returnstring = returnstring + listevent[2] + ". "
            eventcount = eventcount + 1

#if there is something to post, post it
if len(eventlist) != 0:
    ihours = int(hours)
    if ihours < 12:
        robot.post("Good Morning! There are [" + str(eventcount) + "] event(s) in the next hour!")
    if ihours > 12 and ihours < 18:
        robot.post("Good Afternoon! There are [" + str(eventcount) + "] event(s) in the next hour!")
    if ihours > 18:
        robot.post("Good Evening There are [" + str(eventcount) + "] event(s) in the next hour!")
    for s in eventlist:
        robot.post(s)
