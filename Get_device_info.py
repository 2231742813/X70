import socket
import binascii
import struct

a = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 2929
addr = ('202.11.11.3', port)
a.connect(addr)


data = b'\x02\x30\x30\x39\x37\x10\xf5\x03'
a.send(data)
msg = a.recv(1024)

print(type(msg))
print(msg)
# msg = str(msg)
# print(type(msg))
# print(msg)
print("-------------------")
#
# print(bytes().fromhex(msg))
# num = 12
# print(hex(num))



# 四、字节转字符串
# 4.1、任意字节均为16进制字符串，转字符串：直接转即可
print(binascii.b2a_hex(msg).decode())  # 7b000000  字符串
# 4.2、普通字节转16进制字符串：先将字节进行16进制处理，再转字符串
# print(msg.decode())  # 非16进制字符串，直接解不出来
msg=binascii.b2a_hex(msg)
print(msg.decode())  # 7b000000  字符串

a.close()
