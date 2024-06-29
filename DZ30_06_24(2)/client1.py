import socket

class TicTacToeClient:
    def __init__(self, address, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((address, port))

    def send_move(self, move):
        self.client.sendall(str(move).encode('utf-8'))

    def receive_response(self):
        return self.client.recv(1024).decode('utf-8')

client = TicTacToeClient('localhost', 5555)

game_over = False
while not game_over:
    move = input("Введите номер клетки (0-8) или 'q' для выхода: ")
    if move == 'q':
        game_over = True
    else:
        client.send_move(move)
        response = client.receive_response()
        print(response)

client.client.close()
