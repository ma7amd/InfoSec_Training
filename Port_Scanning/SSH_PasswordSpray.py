import sys
import socket
import ipaddress
import paramiko

def checkPort(ip, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(0.5)
	result = sock.connect_ex((ip, port))
	if result == 0:
		return True
	else:
		return False


def checkPass(ip, usr, passwd):
	try:
		conn = paramiko.SSHClient()
		conn.set_missing_host_key_policy(paramikto.AutoAddPolicy())
		session = conn.connect(ip, 22, username=usr, password=passwd, timeout=1)
		conn.close()
		return True
	except Exception as e:
		print(e)
		return False


ipRange = sys.argv[1]
usr = str(sys.argv[2])
passwd = str(sys.srgv[3])
port = int(22)


for ip in ipaddress.IPv4Network(ipRange):
	if checkPort(str(ip), port):
		print('IP {0} has SSH Open'.format(ip))
		if checkPass(str(ip), usr, passwd):
			print('Working Creds on Host {0}'.format(ip))
