import socket

def send_file(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        filename = input("Введите имя файла для отправки: ")
        s.sendall(filename.encode())

        confirmation = s.recv(1024).decode()
        if confirmation == "READY":
            print("Отправка файла...")
            with open(filename, 'rb') as f:
                s.sendall(f.read())
            print("Файл отправлен.")
        else:
            print("Отправка отменена.")

if __name__ == "__main__":
    host = 'localhost'
    port = 65432
    send_file(host, port)
