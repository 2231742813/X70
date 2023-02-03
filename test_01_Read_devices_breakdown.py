# import socket
# import pickle
# import base64
# import crcmod.predefined
# from binascii import unhexlify
#
# # 获取设备当前故障
#
# a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
# port = 2929
# addr = ('202.11.11.3', port)
# a.connect(addr)
# # 帧头
# frame_header = b'\02'
# # 地址
# frame_addres1 = b'0'
# frame_addres2 = b'0'
# # 帧类型
# frame_type1 = b'0'
# frame_type2 = b'1'
# # crc检验
# crc16_xmodem = crcmod.mkCrcFun(0x11021, rev=False, initCrc=0x0000, xorOut=0x0000)
# check_code = '30303031'
# check_code = hex(crc16_xmodem(unhexlify(check_code)))
# check_code = check_code.encode()
# check_code = check_code[2:6:]
# check_code = base64.b16decode(check_code.upper())
# # 帧尾
# frame_end = b'\03'
# # 组合帧Data
# data = frame_header + frame_addres1 + frame_addres2 + frame_type1 + frame_type2 + check_code + frame_end
# # 发送数据
# a.send(data)
# # 接受返回数据
# msg = a.recv(1024)
# print(msg)
# # 断开连接
# a.close()
