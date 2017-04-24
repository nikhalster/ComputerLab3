import socket,sys,hashlib

print("")
print("Enter your password to gain a Kerberos ticket : ")
password = raw_input()
print("Enter salt")
salt = raw_input()
digest = hashlib.sha1(salt + password)
digest = digest.hexdigest()

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("",5000))

#passwordDigest = hashlib.sha1(password).hex
clientsocket.send(digest)

print("")
clientsocket.close()