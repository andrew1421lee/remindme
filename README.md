# RemindMe
Inspired by all those times the secretary of [*club name redacted*] forgot to remind people about upcoming events.

RemindMe is a GroupMe bot that, once told a list of upcoming events, can remind everyone in a group chat about upcoming events. A server is also included that allows clients to update the csv file through the network. The default setting sends reminders for events in the following hour.

Requires Python3 and GroupyAPI

Server only tested on Linux. Client also tested on Windows.

## Setup the Server
1. Make sure GroupyAPI is installed and .groupy.key file is made and in the correct place.

2. Put the scripts somewhere safe. For this tutorial, we will be putting it in ~/events

3. Create a new 'events.csv' file in the same directory as the script.
The 'events.csv' is formated like so:
```
"DD/MM","HH:MM","Description"
e.g
"02/14","21:23","9:23pm Event"
```
The first line (columns) is:
```
"Date","Time","Description"
```
(make sure to make a new line after)

4. Create a cron job to run the script every full hour.
```bash
crontab -e
0 * * * * /usr/bin/python3 /home/username/events/remindme.py
```
5. Run server.py

The server only needs server.py up 24/7 if you want to be able to update the events csv from another computer. You can edit the csv from the server manually also.

If you want to manually send a reminder, just run remindme.py.

## Setup the Client
1. On another computer, put the client.py script in a folder. For this tutorial it's in
```
C:\Users\Username\Events
```
2. The client script requires a events.csv file in the same directory. So copy the events.csv you made from before. Changes made to this csv file will be sent to the server when client.py is run (and server.py is listening).

3. Edit client.py so that the IP address matches that of the server's.
```python
host = "localhost" #most likely not localhost
port = 12345
```
4. Now just add your events to the events.csv and run client.py to send it to the Server.

###Optional showcase!
EventFileWriter.exe is a simple Visual Basic program that provides a GUI for editing the events.csv file.
Make sure events.csv exists and is formatted properly before launching.

(psst, it works a charm under Wine. Don't tell Balmer)

## Customization

You can change the name of the ReminderBot by changing:
```python
robot = groupy.Bot.create('RemindMe', chat)
```

You can change where the bot posts by changing:
```python
for g in groupy.Group.list().filter(name__contains='me'):
```
