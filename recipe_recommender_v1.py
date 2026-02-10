# Recipe Recommender v1
# Uses Spoonacular API to recommend recipes based on user preferences

import requests
import random

from config import API_KEY
BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"


def show_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("🍳 RECIPE RECOMMENDER")
    print("=" * 50)
    print("1. Set preferences")
    print("2. Get recipe recommendations")
    print("3. View current preferences")
    print("4. Clear all preferences")
    print("5. View saved favorites")  
    print("6. Exit")  
    print("=" * 50)

def get_user_preferences(current_preferences=None):
    """Collect user's dietary and nutritional preferences"""
    if current_preferences is None:
        preferences = {}
    else:
        preferences = current_preferences.copy()  # Keep old preferences
    
    print("\n--- Set Your Preferences ---")
    print("(Press Enter to skip any preference)\n")
    
    print("📊 NUTRITIONAL PREFERENCES:")
    min_cal = input("Minimum calories: ").strip()
    if min_cal:
        preferences['minCalories'] = min_cal
    
    max_cal = input("Maximum calories: ").strip()
    if max_cal:
        preferences['maxCalories'] = max_cal
    
    min_carbs = input("Minimum carbs (g): ").strip()
    if min_carbs:
        preferences['minCarbs'] = min_carbs
    
    max_carbs = input("Maximum carbs (g): ").strip()
    if max_carbs:
        preferences['maxCarbs'] = max_carbs
    
    min_protein = input("Minimum protein (g): ").strip()
    if min_protein:
        preferences['minProtein'] = min_protein
    
    max_protein = input("Maximum protein (g): ").strip()
    if max_protein:
        preferences['maxProtein'] = max_protein
    
    min_fat = input("Minimum fat (g): ").strip()
    if min_fat:
        preferences['minFat'] = min_fat
    
    max_fat = input("Maximum fat (g): ").strip()
    if max_fat:
        preferences['maxFat'] = max_fat
    
    # Diet type
    print("\n🥗 DIET TYPE:")
    print("Options: vegetarian, vegan, ketogenic, paleo, gluten free, pescetarian")
    diet = input("Choose one diet type: ").strip().lower()
    if diet:
        preferences['diet'] = diet
    
    # Intolerances/Allergies (can be multiple)
    print("\n⚠️  INTOLERANCES/ALLERGIES:")
    print("Options: dairy, egg, gluten, grain, peanut, seafood, sesame, shellfish, soy, sulfite, tree nut, wheat")
    print("(You can enter multiple, separated by commas)")
    intolerances = input("Enter intolerances: ").strip()
    if intolerances:
        preferences['intolerances'] = intolerances
    
    # Include ingredients
    print("\n✅ INCLUDE INGREDIENTS:")
    print("(Enter ingredients separated by commas)")
    include_ingredients = input("Ingredients to include: ").strip()
    if include_ingredients:
        preferences['includeIngredients'] = include_ingredients
    
    # Exclude ingredients
    print("\n❌ EXCLUDE INGREDIENTS:")
    print("(Enter ingredients separated by commas)")
    exclude_ingredients = input("Ingredients to exclude: ").strip()
    if exclude_ingredients:
        preferences['excludeIngredients'] = exclude_ingredients
    
    # Recipe type (can be multiple)
    print("\n🍽️  RECIPE TYPE:")
    print("Options: main course, side dish, dessert, snack, breakfast, soup, salad, sauce, drink")
    print("(You can enter multiple, separated by commas)")
    recipe_type = input("Choose recipe type(s): ").strip().lower()
    if recipe_type:
        preferences['type'] = recipe_type
    
    # Cuisine
    print("\n🌍 CUISINE:")
    print("Options: african, asian, american, british, cajun, caribbean, chinese, european,")
    print("         french, german, greek, indian, irish, italian, japanese, korean,")
    print("         latin american, mediterranean, mexican, middle eastern, spanish, thai, vietnamese")
    cuisine = input("Choose cuisine: ").strip().lower()
    if cuisine:
        preferences['cuisine'] = cuisine
    
    # Cooking time
    print("\n⏱️  COOKING TIME:")
    max_time = input("Maximum cooking time (minutes): ").strip()
    if max_time:
        preferences['maxReadyTime'] = max_time
    
    print("\n✓ Preferences saved!")
    return preferences


