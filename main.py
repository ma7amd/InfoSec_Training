import socket

TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPSocket.bind(("0.0.0.0", 8000))
TCPSocket.listen(2)
(client, (ip, port)) = TCPSocket.accept()
TCPSocket.close()
