import socket

# Конфигурация клиента
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'  # Или IP-адрес сервера, если он запущен на другом компьютере
port = 12345  # Убедитесь, что порт соответствует порту сервера

try:
    client.connect((host, port))
except ConnectionRefusedError:
    print("Не удалось подключиться к серверу. Проверьте, что сервер запущен и доступен.")
    exit(1)

def main():
    while True:
        try:
            # Получение сообщения от сервера
            message = client.recv(1024).decode('utf-8')
        except Exception as e:
            print(f"Произошла ошибка при получении данных: {e}")
            continue

        if "WELCOME" in message:
            print("Добро пожаловать в игру крестики-нолики!")
        elif "GAME" in message:
            print(message)
        elif "YOUR MOVE" in message:
            print("Ваш ход. Введите координаты (например, '1 1'): ")
            move = input()
            client.send(move.encode('utf-8'))
        elif "INVALID MOVE" in message:
            print("Некорректный ход. Попробуйте снова.")
        elif "VICTORY" in message:
            print("Поздравляем! Вы выиграли!")
            break
        elif "DEFEAT" in message:
            print("К сожалению, вы проиграли.")
            break
        elif "DRAW" in message:
            print("Игра закончилась вничью.")
            break
        elif "Неизвестная команда" in message:
            pass  # Просто игнорируем и не выводим ничего
        else:
            print(f"Получено сообщение: {message}")

if __name__ == "__main__":
    main()
