import socket
import pickle
import base64
import crcmod.predefined
from binascii import unhexlify

# 获取设备当前亮度
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 2929
addr = ('202.11.11.3', port)
a.connect(addr)
# 帧头
frame_header = b'\02'
# 地址
frame_addres1 = b'0'
frame_addres2 = b'0'
# 帧类型
frame_type1 = b'0'
frame_type2 = b'6'
# crc检验
crc16_xmodem = crcmod.mkCrcFun(0x11021, rev=False, initCrc=0x0000, xorOut=0x0000)
# 校验码拼接,拼接后为字符串
check_code = '3' + str(frame_addres1, 'UTF-8') + '3' + str(frame_addres2, 'UTF-8') + '3' + str(frame_type1, 'UTF-8') + '3' + str(frame_type2, 'UTF-8')
# 转为16进制，转后为16进制字符串
check_code = hex(crc16_xmodem(unhexlify(check_code)))
# 16进制字符串转为字节
check_code = check_code.encode()
# 转为字节后为六位，取后四位校验码
check_code = check_code[2:6:]
# 转为字节，格式为'\x**\x**'
check_code = base64.b16decode(check_code.upper())
# 帧尾
frame_end = b'\03'
# 组合帧Data
data = frame_header + frame_addres1 + frame_addres2 + frame_type1 + frame_type2 + check_code + frame_end
# 发送数据
a.send(data)
# 接受返回数据
msg = a.recv(1024)
# 断开连接
a.close()

msg = str(msg)
a = len(msg)
msg = msg[8:a-13:]
print("返回信息为:{}".format(msg))
if msg[0] == '1':
    print("亮度调节方式为：手动")
    print("显示亮度为：{}".format(int(msg[1:3:])+1))
elif msg[0] == '0':
    print("亮度调节方式为：自动")
    print("显示亮度为：{}".format(int(msg[1:3:])+1))
else:
    print("异常信息")



