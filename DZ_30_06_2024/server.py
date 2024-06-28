import socket
import os

# Функция для отправки файла
def send_file(conn, filename, client_sender):
    with open(filename, 'rb') as file:
        conn.sendfile(file, 0)
    print("Файл успешно отправлен.")
    client_sender.send("Файл успешно доставлен получателю.".encode())

# Настройка сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))
server_socket.listen()

print(f"Сервер запущен и ожидает подключения на {host}:{port}")

while True:
    conn, addr = server_socket.accept()
    print(f"Подключен клиент: {addr}")

    # Получение имени файла
    filename = conn.recv(1024).decode()
    print(f"Запрошен файл: {filename}")

    # Проверка существования файла
    if not os.path.isfile(filename):
        conn.send("Файл не найден.".encode())
        conn.close()
        continue

    # Ожидание подтверждения от получателя
    conn.send("Готов к передаче файла. Отправьте 'yes' для подтверждения.".encode())
    confirmation = conn.recv(1024).decode()

    if confirmation.lower() == 'yes':
        send_file(conn, filename)
        conn.send("Отправка файла завершена.".encode())
    else:
        conn.send("Передача файла отменена.".encode())

    conn.close()
