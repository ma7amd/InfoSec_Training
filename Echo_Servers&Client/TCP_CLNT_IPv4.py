'''
# Elearning PTS course
import socket

SRV_ADDR = input("Type the server IP address: ")
SRV_PORT = int(input("Specify the port: "))

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect((SRV_ADDR, SRV_PORT))
print("Connection established")

msg = input("Type your message: ")
my_sock.sendall(msg)
my_sock.close()
'''

# better try to maintain the close signal
import socket

HOST = '192.168.0.100'
Port = 50000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, Port))
    msg = input("Type your message: ")
    b = msg.encode('utf-8')
    s.sendall(b)
    data = s.recv(1024)
print("Received: ", repr(data))