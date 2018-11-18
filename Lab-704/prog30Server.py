import socket

s = socket.socket()
port = 60000
host = socket.gethostname()
s.bind((host,port))

s.listen(5)
print('Server Listening...')

while True:
	c,addr = s.accept()
	print("Connected to ",addr,"...")
	fp = open("recv.txt","wb")
	data = c.recv(4096)
	if not data:
		break
	fp.write(data)
	print("Data received...")
	break

fp.close()
s.close()
