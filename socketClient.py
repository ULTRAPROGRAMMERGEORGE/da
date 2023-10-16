import socket
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 3030))
    s.sendall('Help me!'.encode('utf-8'))
    data = s.recv(1024)
    s.close()
