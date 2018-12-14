#!/usr/bin/pyenv

print("hello world")

class Server(object):
    name = 'MyServer'

class Client(object):
    name = 'Client'
    def __init__(self, type):
        self.type = type


class PCClient(Client):
    def __init__(self, type):
        super(PCClient, self).__init__(type)
        self.format = ''


