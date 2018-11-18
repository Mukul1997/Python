import socket

s = socket.socket()
port = 60001
host = socket.gethostname()

s.bind((host,port))
s.listen(5)

print('server running...')

while True:
    c,a = s.accept()
    print('connected to ',a)
    data = c.recv(4096)
    print('Expression recieved is ',data.decode())
    expr = (data.decode()).split()
    a = expr[0]
    b = expr[2]
    op = expr[1]

    if op == '+':
        res = int(a) + int(b)
    elif op == '-':
        res = int(a) - int(b)
    elif op == '*':
        res = int(a) * int(b)
    elif op == '/':
        res = int(a) / int(b)
    else:
        res = '@#$%&*'

    res = str(res)
    c.send(res.encode())
    c.close()
    break

s.close()
print('done')
