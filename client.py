import socket
import sys

host = "localhost"
port = 12345
s = socket.socket()
s.connect((host,port))
f=open ("events.csv", "rb")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
s.close()
