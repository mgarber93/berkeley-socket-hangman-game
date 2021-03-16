import socket
from common import host, port


def read_and_print(connection):
    """Read from connection and print as utf-8"""
    data = connection.recv(1024).decode()
    print(data)


PROMPT = 'Guess a letter...\n>'


def client():
    """Create a client"""
    with socket.socket() as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to: ({host}, {port})")
        read_and_print(client_socket)
        message = input(PROMPT)

        while message != '/q':
            client_socket.send(message.encode())
            read_and_print(client_socket)
            message = input(PROMPT)


if __name__ == '__main__':
    client()
