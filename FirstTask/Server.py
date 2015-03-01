__author__ = 'Konstantin'

import asyncore
import socket
import threading


class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        test = 1
        data = self.recv(256)
        if len(data) > 0:
            method = data
            print(method)
            str(method)
            tmp = eval(method)

            self.send(str(tmp))



class SockServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(3)

    def handle_accept(self):
        pair = self.accept()
        if pair is None:
            pass
        else:
            sock, addr = pair
            print ('connection from host: %s' % repr(addr))
            handler = EchoHandler(sock)

class AsyncEventLoop (threading.Thread):

    def run(self):
        asyncore.loop()


server = SockServer('127.0.0.1', 10101)
evLoop = AsyncEventLoop()
evLoop.start()
