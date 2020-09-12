#During elearnsecurity course PTS

import http.client

host = input("Insert the server IP: ")
port = input("Insert the listening port: (default: 80) ")
url = input("Insert the URL: ")

if port == "":
    port = 80

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('GET', url)
    response = connection.getresponse()
    print("Server response: ", response.status)
    connection.close()
except ConnectionRefusedError:
    print("Connection failed.")