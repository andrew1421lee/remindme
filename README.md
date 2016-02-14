# RemindMe
This Python script checks a csv file in it's directory and posts reminders for every event in the file.

Requires Python3 and GroupyAPI

## Setup
1. Make sure GroupyAPI is installed and .groupy.key file is made.

2. Put the script somewhere save.

3. Create a new 'events.csv' file in the same directory as the script.
The 'events.csv' is formated like so:
''''
"DD/MM","HH:MM","EVENT DESCRIPTION"
''''
4. Create a cron job to run the script every full hour.

## Customization

You can change the name of the ReminderBot by changing:
'''python
robot = groupy.Bot.create('RemindMe', chat)
'''
