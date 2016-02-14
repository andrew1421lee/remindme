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

## Flexibility
RemindMe uses a simple universal file that can be created in nearly any language.
Just as a proof of concept, I included two examples:

A barebones Android app that can update event files on the fly. It can share the file using Android's robust share menu. It was made using MIT App Inventor

A barebones Windows GUI that can also update event files. It was made in Visual Basic. It won't work unless you have a file at exactly
```
C:\Users\andre\events\events.csv
```

##TODO

- Curfew settings - implement a way to restrict times where the bot can post

- Ability to tag users for events
