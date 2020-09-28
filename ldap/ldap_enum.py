import ldap3


'''
server = ldap3.Server('x.X.x.X', get_info = ldap3.ALL, port =636, use_ssl = True)
connection = ldap3.Connection(server)
connection.bind()
server.info
'''

IP = '10.10.10.192'
port = 3268

server = ldap3.Server(IP, get_info=ldap3.ALL, port=port)
connection = ldap3.Connection(server)
connection.bind()
information = server.info
print(information)
connection.search(search_base='DC=BLACKFIELD,DC=LOCAL', search_filter='(&(objectClass=*))', search_scope='SUBTREE', attributes='*')
entry = connection.entries
print(entry)
connection.search(search_base='DC=BLACKFIELD,DC=LOCAL', search_filter='(&(objectClass=person))', search_scope='SUBTREE', attributes='userPassword')
dump = connection.entries
print(dump)

