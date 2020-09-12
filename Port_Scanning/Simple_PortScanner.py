#During elearnsecurity course PTS

import socket

target = input("Enter the IP address of the machine: ")
port_range = input("Enter the port range you want to scan: (example 5-5000) ")

lower_port = int(port_range.split('-')[0])
higher_port = int(port_range.split('-')[1])

print('Scanning started for target ', target, 'from port ', lower_port, 'to port ', higher_port)

for port in range(lower_port, higher_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if status == 0:
        print("*** Port ", port, "- OPEN ***" )
    else:
        print("Port ", port, '- CLOSED')
        s.close()