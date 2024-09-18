class RecipeQuerySystem:
    def __init__(self, recipe_database):
        self.recipe_db = recipe_database
    
    def search_by_ingredient(self, ingredient):
        """
        Search for recipes that contain a specific ingredient.
        """
        return [recipe for recipe in self.recipe_db if ingredient in recipe['ingredients']]
    
    def search_by_cooking_time(self, max_time):
        """
        Search for recipes that can be prepared within a certain time frame.
        """
        return [recipe for recipe in self.recipe_db if recipe['cooking_time'] <= max_time]
    
    def search_by_dietary_restrictions(self, restriction):
        """
        Search for recipes based on dietary restrictions (e.g., vegan, gluten-free).
        """
        return [recipe for recipe in self.recipe_db if restriction in recipe['dietary_info']]
