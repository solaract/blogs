# python黑帽子：黑客与渗透测试编程之道

@import "[TOC]" {cmd="toc" depthFrom=2 depthTo=3 orderedList=false}

<!-- code_chunk_output -->

- [一、环境安装配置](#一-环境安装配置)
- [二、基础网络编工具](#二-基础网络编工具)

<!-- /code_chunk_output -->


## 一、环境安装配置
1. 安装kali虚拟机
2. 更新kali系统
    ```shell {.line-numbers}
    sudo apt update
    apt list --upgradable
    sudo apt upgrade
    sudo apt dist-upgrade
    sudo apt autoremove
    ```
3. 配置python环境
   ```shell {.line-numbers}
   python
   #升级python版本
   sudo apt-get upgrade python
   ```
4. 创建python虚拟环境
   ```shell {.line-numbers}
   mkdir bhp
   cd bhp
   #-m调用venv包，创建虚拟环境venv3
   python -m venv venv3
   #激活虚拟环境
   source venv3/bin/activate
   #退出虚拟环境
   deactivate
   ```

## 二、基础网络编工具
1. TCP客户端：
   ```py {.line-numbers}
   import socket

   target_host = 'www.baidu.com'
   target_port = 80
    
   #AF_INET：使用标准IPv4地址或主机名
   #SOCK_STREAM：TCP客户端
   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   client.connect((target_host,target_port))
   client.send(b"GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n")
   response = client.recv(4096)
   print(response.decode())
   client.close()
   ```
2. UDP客户端：
   ```py {.line-numbers}
   import socket
   target_host = "127.0.0.1"
   target_port = 9997

   client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   client.sendto(b"AAABBBCCC",(target_host,target_port))
   data,addr = client.recvfrom(4096)

   print(data.decode())
   client.close()
   ```
3. TCP多线程服务端
   ```py {.line-numbers}
   import socket
   import threading

   IP = '0.0.0.0'
   PORT = 9998

   def main():
      server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      #设置监听地址
      server.bind((IP, PORT))
      #最大连接数设置为5
      server.listen(5)
      print(f'[*] Listening on {IP}:{PORT}')

      while True:
         #保存客户端socket对象及地址
         client, address = server.accept()
         print(f'[*] Accepted connection from {address[0]}:{address[1]}')
         #创建新线程
         client_handler = threading.Thread(target=handle_client, args=(client,))
         client_handler.start()

   def handle_client(client_socket):
      with client_socket as sock:
         request = sock.recv(1024)
         print(f'[*] Received:{request.decode("utf-8")}')
         sock.send(b'ACK')

   if __name__ == '__main__':
      main()
   ```
4. netcat
   ```py {.line-numbers}
   import argparse
   import socket
   import shlex
   import subprocess
   import sys
   import textwrap
   import threading

   def execute(cmd):
      #去除字符串两侧空白字符串
      cmd = cmd.strip()
      if not cmd:
         return
      #shlex.split()解析命令字符串参数列表
      #subprocess模块生成子进程
      #subprocess.check_output运行命令并获取标准输出
      output = subprocess.check_output(shlex.split(cmd),stderr=subprocess.STDOUT)
      return output.decode
   ```
   - shlex 模块是 Python 中用于解析 shell 命令字符串的模块。它提供了一个 shlex 类，该类允许你将命令字符串解析为适用于 subprocess 模块等的参数列表。
      ```py {.line-numbers}
      import shlex

      # 解析简单的命令字符串
      command_string = "echo 'hello'"
      command_list = shlex.split(command_string)
      print(command_list)
      #['echo', 'hello']
      ```
   - subprocess.check_output 是 subprocess 模块提供的一个函数，用于运行命令并获取其标准输出。与 subprocess.run 不同，check_output 函数会直接返回命令的标准输出，而不是一个包含各种信息的 CompletedProcess 对象。
      ```py {.line-numbers}
      ##subprocess
      import subprocess

      try:
         # 运行命令并获取标准输出
         output = subprocess.check_output(["cd", "123"], shell=True, text=True)
         print(output)
      except subprocess.CalledProcessError as e:
         print(f"命令执行失败：{e}")

      ```