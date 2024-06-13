# 1.
# class Shoe:
#     def __init__(self, shoe_type, shoe_style, color, price, manufacturer, size):
#        self.shoe_type = shoe_type
#        self.shoe_style = shoe_style
#        self.color = color
#        self.price = price
#        self.manufacturer = manufacturer
#        self.size = size
#
#
#
# class ShoeController:
#     def __init__(self):
#         pass
#
#     def create_shoe(self, shoe_type, shoe_style, color, price, manufacturer, size):
#         return Shoe(shoe_type, shoe_style, color, price, manufacturer, size)
#
# class ShoeView:
#     def shoe_details(self, shoe):
#         print("Shoe Type: {}".format(shoe.shoe_type))
#         print("Shoe Style: {}".format(shoe.shoe_style))
#         print("Shoe Color: {}".format(shoe.color))
#         print("Shoe Price: {}".format(shoe.price))
#         print("Shoe Manufacturer: {}".format(shoe.manufacturer))
#         print("Shoe Size: {}".format(shoe.size))
#
#
#
#
# class ShoeModel:
#     def __init__(self):
#         self.shoe = None
#
#
#     def set_shoe(self, shoe):
#         self.shoe = shoe
#
#
#     def get_shoe(self):
#         return self.shoe
#
#
# if __name__ == "__main__":
#     shoe_controller = ShoeController()
#     shoe_model = ShoeModel()
#     shoe_view = ShoeView()
#
#
#     shoe = shoe_controller.create_shoe("men", "sneakers", "black", "50", "Nike", 42)
#     shoe_model.set_shoe(shoe)
#
#
#     shoe_details = shoe_model.get_shoe()
#     shoe_view.shoe_details(shoe_details)


# 2.
# class Recipe:
#     def __init__(self, name, author, recipe_type, description, video_link, ingredients, cuisine):
#         self.name = name
#         self.author = author
#         self.recipe_type = recipe_type
#         self.description = description
#         self.video_link = video_link
#         self.ingredients = ingredients
#         self.cuisine = cuisine
#
#     def get_info(self):
#         return f"Recipe: {self.name}\nAuthor: {self.author}\nType: {self.recipe_type}\nDescription: {self.description}\nVideo Link: {self.video_link}\nIngredients: {', '.join(self.ingredients)}\nCuisine: {self.cuisine}"
#
# class RecipeController:
#     def create_recipe(self, name, author, recipe_type, description, video_link, ingredients, cuisine):
#         recipe = Recipe(name, author, recipe_type, description, video_link, ingredients, cuisine)
#         return recipe
#
#
# class RecioeView:
#     def show_recipe(self, recipe):
#         print(recipe.get_info())
#
#
# controller = RecipeController()
# view = RecioeView()
#
# recipe_data = {
#     "name": "Плов",
#     "author": "Обломов",
#     "recipe_type": "Основное блюдо",
#     "description": "блюдо восточной кухни, основу которого составляет варёный рис",
#     "video_link": "https://www.youtube.com/watch?v=6ND8Yuiyv7A",
#     "ingredients": ["Курица", "Рис", "Белый лук", "Морковь", "Лавровый лист", "Томатная паста"],
#     "cuisine": "Абхазия",
#
# }
#
# recipe = controller.create_recipe(**recipe_data)
#
# view.show_recipe(recipe)
