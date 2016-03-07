import socket
import sys
import configparser
config = configparser.ConfigParser()
config.read('config')

host = config.get('Server','ip')
port = int(config.get('Server','port'))

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
