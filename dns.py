
import socket
port 53
ip ="'pickatwu.github.io'

sock = socket.socket(socket.AF_INET, socket,SOCK_DRAM)
sock.bind((ip, port))

while 1;
data, addr = sock.recvfrom()
print()
