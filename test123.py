import socket
import pickle
import base64

import crcmod.predefined
from binascii import unhexlify
crc16_xmodem = crcmod.mkCrcFun(0x11021, rev=False, initCrc=0x0000, xorOut=0x0000)
s = '30303036'
print(hex(crc16_xmodem(unhexlify(s))))
print(type(hex(crc16_xmodem(unhexlify(s)))))
test1 = hex(crc16_xmodem(unhexlify(s)))
res = test1.encode()
res = res[2:6:]
print(res)
print(type(res))
res = base64.b16decode(res.upper())
# res = hex(crc16_xmodem(unhexlify(s)))
# res = base64.b16decode(res.upper())

hex_str = 'ba'
print("--------------------------")
# print(base64.b16decode(hex_str.upper()))


a = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 2929
addr = ('202.11.11.3', port)
a.connect(addr)

frame_header = b'\02'
frame_addres1 = b'0'
frame_addres2 = b'0'
frame_type1 = b'0'
frame_type2 = b'6'
# frame_check = b'\xba'
frame_check = base64.b16decode(hex_str.upper())
frame_check1 = b'\x4c'
frame_end = b'\03'

# data = frame_header + frame_addres1 + frame_addres2 + frame_type1 + frame_type2 + frame_check + frame_check1 + frame_end
data = frame_header + frame_addres1 + frame_addres2 + frame_type1 + frame_type2 + res + frame_end
print(data)
# data = data.encode()
print(data)
# data = pickle.dumps(data)
a.send(data)
msg = a.recv(1024)
a.close()

print(ord('1'))
# print(int('\xbaL',16))
# print(int('0xbaL',16))


# print(type('abc'.encode('ascii')))