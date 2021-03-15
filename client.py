import socket
from common import host, port


def client():
    """Create a client"""
    with socket.socket() as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to: ({host}, {port})")

        message = input('Enter message to send...\n>')

        while message != '/q':
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()
            print(data)
            message = input('Enter message to send...\n>')


if __name__ == '__main__':
    client()
