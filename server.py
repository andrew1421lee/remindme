import socket
import sys
s = socket.socket()
s.bind(("localhost",50000))
s.listen(10) # Acepta hasta 10 conexiones entrantes.

while True:
    print("Waiting for Connection")
    sc, address = s.accept()
    print(str(address) + " connected!")
    f = open('buffer','wb') #open in binary
    print("Recieving Data")
    l = sc.recv(1024)
    while (l):
        f.write(l)
        l = sc.recv(1024)
    f.close()
    with open('buffer') as bh:
        with open('events.csv', 'a') as fh:
            print("Adding Event")
            fh.write(bh.read())
            #fh.write("\n")
    print("Good bye")

sc.close()

s.close()
