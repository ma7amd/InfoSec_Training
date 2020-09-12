'''
import socket

TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPSocket.bind(("0.0.0.0", 8000))
TCPSocket.listen(2)
(client, (ip, port)) = TCPSocket.accept()
TCPSocket.close()
'''

#------------------------------------------------------------------------------------------------------------------------------------#

'''
# eLearnSecurity 2019
import socket
SRV_ADDR = "192.168.0.10"
SRV_PORT = 44444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print("Server started! Waiting for connections...")
connection, address = s.accept()
print('Client connected with address:', address)
while 1:
    data = connection.recv(1024)
    if not data: break
    #connection.sendall(b'-- Message Received --\n')
    print(data.decode('utf-8'))
connection.close()
'''
#------------------------------------------------------------------------------------------------------------------------------------#

# A more better way of a TCP server that maintain the connection without sending close signal.

#Server with IPv4 setup only

import socket

HOST = ''
Port = 50000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, Port))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by ', addr)
        while True:
            data = conn.revv(1024)
            if not data: break
            conn.sendall(data)
