import groupy
import os
from time import strftime
#os.chdir("/home/anchu/Documents/CS140/Code/tascbot/")
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#print(os.path.dirname(os.path.abspath(__file__)))
hours = strftime("%H")
minutes = strftime("%M")
month = strftime("%m")
day = strftime("%d")

sctime = int(hours)*60 + int(minutes)
currtime = hours + ":" +minutes

currdate = month + "/" + day
returnstring = ""
chat = groupy.Group.list().last
robot = groupy.Bot.create('RemindMe', chat)

lines = [line.rstrip('\n') for line in open('events.csv')]

for i in lines:
    mystring =  i
    listevent = mystring.split("|")
    etime = listevent[1].split(":")
    setime = int(etime[0])*60 + int(etime[1])
    ctime = setime - sctime
    if currdate == listevent[0]:
        if ctime > 54 and ctime < 111:
            returnstring = returnstring + listevent[2] + ", "
if returnstring != "":
    print(returnstring)
    robot.post(returnstring)
