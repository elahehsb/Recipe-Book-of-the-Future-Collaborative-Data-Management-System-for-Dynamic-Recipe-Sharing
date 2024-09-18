import hashlib
import time

class RecipeVersionControl:
    def __init__(self):
        self.recipe_versions = {}

    def create_recipe(self, recipe_id, user, recipe_details):
        """
        Create a new recipe with version control.
        """
        timestamp = time.time()
        recipe_hash = hashlib.sha256(str(recipe_details).encode()).hexdigest()
        
        self.recipe_versions[recipe_id] = [{
            'user': user,
            'timestamp': timestamp,
            'recipe_details': recipe_details,
            'recipe_hash': recipe_hash
        }]
    
    def modify_recipe(self, recipe_id, user, updated_recipe_details):
        """
        Modify an existing recipe and track changes with versioning.
        """
        timestamp = time.time()
        recipe_hash = hashlib.sha256(str(updated_recipe_details).encode()).hexdigest()
        
        version_entry = {
            'user': user,
            'timestamp': timestamp,
            'recipe_details': updated_recipe_details,
            'recipe_hash': recipe_hash
        }
        
        if recipe_id in self.recipe_versions:
            self.recipe_versions[recipe_id].append(version_entry)
        else:
            print(f"Recipe with ID {recipe_id} does not exist.")
    
    def get_recipe_history(self, recipe_id):
        """
        Get the version history of a recipe.
        """
        return self.recipe_versions.get(recipe_id, [])
