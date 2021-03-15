import socket
from common import host, port


def client():
    """Create a client"""
    client_socket = socket.socket()
    client_socket.connect((host, port))
    print(f"Connected to: ({host}, {port})")

    message = input('Enter message to send...\n>')

    while message != '/q':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(data)
        message = input('Enter message to send...\n>')

    client_socket.close()


if __name__ == '__main__':
    client()
