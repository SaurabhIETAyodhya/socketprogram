import socket

s = socket.socket()    #create socket function
print("scoket Created")

s.bind(('localhost',9999))     #bind socket with port number

s.listen(3)     #it will have buffer for 3 connection
print("waiting for connections")

while True:
    c, addr = s.accept()         #responsible for accept the connection
    name = c.recv(1024).decode()

    print("connected with", addr,name)

    c.send(bytes('welcome to IET faizabad','utf-8'))
    c.close()





