import random
from socket import socket, SOL_SOCKET, SO_REUSEADDR
from hangman import HangManGame
from common import host, port, FixedLengthConnection

MAX_CONNECTIONS = 1

with open("words.txt") as words_file:
    content = words_file.read().splitlines()


def server():
    """Create a server"""
    with socket() as server_socket:
        server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        print(f"Listening on: {host} on port: {port}")
        server_socket.listen(MAX_CONNECTIONS)
        client_connection, address = server_socket.accept()
        connection = FixedLengthConnection(client_connection)
        print(f"Connection by: ({client_connection}, {address})")

        random_word = random.choice(content)
        print(f"starting hangman game with: {random_word}")
        game = HangManGame(random_word)

        while not game.is_game_over():
            connection.send(game.prompt())
            data = connection.receive()
            letter = str(data)
            if not game.is_valid_guess(letter):
                connection.send(f'Invalid letter {letter}!')
            else:
                game.guess(letter)

        if game.has_found_all_letters():
            final_message = 'You win!'
        else:
            final_message = 'You lose!'

        connection.send(final_message)


if __name__ == '__main__':
    server()
