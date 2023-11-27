# -*- coding: utf-8 -*-


## TCP客户端
# import socket
# target_host = 'www.baidu.com'
# target_port = 80

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# client.connect((target_host,target_port))

# client.send(b"GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n")

# response = client.recv(4096)

# print(response.decode())
# client.close()

# # UDP客户端
# import socket
# target_host = "127.0.0.1"
# target_port = 9997

# client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client.sendto(b"AAABBBCCC",(target_host,target_port))
# data,addr = client.recvfrom(4096)

# print(data.decode())
# client.close()

# ## TCP多线程服务器
# import socket
# import threading

# IP = '0.0.0.0'
# PORT = 9998

# def main():
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     #设置监听地址
#     server.bind((IP, PORT))
#     #最大连接数设置为5
#     server.listen(5)
#     print(f'[*] Listening on {IP}:{PORT}')

#     while True:
#         #保存客户端socket对象及地址
#         client, address = server.accept()
#         print(f'[*] Accepted connection from {address[0]}:{address[1]}')
#         #创建新线程
#         client_handler = threading.Thread(target=handle_client, args=(client,))
#         client_handler.start()

# def handle_client(client_socket):
#     with client_socket as sock:
#         request = sock.recv(1024)
#         print(f'[*] Received:{request.decode("utf-8")}')
#         sock.send(b'ACK')

# if __name__ == '__main__':
#     main()


# # netcat
# import argparse
# import socket
# import shlex
# import subprocess
# import sys
# import textwrap
# import threading
#
#
# def execute(cmd):
#     # 去除字符串两侧的空白字符
#     cmd = cmd.strip()
#     if not cmd:
#         return
#     # shlex.split()解析命令字符串参数列表
#     # subprocess模块生成子进程
#     # subprocess.check_output运行命令并获取标准输出
#     output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
#     return output.decode
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(
#         description='BHP Net Tool',
#         formatter_class=argparse.RawDescriptionHelpFormatter,
#         epilog=textwrap.dedent('''Example:
#             netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
#             netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt #upload to file
#             netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
#             echo 'ABC' | ./etcat.py -t 192.168.1.108 -p 135 # echo text to server port 135
#             netcat.py -t 192.168.1.108 -p 5555 # connect to server
#         ''')
#     )
#     parser.add_argument('-c', '--command', action='store_true', help='command shell')
#     parser.add_argument('-e', '--execute', help='execute specified command')
#     parser.add_argument('-l', '--listen', action='store_true', help='listen')
#     parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
#     parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')
#     parser.add_argument('-u', '--upload', help='upload file')
#     args = parser.parse_args()
#     if args.listen:
#         buffer = ''
#     else:
#         buffer = sys.stdin.read()
#     nc = NetCat(args, buffer.encode())
#     nc.run()


# ##shelex
# import shlex

# # 解析简单的命令字符串
# command_string = "echo 'hello'"
# command_list = shlex.split(command_string)
# print(command_list)

# subprocess
import subprocess

try:
    # 运行命令并获取标准输出
    output = subprocess.check_output(["cd", "123"], shell=True, text=True)
    print(output)
except subprocess.CalledProcessError as e:
    print(f"命令执行失败：{e}")

# import argparse
#
# parser = argparse.ArgumentParser(description='命令行参数示例')
#
# # 添加位置参数
# parser.add_argument('input_file', help='输入文件的路径')
#
# # 添加可选参数
# parser.add_argument('-o', '--output_file', help='输出文件的路径', default='output.txt')
#
# # 解析命令行参数
# args = parser.parse_args()
#
# # 访问解析后的参数
# input_file = args.input_file
# output_file = args.output_file
#
# print(f'输入文件路径: {input_file}')
# print(f'输出文件路径: {output_file}')
#
# # 输入：python .\socket_test.py input.txt -o output.txt
# # 输出：
# # 输入文件路径: input.txt
# # 输出文件路径: output.txt
