#During elearnsecurity course PTS

import http.client

print('** This program return a list of methods if OPTIONS is enabled **\n')

host = input("Insert the server IP: ")
port = input("Insert the listening port: ")

if port == "":
    port = 80
try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('OPTIONS', '/')
    response = connection.getresponse()
    print("Enabled methods are: ", response.getheader('allow'))
    connection.close()
except ConnectionRefusedError:
    print("Connection Failed")
