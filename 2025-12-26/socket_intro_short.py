import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET /data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    try:
        data = mysock.recv(512)
        if not data:
            break
        print(data.decode(), end='')
    except ConnectionResetError:
        break
mysock.close()