import socket,sys,booth

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(("",5000))
ss.listen(5)

cs, address = ss.accept()
number = cs.recv(1024)

number = number.split(',')
print(number)

multiplicand = int(number[0])
multiplier = int(number[1])
multiplicandLength = int(number[2])
multiplierLength = int(number[3])

product = booth.booth(multiplicand, multiplier, multiplicandLength, multiplierLength)

print("Product is {}".format(product))

cs.close()
ss.close()
