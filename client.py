import socket
import sys

host = "localhost"
port = 12345

f = open("events.csv","r")
lines = f.readlines()
f.close

f = open("events.csv","w")
for line in lines:
    if line !="'Date','Time','Event'"+"\n":
        f.write(line)
f.close

s = socket.socket()
s.connect((host,port))
f=open ("events.csv", "rb")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
s.close()
