import random

# Define possible categories for the recipe
proteins = ['chicken', 'tofu', 'beef', 'pork', 'fish', 'lentils', 'beans']
vegetables = ['spinach', 'broccoli', 'carrot', 'zucchini', 'tomato', 'bell pepper', 'potato']
grains = ['rice', 'pasta', 'quinoa', 'couscous', 'barley', 'bread']
spices = ['garlic', 'cumin', 'paprika', 'turmeric', 'black pepper', 'oregano', 'chili powder']
herbs = ['basil', 'parsley', 'cilantro', 'rosemary', 'thyme', 'mint']

# Function to generate a random recipe based on random ingredients
def generate_random_recipe():
    # Randomly select ingredients from each category
    protein = random.choice(proteins)
    vegetable = random.choice(vegetables)
    grain = random.choice(grains)
    spice = random.choice(spices)
    herb = random.choice(herbs)

    # Generating a recipe with selected ingredients
    recipe = f"""
    **Recipe: {protein.capitalize()} and {vegetable.capitalize()} with {grain.capitalize()}**
    
    Ingredients:
    - 1 serving of {protein}
    - 1 {vegetable}
    - 1 cup of {grain}
    - 1 tsp of {spice}
    - Fresh {herb} (optional)
 
    Instructions:
    1. Cook the {grain} according to package instructions.
    2. In a pan, sauté the {protein} until golden brown.
    3. Add the {vegetable} and cook for about 5-7 minutes.
    4. Season with {spice} and cook until everything is well combined.
    5. Serve the {protein} and {vegetable} mixture over the {grain}, garnish with fresh {herb} if available.
    
    Enjoy your meal!
    """

    return recipe

# Generate a random recipe and print it
random_recipe = generate_random_recipe()
print(random_recipe)
