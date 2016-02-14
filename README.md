# RemindMe
This Python script checks a csv file in it's directory and posts reminders for every event in the file.

Requires Python3 and GroupyAPI

Currently only tested on Linux.

## Setup to Bot
1. Make sure GroupyAPI is installed and .groupy.key file is made.

2. Put the script somewhere safe.

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
RemindMe csv files are extremely easy to create. Because the script will ignore old dates, you technically don't have to make a new file for a year!

Included is an Android app that showcases how easy it would be to update the bot event list.

##TODO

- Curfew settings - implement a way to restrict times where the bot can post

- Ability to tag users for events
