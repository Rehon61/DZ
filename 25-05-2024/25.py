# 1.

# class PastaBuilder:
#     def __init__(self):
#         self.pasta = Pasta()
#
#     def with_type(self, pasta_type):
#         self.pasta.type = pasta_type
#         return self
#
#     def with_sauce(self, sauce):
#         self.pasta.sauce = sauce
#         return self
#
#     def with_filling(self, filling):
#         self.pasta.filling.append(filling)
#         return self
#
#     def with_topping(self, topping):
#         self.pasta.toppings.append(topping)
#         return self
#
#     def build(self):
#         return self.pasta
#
#
# class Pasta:
#     def __init__(self):
#         self.type = None
#         self.sauce = None
#         self.filling = []
#         self.toppings = []
#
#     def __str__(self):
#         return f"Паста: {self.type}, соус: {self.sauce}, начинка: {', '.join(self.filling)}, добавки: {', '.join(self.toppings)}"
#
#
#
# builder = PastaBuilder()
#
# spaghetti_with_tomato_sauce = builder \
#     .with_type("спагетти") \
#     .with_sauce("томатный") \
#     .with_topping("пармезан") \
#     .build()
#
# print(spaghetti_with_tomato_sauce)
#
# lasagna_with_meat_filling = builder \
#     .with_type("лазанья") \
#     .with_filling("мясо") \
#     .with_sauce("альфредо") \
#     .with_topping("моцарелла") \
#     .with_topping("базилик") \
#     .build()
#
# print(lasagna_with_meat_filling)


# # 3.
# import copy
#
# class Document:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#     def clone(self):
#
#         return copy.deepcopy(self)
#
#
#
# original_document = Document("Мой документ", "Это содержимое моего документа.")
#
#
# cloned_document = original_document.clone()
#
#
# cloned_document.title = "Клонированный документ"
# cloned_document.content += " Это дополнительный контент."
#
#
# print(original_document.title)
# print(original_document.content)
# print(cloned_document.title)
# print(cloned_document.content)