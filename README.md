# RemindMe
This Python script checks a csv file in it's directory and posts reminders for every event in the file.

Requires Python3 and GroupyAPI

Currently only tested on Linux.

## Setup
1. Make sure GroupyAPI is installed and .groupy.key file is made.

2. Put the script somewhere save.

3. Create a new 'events.csv' file in the same directory as the script.
The 'events.csv' is formated like so:
```
"DD/MM","HH:MM","EVENT DESCRIPTION"
```
4. Create a cron job to run the script every full hour.

## Customization

You can change the name of the ReminderBot by changing:
```python
robot = groupy.Bot.create('RemindMe', chat)
```

You can change where the bot posts by changing:
```python
for g in groupy.Group.list().filter(name__contains='me'):
```

## Android Companion App
RemindMe comes with a barebones Android app that can generate csv files on the fly. It can also share the file using Android's robust share menu.

##TODO

- Curfew settings - implement a way to restrict times where the bot can post

- Ability to tag users for events
