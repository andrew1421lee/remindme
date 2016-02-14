import socket
import sys

s = socket.socket()
s.connect(("localhost",50000))
f=open ("events.csv", "rb")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
s.close()
