import socket
import sys
import configparser
config = configparser.ConfigParser()
config.read('config')

host = config.get('Server','ip')#"128.226.247.65"
port = int(config.get('Server','port'))

f = open("events.csv","r")
lines = f.readlines()
f.close

f = open("events.csv","w")
for line in lines:
    #ignore formatting
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

open("events.csv", 'w').close

#f = open("events.csv", "w")
#f.write("Date,Time,Event" + "\n")
#f.close
