import binascii
import struct

data_zh = "网络超时"
data_en = "timeout"

# 一、字符串转字节
# 1.1、中文字符串转字节(不同编码格式展示)：直接选择编码方式进行编码，就能转字节
gb_zh = data_zh.encode("GB2312")
print(gb_zh)  # b'\xcd\xf8\xc2\xe7\xb3\xac\xca\xb1'

gbk_zh = data_zh.encode("GBK")
print(gbk_zh)  # b'\xcd\xf8\xc2\xe7\xb3\xac\xca\xb1'  备注：GB2312是GBK的子集

utf_zh = data_zh.encode("utf-8")
print(utf_zh)  # b'\xe7\xbd\x91\xe7\xbb\x9c\xe8\xb6\x85\xe6\x97\xb6'
# print(data_zh.encode("ASCII"))  # 不支持
#
# 1.2、英文字符串转字节(不同编码格式展示)：直接选择编码方式进行编码，就能转字节
gb_en = data_en.encode("GB2312")
print(gb_en)  # b'timeout'
gbk_en = data_en.encode("GBK")
print(gbk_en)  # b'timeout'
utf_en = data_en.encode("utf-8")
print(utf_en)  # b'timeout'
asc_en = data_en.encode("ASCII")
print(asc_en)  # b'timeout'

print("----------------------------------")
# 1.3、字符串转16进制字节：先将字符串转字节，再转16进制
gb_zh_16 = binascii.b2a_hex(gb_zh)
print(gb_zh_16)  # b'cdf8c2e7b3accab1'
gb_en_16 = binascii.b2a_hex(gb_en)
print(gb_en_16)  # b'74696d656f7574'
print("----------------------------------")



# # 1.4、任意字符为16进制的字符串转字节：直接编码即可
gb_zh_16_str = 'cdf8c2e7b3accab1'
print(bytes().fromhex(gb_zh_16_str))  # b'\xcd\xf8\xc2\xe7\xb3\xac\xca\xb1'
#
# # 1.5、任意字符为16进制的字符串转16进制字节：直接编码即可
# gb_zh_16_str = 'cdf8c2e7b3accab1'
# print(gb_zh_16_str.encode())  # b'cdf8c2e7b3accab1'
#
# # 二、数字转字节
# # 2.1、数字转普通字节、大端序或小端序字节：直接通过struct模块打包实现
# num = 123
# print(struct.pack('@L' , num))  # b'{\x00\x00\x00'  按原字节转化成的普通字节
# print(struct.pack('=L' , num))  # b'{\x00\x00\x00'  按标准方式转化成的普通字节
# print(struct.pack('<L' ,
#                   num))  # b'{\x00\x00\x00' 小端序字节，相关参数请参考文章：https://blog.csdn.net/weixin_43431593/article/details/122078688
# print(struct.pack('>L' , num))  # b'\x00\x00\x00{' 大端序字节
#
# # 2.2、数字转16进制字节：先将数字转化成字节，再将字节格式化成16进制
# num_byte = struct.pack('@L' , num)
# print(binascii.b2a_hex(num_byte))  # b'7b000000' 字符串类型  注意，原编码决定了16进制长度和排序
#
# # 三、数字转字符串
# # 3.1、数字转普通字符串
# print(str(num))  # 123 字符串
# # 3.2、数字转16进制字符串
# print(hex(num))  # 0x7b
#
# # 四、字节转字符串
# # 4.1、任意字节均为16进制字符串，转字符串：直接转即可
# print(binascii.b2a_hex(num_byte).decode())  # 7b000000  字符串
# # 4.2、普通字节转16进制字符串：先将字节进行16进制处理，再转字符串
# # print(num_byte.decode())  # 非16进制字符串，直接解不出来
# num_byte_16 = binascii.b2a_hex(num_byte)
# print(num_byte_16.decode())  # 7b000000  字符串
#
# # 五、字节转数字
# # 4.1、普通字节转数字：需要知道原先的编码方式
# print(struct.unpack('@L' , num_byte))  # (123,)
# # 4.2、任意字节都为16进制的字节转数字:先转化成字符串，再数字
# print(int(num_byte_16.decode() , 16))  # 2063597568
#

