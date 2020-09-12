# This server will allow connection on both IPv4 or IPv6
'''The server side will listen to the first address family available (it should listen to both instead).
On most of IPv6-ready systems, IPv6 will take precedence and the server may not accept IPv4 traffic.
The client side will try to connect to the all addresses returned as a result of the name resolution, and sends traffic to the first one connected successfully.'''



import socket
import sys

HOST = '192.168.0.100'
Port = 50000
s = None

for res in socket.getaddrinfo(HOST, Port, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('Could not open a socket')
    sys.exit(1)
conn, addr = s.accept()
with conn:
    print('connected by ', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)