import socket
from _thread import *

server = "10.133.22.169"
port = 5555
address = (server, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(address)

s.listen(2)
print("Waiting for connections")

while True:
    conn, addr = s.accept()
    print("Connected to :", addr)