# 1.
# class Command:
#     def execute(self):
#         pass
#
# class InsertTextCommand(Command):
#     def __init__(self, editor, text):
#         self.editor = editor
#         self.text = text
#
#     def execute(self):
#         self.editor.insert_text(self.text)
#
#
# class DeleteTextCommand(Command):
#     def __init__(self, editor, start, end):
#         self.editor = editor
#         self.start = start
#         self.end = end
#
#     def execute(self):
#         self.editor.delete_text(self.start, self.end)
#
# class Editor:
#     def __init__(self):
#         self.text = ""
#
#     def insert_text(self, text):
#         self.text += text
#
#     def delete_text(self, start, end):
#         self.text = self.text[:start] + self.text[end:]
#
#
# class TextEditor:
#     def __init__(self):
#         self.commands = []
#
#     def add_command(self, command):
#         self.commands.append(command)
#
#     def execute_commands(self):
#         for command in self.commands:
#             command.execute()
#
#
# editor = Editor()
#
#
# insert_command = InsertTextCommand(editor, "Hello, world")
# delete_command = DeleteTextCommand(editor, 7, 13)
#
#
# text_editor = TextEditor()
# text_editor.add_command(insert_command)
# text_editor.add_command(delete_command)
#
#
# text_editor.execute_commands()
#
#
# print(editor.text)


# 2.
# import time
# import logging
#
# class RealSubject:
#     def __init__(self, filename):
#         self.filename = filename
#         self.data = self.load_data()
#
#     def load_data(self):
#         with open(self.filename, 'r') as f:
#             return [float(line.strip()) for line in f]
#
#     def sum(self):
#         return sum(self.data)
#
#     def max(self):
#         return max(self.data)
#
#     def min(self):
#         return min(self.data)
#
# class Proxy(RealSubject):
#     def __init__(self, filename):
#         super().__init__(filename)
#         self.logger = logging.getLogger(__name__)
#
#     def log(self, operation, result):
#         self.logger.info(f'Operation: {operation}, Result: {result}')
#
#     def sum(self):
#         result = super().sum()
#         self.log('sum', result)
#         return result
#
#     def max(self):
#         result = super().max()
#         self.log('max', result)
#         return result
#
#     def min(self):
#         result = super().min()
#         self.log('min', result)
#         return result
#
# if __name__ == '__main__':
#     filename = 'data.txt'
#     proxy = Proxy(filename)
#
#     while True:
#         operation = input('Enter operation (sum, max, min): ')
#         if operation in ['sum', 'max', 'min']:
#             result = getattr(proxy, operation)()
#             print(f'Result: {result}')
#         else:
#             print('Invalid operation')
#
#
#         time.sleep(5)
#         proxy.data = proxy.load_data()

# 3,
# from abc import ABC, abstractmethod
# from typing import List
#
#
# class Repository(ABC):
#     @abstractmethod
#     def find_all(self):
#         pass
#
#     @abstractmethod
#     def find_by_id(self, id):
#         pass
#
#     @abstractmethod
#     def save(self, entity):
#         pass
#
#     @abstractmethod
#     def delete(self, entity):
#         pass
#
#
#
# class Singleton(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]
#
#
#
# class FactoryMethod:
#     @staticmethod
#     def create(entity_type):
#         if entity_type == 'book':
#             return Book()
#         elif entity_type == 'librarian':
#             return Librarian()
#         elif entity_type == 'reader':
#             return Reader()
#         else:
#             raise ValueError(f'Invalid entity type: {entity_type}')
#
#
#
# class Entity:
#     def __init__(self, id):
#         self.id = id
#
#
#
# class Book(Entity):
#     def __init__(self, id, title, author):
#         super().__init__(id)
#         self.title = title
#         self.author = author
#
#
#
# class Librarian(Entity):
#     def __init__(self, id, name):
#         super().__init__(id)
#         self.name = name
#
#
#
# class Reader(Entity):
#     def __init__(self, id, name):
#         super().__init__(id)
#         self.name = name
#
#
#
# class BookRepository(Repository):
#     def __init__(self):
#         self._books = {}
#
#     def find_all(self):
#         return list(self._books.values())
#
#     def find_by_id(self, id):
#         return self._books.get(id)
#
#     def find_by_title(self, title):
#         for book in self._books.values():
#             if book.title == title:
#                 return book
#         return None
#
#
#
# from book_repository import BookRepository
#
#
# book_repository = BookRepository()
#
#
# book1 = Book(1, "Война и мир", "Лев Толстой")
# book2 = Book(2, "Преступление и наказание", "Федор Достоевский")
#
#
# book_repository.save(book1)
# book_repository.save(book2)
#
#
# books = book_repository.find_by_title("Война и мир")
# if books is not None:
#     print(f"Книга: {books.title} ({books.author})")