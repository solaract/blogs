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
   