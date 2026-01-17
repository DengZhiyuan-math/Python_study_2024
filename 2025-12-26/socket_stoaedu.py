import socket
import ssl

host = 'badi-info.ch'
port = 443

# 1. 创建 TCP socket
raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 用 TLS 包一层（关键）
context = ssl.create_default_context()
mysock = context.wrap_socket(raw_sock, server_hostname=host)

# 3. 连接 HTTPS 端口
mysock.connect((host, port))

# 4. 发送合法的 HTTP/1.1 请求
cmd = (
    'GET / HTTP/1.1\r\n'
    f'Host: {host}\r\n'
    'Connection: close\r\n'
    '\r\n'
)
mysock.send(cmd.encode())

# 5. 接收响应
while True:
    try:
        data = mysock.recv(512)
        if not data:
            break
        print(data.decode(errors='ignore'), end='')
    except ConnectionResetError:
        break

mysock.close()

