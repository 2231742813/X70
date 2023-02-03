import socket

frame_header = '\02'
frame_address = '\30'
frame_address1 = '\30'
frame_type = '\30\36'
frame_check = '\ba\4c'
# frame_data = b''
frame_end = '\03'

a = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 2929
addr = ('202.11.11.3', port)
a.connect(addr)
# data = b'\x02\x30\x30\x30\x36\xba\x4c\x03'
data = b'\x02\x30\x30\x30\x36\xba\x4c\x03'
# data1 = b'\x30\x30\x36\xba\x4c\x03'
# data = data + data1
print(type(data))
print("+-----------------------")
print(data)
# data = frame_header + frame_address + frame_address1 + frame_type + frame_check + frame_end
print("-----------------------")
# print(data)
# data = data.encode()
# print("---------------")
# print(data)
a.send(data)
msg = a.recv(1024)
print(type(msg))
print(msg)
msg = msg.decode()
# print("---------------------")
# print(type(msg))
# print(msg)
a.close()

# a = '\x53'
# print(type(a))
# print(len(a))
# print(a)

