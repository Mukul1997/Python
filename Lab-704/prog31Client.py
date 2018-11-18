import socket

s = socket.socket()
port = 60001
host = socket.gethostname()

s.connect((host,port))

exp = input('Enter expression  :')
s.sendall(exp.encode())
res = s.recv(4096)
print(res.decode())
s.close()
print('Client end')
