class RecipeRecommendationSystem:
    def __init__(self, user_profiles, recipe_database):
        self.user_profiles = user_profiles
        self.recipe_db = recipe_database
    
    def recommend_recipes(self, user_id):
        """
        Recommend recipes based on user preferences and past activities.
        """
        user_preferences = self.user_profiles.get(user_id, {}).get('preferences', [])
        recommended_recipes = []
        
        for recipe in self.recipe_db:
            if any(preference in recipe['tags'] for preference in user_preferences):
                recommended_recipes.append(recipe)
        
        return recommended_recipes
