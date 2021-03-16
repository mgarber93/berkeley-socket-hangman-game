from socket import socket
from common import host, port, FixedLengthConnection


def read_and_print(connection):
    """Read from connection and print as utf-8"""
    data = connection.receive()
    print(data)
    return data


PROMPT = 'Guess a letter...\n>'


def client():
    """Create a game client"""
    with socket() as client_socket:
        client_socket.connect((host, port))
        connection = FixedLengthConnection(client_socket)
        print(f"Connected to: ({host}, {port})")
        message = ''

        while message != '/q':
            response = read_and_print(connection)
            if response == 'You win!' or response == 'You lose!':
                return
            message = input(PROMPT)
            connection.send(message)


if __name__ == '__main__':
    client()
