import socket

s = socket.socket()
host = socket.gethostname()
port = 60000

s.connect((host, port))


print ('Sending data...')
try:
	fp = open('input.txt',"rb")
	data = fp.read()
	s.sendall(data)
	print("Data sent from client...")
	s.close()
	fp.close()

except FileNotFoundError:
	print("Error")
