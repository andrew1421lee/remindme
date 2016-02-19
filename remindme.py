import groupy
import os
import csv
from time import strftime
import configparser

#change working directory to directory of file so it can find files
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#configuration
config = configparser.ConfigParser()
config.read('config')
filename = config.get('Server', 'file_name')
min_time = int(config.get('Server', 'minimum-time'))
max_time = int(config.get('Server', 'maximum-time'))
groupname = config.get('Server', 'group_name')
before12a = config.get('Text', 'before12a')
before12b = config.get('Text', 'before12b')
after12a = config.get('Text', 'after12a')
after12b = config.get('Text', 'after12b')
after6a = config.get('Text', 'after6a')
after6b = config.get('Text', 'after6b')

hours = strftime("%H")
minutes = strftime("%M")
month = strftime("%m")
day = strftime("%d")
sctime = int(hours)*60 + int(minutes)
currdate = month + "/" + day
eventlist = []
robot = groupy.Bot.list().first

#reads the file 'events.csv' and splits it into an array of lines
#lines = [line.rstrip('\n') for line in open('events.csv')]
eventcount = 0
with open(filename, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] != "Date":
            etime = row[1].split(":")
            setime = int(etime[0])*60 + int(etime[1])
            if(int(etime[0]) > 12):
                etime[0] = int(etime[0]) -12
            ctime = setime - sctime
            if currdate == row[0]:
                if ctime > min_time and ctime < max_time:
                    eventlist.append(str(etime[0]) + ":" + etime[1] + " - " + row[2])
                    eventcount = eventcount +1

#if there is something to post, post it
if len(eventlist) != 0:
    ihours = int(hours)
    if ihours < 12:
        robot.post(before12a + str(eventcount) + before12b)
    if ihours >= 12 and ihours < 18:
        robot.post(after12a + str(eventcount) + after12b)
    if ihours >= 18:
        robot.post(after6a + str(eventcount) + after6b)
    for s in eventlist:
        robot.post(s)
