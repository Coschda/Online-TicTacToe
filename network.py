import socket

class Network:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.133.22.169"
        self.port = 5555
        self.addr = (self.server, self.port)