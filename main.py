from recipes.recipe_version_control import RecipeVersionControl
from recipes.recipe_query_system import RecipeQuerySystem
from recipes.recipe_recommendation import RecipeRecommendationSystem
from user_management.user_activity_tracking import UserActivityTracker
from user_management.privacy_settings import PrivacySettings

def main():
    # Initialize components
    recipe_control = RecipeVersionControl()
    user_activity = UserActivityTracker()
    privacy_settings = PrivacySettings()

    # Create initial recipes
    recipe1 = {
        'name': 'Spaghetti Carbonara',
        'ingredients': ['spaghetti', 'egg', 'bacon', 'parmesan'],
        'cooking_time': 30,
        'dietary_info': ['non-vegetarian'],
        'tags': ['Italian', 'Pasta']
    }

    recipe2 = {
        'name': 'Vegan Tacos',
        'ingredients': ['tortilla', 'black beans', 'avocado', 'salsa'],
        'cooking_time': 20,
        'dietary_info': ['vegan'],
        'tags': ['Mexican', 'Quick']
    }

    # Add recipe versions
    recipe_control.create_recipe('1', 'User1', recipe1)
    recipe_control.create_recipe('2', 'User2', recipe2)

    # Query recipes by ingredient
    query_system = RecipeQuerySystem([recipe1, recipe2])
    result = query_system.search_by_ingredient('spaghetti')
    print("Recipes with spaghetti:", result)

    # Log user activity
    user_activity.log_activity('User1', 'create_recipe', 'Spaghetti Carbonara')
    print("User activity for User1:", user_activity.get_user_activity('User1'))

    # Recommend recipes for a user
    user_profiles = {'User1': {'preferences': ['Italian', 'Vegan']}}
    recommendation_system = RecipeRecommendationSystem(user_profiles, [recipe1, recipe2])
    recommendations = recommendation_system.recommend_recipes('User1')
    print("Recommended recipes for User1:", recommendations)

if __name__ == "__main__":
    main()
