import groupy
import os
import csv
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
#lines = [line.rstrip('\n') for line in open('events.csv')]
eventcount = 0
with open('events.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        etime = row[1].split(":")
        setime = int(etime[0])*60 + int(etime[1])
        ctime = setime - sctime
        print(ctime)
        if currdate == row[0]:
            if ctime > 54 and ctime < 111:
                eventlist.append(row[2])
                eventcount = eventcount +1
                print("derp")
                print(eventlist)

#if there is something to post, post it
if len(eventlist) != 0:
    ihours = int(hours)
    if ihours < 12:
        robot.post("Good Morning! There are [" + str(eventcount) + "] event(s) in the following hour!")
    if ihours > 12 and ihours < 18:
        robot.post("Good Afternoon! There are [" + str(eventcount) + "] event(s) in the following hour!")
    if ihours > 18:
        robot.post("Good Evening! There are [" + str(eventcount) + "] event(s) in the following hour!")
    for s in eventlist:
        robot.post(s)
