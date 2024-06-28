import socket
import threading

# Инициализация игрового поля
game_board = [" " for _ in range(9)]
players = {}
player_turn = 1
game_active = True
lock = threading.Lock()

# Функция для вывода игрового поля в консоль
def print_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

# Функция для проверки победителя
def check_winner(board, mark):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == mark:
            return True
    return False

# Функция для отправки сообщений всем клиентам
def broadcast(message):
    for player_conn in players.values():
        player_conn.sendall(message.encode())

# Функция потока клиента
def client_thread(conn, player):
    global game_board, player_turn, game_active
    conn.sendall(f"PLAYER {player}".encode())
    try:
        while game_active:
            with lock:
                if player == player_turn:
                    conn.sendall("YOUR MOVE".encode())
                    data = conn.recv(1024).decode()
                    move = int(data) - 1
                    if 0 <= move < 9 and game_board[move] == " ":
                        game_board[move] = "X" if player == 1 else "O"
                        print_board(game_board)
                        broadcast(f"MOVE {move + 1} by PLAYER {player}")
                        if check_winner(game_board, game_board[move]):
                            broadcast("WIN")
                            game_active = False
                        player_turn = 2 if player == 1 else 1
                    else:
                        conn.sendall("INVALID MOVE".encode())
                else:
                    conn.sendall("WAIT".encode())
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        conn.close()

# Настройка сервера
def setup_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen(2)
    print("Сервер игры запущен и ожидает подключения игроков...")
    while len(players) < 2:
        conn, addr = server.accept()
        print(f"Подключение от {addr}")
        player_id = len(players) + 1
        players[player_id] = conn
        threading.Thread(target=client_thread, args=(conn, player_id)).start()

# Запуск сервера
if __name__ == "__main__":
    setup_server()
