import socket
from common import host, port

MAX_CONNECTIONS = 1


def server():
    """Create a server"""

    with socket.socket() as server_socket:
        server_socket.bind((host, port))
        print(f"Listening on: {host} on port: {port}")
        server_socket.listen(MAX_CONNECTIONS)
        client_connection, address = server_socket.accept()
        print(f"Connection by: ({client_connection}, {address})")

        while True:
            print("Waiting for message...")
            data = client_connection.recv(1024).decode()
            if not data:
                break
            print(str(data))

            message = input('Enter message to send...\n>')
            client_connection.send(message.encode())


if __name__ == '__main__':
    server()
