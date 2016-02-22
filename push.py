import socket
import sys

host = "localhost"
port = 12345

date = input('Date << MM/DD:')
time = input('Time << 24:00:')
name = input('Event << String:')

event = (date + "," + time + "," + name + "\n")

#print("Event is : " + event)

#print(bytes(event, encoding='utf-8'))

s = socket.socket()
print("Connecting to host...")
s.connect((host,port))
print("Sending event")
r = s.send(bytes(event, encoding='utf-8'))
