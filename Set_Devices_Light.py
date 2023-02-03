import socket
import base64
import crcmod.predefined
from binascii import unhexlify
import random
from crcmod import mkCrcFun

# CRC16/XMODEM
def crc16_xmodem(s) :
        crc16 = mkCrcFun(0x11021 , rev=False , initCrc=0x0000 , xorOut=0x0000)
        return get_crc_value(s , crc16)

# common func
def get_crc_value(s , crc16) :
        data = s.replace(' ' , '')
        crc_out = hex(crc16(unhexlify(data))).upper()
        str_list = list(crc_out)
        if len(str_list) == 5 :
            str_list.insert(2 , '0')  # 位数不足补0
        crc_data = ''.join(str_list[2 :])
        return crc_data[:2] + ' ' + crc_data[2 :]


# 设备设备亮度调节方式
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 2929
addr = ('202.11.11.3', port)
a.connect(addr)
frame_header = b'\02'
frame_addres1 = b'0'
frame_addres2 = b'0'
frame_type1 = b'0'
frame_type2 = b'4'

# 亮度调节方式
setting_method = random.choice(['0', '1'])
setting_method = setting_method.encode()

frame_data = setting_method
check_code = '3' + str(frame_addres1, 'UTF-8') + '3' + str(frame_addres2, 'UTF-8') + '3' + str(frame_type1, 'UTF-8') + '3' + str(frame_type2, 'UTF-8') + '3' + str(frame_data, 'UTF-8')
check_code = crc16_xmodem(check_code)
check_code = check_code.replace(' ','')
check_code = check_code.encode()
check_code = base64.b16decode(check_code.upper())
# 帧尾
frame_end = b'\03'
# 组合帧Data
data = frame_header + frame_addres1 + frame_addres2 + frame_type1 + frame_type2 + frame_data + check_code + frame_end
# 发送数据
a.send(data)
# 接受返回数据
msg = a.recv(1024)
# 断开连接
a.close()


msg = str(msg)
a = len(msg)
msg = msg[6:a-12:]
# print("返回信息为:{}".format(msg))
if msg[0] == '0':
    print("返回信息为0，亮度调节方式设置成功")
else:
    print("异常信息")



