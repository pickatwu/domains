
import socket
port 53
ip ="'pickatwu.github.io'

sock = socket.socket(socket.AF_INET, socket,SOCK_DRAM)
sock.bind((ip, port))

def buildresponse(data):

  TransactionID = data[0:2]
  
  for byte in TransactionID:
    print(byte)
  
while 1;
data, addr = sock.recvfrom(512)
print(Data)
sock.sendto(b'Load',addr)

r =buildresponse(data)
sock.sendto(r ,addr)
