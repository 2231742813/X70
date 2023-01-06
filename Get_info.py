# import socket
# ip_port = ('202.11.11.3', 2929)
# s = socket.socket()
# s.connect(ip_port)
# mes = '0123'
# s.sendall(mes.isascii())
# s.close()


import socket
a = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 2929
addr = ('202.11.11.3', port)
a.connect(addr)
data = b'\x02\x30\x30\x30\x31\xca\xab\x03'
a.send(data)
msg = a.recv(1024)
print(type(msg))
print(msg)

msg = str(msg)
print(type(msg))
print(msg)
a.close()

