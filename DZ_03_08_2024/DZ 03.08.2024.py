import sqlite3


def create_table():
    with sqlite3.connect('computers.db') as con:
        cursor = con.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Computers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                model TEXT NOT NULL,
                processor TEXT NOT NULL,
                ram TEXT NOT NULL,
                price REAL NOT NULL
            );
        ''')
        con.commit()


def add_computer(model, processor, ram, price):
    with sqlite3.connect('computers.db') as con:
        cursor = con.cursor()
        cursor.execute('''
            INSERT INTO Computers (model, processor, ram, price)
            VALUES (?, ?, ?, ?);
        ''', (model, processor, ram, price))
        con.commit()
        print(f"Компьютер {model} успешно добавлен.")


def show_computers():
    with sqlite3.connect('computers.db') as con:
        cursor = con.cursor()
        cursor.execute('SELECT * FROM Computers')
        rows = cursor.fetchall()
        for row in rows:
            print(row)

if __name__ == '__main__':
    create_table()
    while True:
        command = input('''
1. Добавить компьютер
2. Просмотреть компьютеры
0. Выйти из программы
Введите команду: ''')
        if command == '1':
            model = input("Введите модель компьютера: ")
            processor = input("Введите процессор компьютера: ")
            ram = input("Введите объем оперативной памяти (например, 8GB): ")
            price = float(input("Введите цену компьютера: "))
            add_computer(model, processor, ram, price)
        elif command == '2':
            show_computers()
        elif command == '0':
            break
        else:
            print("Неверная команда. Пожалуйста, выберите один из предложенных вариантов.")