def view_preferences(preferences):
    """Display current preferences"""
    if not preferences:
        print("\n📝 No preferences set. All recipes will be shown randomly.")
        return
    
    print("\n--- Current Preferences ---")
    
    # Nutritional info
    nutritional = []
    if 'minCalories' in preferences or 'maxCalories' in preferences:
        cal_range = f"{preferences.get('minCalories', '0')}-{preferences.get('maxCalories', '∞')} cal"
        nutritional.append(f"Calories: {cal_range}")
    
    if 'minCarbs' in preferences or 'maxCarbs' in preferences:
        carb_range = f"{preferences.get('minCarbs', '0')}-{preferences.get('maxCarbs', '∞')}g"
        nutritional.append(f"Carbs: {carb_range}")
    
    if 'minProtein' in preferences or 'maxProtein' in preferences:
        protein_range = f"{preferences.get('minProtein', '0')}-{preferences.get('maxProtein', '∞')}g"
        nutritional.append(f"Protein: {protein_range}")
    
    if 'minFat' in preferences or 'maxFat' in preferences:
        fat_range = f"{preferences.get('minFat', '0')}-{preferences.get('maxFat', '∞')}g"
        nutritional.append(f"Fat: {fat_range}")
    
    if nutritional:
        print(f"📊 Nutritional: {', '.join(nutritional)}")
    
    # Other preferences
    if 'diet' in preferences:
        print(f"🥗 Diet: {preferences['diet'].capitalize()}")
    
    if 'intolerances' in preferences:
        print(f"⚠️  Intolerances: {preferences['intolerances']}")
    
    if 'includeIngredients' in preferences:
        print(f"✅ Include: {preferences['includeIngredients']}")
    
    if 'excludeIngredients' in preferences:
        print(f"❌ Exclude: {preferences['excludeIngredients']}")
    
    if 'type' in preferences:
        print(f"🍽️  Type: {preferences['type'].capitalize()}")
    
    if 'cuisine' in preferences:
        print(f"🌍 Cuisine: {preferences['cuisine'].capitalize()}")
    
    if 'maxReadyTime' in preferences:
        print(f"⏱️  Max time: {preferences['maxReadyTime']} minutes")


def get_recipe_recommendations(preferences, number=10):
    """Fetch recipes from Spoonacular API based on preferences"""
    
    
    # Build API parameters
    params = {
        'apiKey': API_KEY,
        'number': number,
        'addRecipeInformation': True,
        'fillIngredients': True,
        'addRecipeNutrition': True,
        'sort': 'random'
    }
    
    # Add user preferences to params
    params.update(preferences)
    
    try:
        print("\n🔍 Searching for recipes...")
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        recipes = data.get('results', [])
        
        if not recipes:
            print("\n😔 No recipes found matching your preferences.")
            print("Try adjusting your filters!")
            return
        
        print(f"\n🎉 Found {len(recipes)} recipes!")
        print("\n" + "=" * 50)
        
        for i, recipe in enumerate(recipes, 1):
            print(f"\n{i}. {recipe['title']}")
            print(f"   ⏱️  Ready in: {recipe.get('readyInMinutes', 'N/A')} minutes")
            print(f"   👥 Servings: {recipe.get('servings', 'N/A')}")
            
            # Ingredients
            ingredients_list = recipe.get('extendedIngredients', [])
            if ingredients_list:
                print(f"   🛒 Ingredients:")
                for ingredient in ingredients_list:
                    amount = ingredient.get('amount', '')
                    unit = ingredient.get('unit', '')
                    name = ingredient.get('name', '')
                    
                    # Format the ingredient nicely
                    if amount and unit:
                        print(f"      • {amount} {unit} {name}")
                    elif amount:
                        print(f"      • {amount} {name}")
                    else:
                        print(f"      • {name}")
            
            # Nutritional info if available
            nutrition = recipe.get('nutrition', {})
            if nutrition and 'nutrients' in nutrition:
                nutrients = nutrition['nutrients']
                print(f"   📊 Nutrition:")
                
                # Always show calories first
                calories = next((n for n in nutrients if n['name'] == 'Calories'), None)
                if calories:
                    print(f"      • Calories per serving: {calories['amount']}{calories['unit']}")
                
                # Show other nutrients
                for nutrient in nutrients[:4]:  # Show top 4 nutrients
                    if nutrient['name'] != 'Calories':  # Skip calories since we already showed it
                        print(f"      • {nutrient['name']}: {nutrient['amount']}{nutrient['unit']}")
            
            print(f"   🔗 View recipe: {recipe.get('sourceUrl', 'N/A')}")
            print("   " + "-" * 45)
        
        save_choice = input("\n💾 Want to save any recipe? Enter number (or press Enter to skip): ").strip()

        
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Error fetching recipes: {e}")
        print("Please check your internet connection and API key.")

