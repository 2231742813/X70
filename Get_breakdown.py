#!/usr/bin/env python
# -*- coding:utf-8 -*-

a=[{'type': 'light', 'hwVersion': 2, 'registerToken': '662357cd-e709-4235-af2e-1e443ec398b8', 'fwType': 16660, 'createTime': '2022-12-09T02:42:14.351Z', 'sn': '0000303875886676', 'swVersion': 272}]
print(type(a[0].values()))
print(a[0])
print(type(a[0]))
b = a[0]
print(b)
print(type(b))
print("分割")
print(b['type'])
print(a[0]['type'])

#
# import socket
#
# ip_port = ('202.11.11.3', 2929)
#
# s = socket.socket()  # 创建套接字
#
# s.connect(ip_port)  # 连接服务器
#
# while True:  # 通过一个死循环不断接收用户输入，并发送给服务器
#     inp = input("请输入要发送的信息： ").strip()
#     if not inp:  # 防止输入空信息，导致异常退出
#         continue
#     s.sendall(inp.encode())
#
#     if inp == "exit":  # 如果输入的是‘exit’，表示断开连接
#         print("结束通信！")
#         break
#
#     server_reply = s.recv(1024).decode()
#     print(server_reply)
#
# s.close()  # 关闭连接

# from socket import *
#
# # 创建socket
# tcp_client_socket = socket(AF_INET, SOCK_STREAM)
#
# # 目的信息
# server_ip = input("请输入服务器ip:")
# server_port = int(input("请输入服务器port:"))
#
# # 链接服务器
# tcp_client_socket.connect((server_ip, server_port))
#
# # 提示用户输入数据
# send_data = input("请输入要发送的数据：")
#
# tcp_client_socket.send(send_data.encode("gbk"))
#
# # 接收对方发送过来的数据，最大接收1024个字节
# recvData = tcp_client_socket.recv(1024)
# print('接收到的数据为:', recvData.decode('gbk'))
#
# # 关闭套接字
# tcp_client_socket.close()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #
# #
# # import socket
# #
# # # 1. 创建客户端的socket对象
# #
# # client = socket.socket()
# #
# # # 2. 连接服务端， 需要指定端口和IP
# #
# # client.connect(('10.10.10.68', 2929))
# #
# # # while True:
# # #
# # #     # 3. 给服务端发送数据
# # #
# # #     send_data = input("输入")
# # #
# # #     client.send(send_data.encode('ASCII'))
# # #
# # #     if send_data == 'quit':
# # #         break
# #
# #
# #     # 4. 获取服务端返回的消息
# #
# # recv_data = client.recv(1024).decode('utf-8')
# #     #
# #     # if recv_data == 'quit':
# #     #     break
# #
# # print("server:>%s" % (recv_data))
# #
# # # 5. 关闭socket连接
# #
# # client.close()
#
#
#
#
#
#
#
