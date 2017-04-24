import hashlib
import socket
import os
import base64

registeredPassword = raw_input("Enter registered password")
#salt = os.urandom(32).decode()
salt = base64.urlsafe_b64encode(os.urandom(32))
print("Salt is {}".format(salt))
digest = hashlib.sha1(salt + registeredPassword)
digest = digest.hexdigest()

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
ss.bind(("", 5000))
ss.listen(5)

clientsocket, address = ss.accept()
receivedPasswordDigestInKbs = clientsocket.recv(1024)

print("Digest is {}".format(digest))
print("Recieved is {}".format(receivedPasswordDigestInKbs))
if digest == receivedPasswordDigestInKbs:
    print("match")
else:
    print("no match")

clientsocket.close()
ss.close()


