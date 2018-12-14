#!/usr/bin/pyenv

print("hello world")

class Server(object):
    name = 'Server'

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def create(self):
        print("create a server") 


class TcpServer(Server):
    name = 'TcpServer'

    def __init__(self, ip, port):
        super(TcpServer, self).__init__(ip, port)
        self.type = 'TCP'
