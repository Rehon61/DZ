# class BookRepository:
#     def __init__(self):
#         self._books = {}
#
#     def find_all(self):
#         return list(self._books.values())
#
#     def find_by_id(self, id):
#         return self._books.get(id)
#
#     def save(self, book):
#         self._books[book.id] = book
#
#     def delete(self, book):
#         del self._books[book.id]
#
#     def find_by_title(self, title):
#         for book in self._books.values():
#              if book.title == title:
#                  return book
#         return None