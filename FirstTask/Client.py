__author__ = 'Konstantin'

import socket
sock = socket.socket()
sock.connect(('127.0.0.1',10101))
print("connected succeed! \n Enter you expression: ")

tmp = input()
sock.send(str(tmp))

data = sock.recv(256)
result = data
sock.close()


print 'result is ',result
