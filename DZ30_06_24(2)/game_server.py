# import socket
# import threading
#
# class TicTacToeGame:
#     def __init__(self):
#         self.board = [' ' for _ in range(9)]
#         self.current_winner = None
#
#     def print_board(self):
#         for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
#             print('| ' + ' | '.join(row) + ' |')
#
#     def available_moves(self):
#         return [i for i, spot in enumerate(self.board) if spot == ' ']
#
#     def make_move(self, square, letter):
#         if self.board[square] == ' ':
#             self.board[square] = letter
#             if self.check_winner(square, letter):
#                 self.current_winner = letter
#             return True
#         return False
#
#     def check_winner(self, square, letter):
#         row_ind = square // 3
#         row = self.board[row_ind*3:(row_ind+1)*3]
#         if all([spot == letter for spot in row]):
#             return True
#         col_ind = square % 3
#         column = [self.board[col_ind+i*3] for i in range(3)]
#         if all([spot == letter for spot in column]):
#             return True
#         if square % 2 == 0:
#             diagonal1 = [self.board[i] for i in [0, 4, 8]]
#             if all([spot == letter for spot in diagonal1]):
#                 return True
#             diagonal2 = [self.board[i] for i in [2, 4, 6]]
#             if all([spot == letter for spot in diagonal2]):
#                 return True
#         return False
#
# def handle_client(conn, addr, game, opponent_conn):
#     connected = True
#     while connected:
#         try:
#             move = conn.recv(1024).decode('utf-8')
#             if move == 'q':
#                 connected = False
#                 opponent_conn.sendall(f"Player {addr} has quit the game. You win!".encode('utf-8'))
#             else:
#                 square = int(move)
#                 letter = 'X' if addr == player1_addr else 'O'
#                 if game.make_move(square, letter):
#                     game.print_board()
#                     if game.current_winner:
#                         conn.sendall("You win! Game over.".encode('utf-8'))
#                         opponent_conn.sendall(f"Player {letter} wins! Game over.".encode('utf-8'))
#                         connected = False
#                         server.sendall("Game over. The server will now close.".encode('utf-8'))
#                         server.close()
#                     else:
#                         opponent_conn.sendall(f"Player {letter} made a move to square {square}".encode('utf-8'))
#                 else:
#                     conn.sendall("Invalid move. Try again.".encode('utf-8'))
#         except ConnectionAbortedError:
#             print(f"Соединение с {addr} было неожиданно прервано.")
#             connected = False
#         except Exception as e:
#             print(f"Произошла ошибка: {e}")
#             connected = False
#
#     conn.close()
#     if opponent_conn:
#         opponent_conn.close()
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('localhost', 5555))
# server.listen()
#
# game = TicTacToeGame()
# player1_conn, player1_addr = server.accept()
# player2_conn, player2_addr = server.accept()
#
# player1_thread = threading.Thread(target=handle_client, args=(player1_conn, player1_addr, game, player2_conn))
# player2_thread = threading.Thread(target=handle_client, args=(player2_conn, player2_addr, game, player1_conn))
# player1_thread.start()
# player2_thread.start()
#
# player1_thread.join()
# player2_thread.join()
#
# server.close()
#
