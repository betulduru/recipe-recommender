# Recipe Recommender v1

A Python-based recipe recommendation system that uses the Spoonacular API to suggest recipes based on your dietary preferences, nutritional goals, and ingredient choices.

## Features

### Preference Filters:
- **Nutritional Goals**: Set min/max for calories, carbs, protein, and fat
- **Diet Type**: Choose one diet (vegetarian, vegan, keto, paleo, gluten-free, etc.)
- **Intolerances/Allergies**: Filter out multiple allergens (dairy, nuts, gluten, etc.)
- **Ingredients**: Include or exclude specific ingredients
- **Recipe Type**: Main course, side dish, dessert, snack, breakfast, soup, salad, sauce, drink
- **Cuisine**: Choose from 20+ cuisines (Italian, Mexican, Asian, etc.)
- **Random Mode**: If no preferences set, shows random recipes each time

## Setup Instructions

### 1. Get Spoonacular API Key
1. Go to https://spoonacular.com/food-api
2. Sign up for a free account
3. Get your API key (free tier: 150 requests/day)

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install requests
```

### 3. Add Your API Key
Open `recipe_recommender.py` and replace this line:
```python
API_KEY = "YOUR_API_KEY_HERE"
```

With your actual API key:
```python
API_KEY = "your_actual_api_key_here"
```

### 4. Run the Program
```bash
python recipe_recommender.py
```

## How to Use

1. **Set Preferences** (Option 1)
   - Set your nutritional goals, dietary restrictions, etc.
   - Press Enter to skip any preference you don't care about
   - You can choose multiple intolerances/allergies

2. **Get Recommendations** (Option 2)
   - View 10 recipes matching your preferences
   - If no preferences set, shows random recipes

3. **View Current Preferences** (Option 3)
   - See what filters are currently active

4. **Clear Preferences** (Option 4)
   - Remove all filters and start fresh

## Example Usage

### Example 1: High Protein, Low Carb
```
Minimum protein (g): 30
Maximum carbs (g): 20
Diet type: ketogenic
```

### Example 2: Vegetarian with Allergies
```
Diet type: vegetarian
Intolerances: dairy, gluten
Recipe type: main course
```

### Example 3: Include/Exclude Ingredients
```
Include ingredients: chicken, tomato
Exclude ingredients: onion, garlic
Cuisine: italian
```

## Spoonacular API Limits

- **Free tier**: 150 requests per day
- Each recommendation search = 1 request
- Monitor your usage at: https://spoonacular.com/food-api/console

## Future Improvements (v2+)

- Save favorite recipes
- Meal planning features
- Shopping list generator
- Recipe rating system
- Export recipes to PDF

## Troubleshooting

**Error: "Please set your Spoonacular API key"**
- Make sure you replaced `YOUR_API_KEY_HERE` with your actual API key

**Error: "No recipes found"**
- Your preferences might be too restrictive
- Try removing some filters

**Error: Request failed**
- Check your internet connection
- Verify your API key is valid
- Check if you've exceeded the daily limit (150 requests)

## Learn More

- Spoonacular API Documentation: https://spoonacular.com/food-api/docs
- Python Requests Library: https://requests.readthedocs.io/

---

Created by Betül - Industrial Engineering Student at Boğaziçi University