import crcmod.predefined
from binascii import unhexlify


crc16_xmodem = crcmod.mkCrcFun(0x11021, rev=False, initCrc=0x0000, xorOut=0x0000)
s = '30303036'
print(hex(crc16_xmodem(unhexlify(s))))
res = hex(crc16_xmodem(unhexlify(s)))