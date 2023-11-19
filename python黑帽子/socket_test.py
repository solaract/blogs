
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

## TCP多线程客户端
import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #设置监听地址
    server.bind(IP, PORT)
    #最大连接数设置为5
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received:{request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()





