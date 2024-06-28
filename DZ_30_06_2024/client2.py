import socket

def receive_file(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Ожидание файлов...")
        conn, addr = s.accept()
        with conn:
            filename = conn.recv(1024).decode()
            print(f"Получено уведомление о файле: {filename}")
            # Запрос подтверждения у пользователя
            user_confirmation = input(f"Принять файл {filename}? (да/нет): ").lower()
            if user_confirmation == "да":
                conn.sendall("READY".encode())
                new_filename = input("Введите новое имя файла для сохранения или нажмите Enter, чтобы сохранить как есть: ")
                new_filename = new_filename or filename
                with open(new_filename, 'wb') as f:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        f.write(data)
                print(f"Файл {new_filename} успешно сохранен.")
            else:
                conn.sendall("CANCEL".encode())
                print("Получение файла отменено.")

if __name__ == "__main__":
    host = 'localhost'  # IP-адрес сервера
    port = 65432        # Порт, который использует сервер
    receive_file(host, port)
