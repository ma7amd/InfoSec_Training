import socket
import sys

HOST = '192.168.0.100'
Port = 50000
s = None

for res in socket.getaddrinfo(HOST, Port, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print("Couldn't open a socket.")
    sys.exit(1)
with s:
    s.sendall(b'Hello World')
    data = s.recv(1024)
print("Received: ", repr(data))