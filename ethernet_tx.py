import socket

def send(data):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(data.encode(), ("127.0.0.1", 5000))
