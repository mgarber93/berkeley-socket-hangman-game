import socket

host = socket.gethostname()
port = 8000

# since our game prompt is the largest message sent, and it has fixed size
# since the number of wrong guesses limits the size of the guesses set
# this messaging scheme will work for our purposes
# adapted from https://docs.python.org/3.4/howto/sockets.html

FIXED_MESSAGE_LENGTH = 512


class FixedLengthConnection:
    """Simplest solution which sends fixed length messages"""

    def __init__(self, connection):
        self.connection = connection

    def connect(self, connection_host, connection_port):
        """Connect on port on localhost"""
        self.connection.connect((connection_host, connection_port))

    def send(self, string):
        if len(string) < FIXED_MESSAGE_LENGTH:
            string = "{:<512}".format(string)

        data = string.encode()

        total_sent_character = 0
        while total_sent_character < FIXED_MESSAGE_LENGTH:
            sent = self.connection.send(data[total_sent_character:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            total_sent_character += sent

    def receive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < FIXED_MESSAGE_LENGTH:
            chunk = self.connection.recv(
                min(FIXED_MESSAGE_LENGTH - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        chunks = b''.join(chunks)
        return chunks.decode().rstrip()  # rstrip padded characters