# After displaying all recipes, ask if user wants to save any
        save_choice = input("\n💾 Want to save any recipe? Enter number (or press Enter to skip): ").strip()
        if save_choice.isdigit():
            recipe_num = int(save_choice)
            if 1 <= recipe_num <= len(recipes):
                save_favorite_recipe(recipes[recipe_num - 1])
            else:
                print("❌ Invalid recipe number")


def save_favorite_recipe(recipe):
    """Save a recipe to favorites file"""
    try:
        # Create favorites file if it doesn't exist
        with open('favorite_recipes.txt', 'a', encoding='utf-8') as f:
            f.write("\n" + "=" * 60 + "\n")
            f.write(f"Recipe: {recipe['title']}\n")
            f.write(f"Ready in: {recipe.get('readyInMinutes', 'N/A')} minutes\n")
            f.write(f"Servings: {recipe.get('servings', 'N/A')}\n")
            f.write(f"URL: {recipe.get('sourceUrl', 'N/A')}\n")
            
            # Save ingredients
            ingredients_list = recipe.get('extendedIngredients', [])
            if ingredients_list:
                f.write("\nIngredients:\n")
                for ingredient in ingredients_list:
                    amount = ingredient.get('amount', '')
                    unit = ingredient.get('unit', '')
                    name = ingredient.get('name', '')
                    if amount and unit:
                        f.write(f"  - {amount} {unit} {name}\n")
                    elif amount:
                        f.write(f"  - {amount} {name}\n")
                    else:
                        f.write(f"  - {name}\n")
            
            f.write("=" * 60 + "\n")
        
        print("\n💾 Recipe saved to 'favorite_recipes.txt'!")
    
    except Exception as e:
        print(f"\n❌ Error saving recipe: {e}")

def view_saved_favorites():
    """Display saved favorite recipes"""
    try:
        with open('favorite_recipes.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            if content.strip():
                print("\n📚 Your Saved Favorites:")
                print(content)
            else:
                print("\n📚 No favorites saved yet!")
    except FileNotFoundError:
        print("\n📚 No favorites saved yet!")


def main():
    """Main program loop"""
    user_preferences = {}
    
    print("\n🍳 Welcome to Recipe Recommender!")
    print("Powered by Spoonacular API")
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            user_preferences = get_user_preferences(user_preferences)   
        
        elif choice == "2":
            get_recipe_recommendations(user_preferences)
        
        elif choice == "3":
            view_preferences(user_preferences)
        
        elif choice == "4":
            user_preferences = {}
            print("\n✓ All preferences cleared!")
        
        elif choice == "5":  # NEW
            view_saved_favorites()
        
        elif choice == "6":  # Changed from 5
            print("\n👋 Happy cooking! Goodbye!")
            break
        
        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()