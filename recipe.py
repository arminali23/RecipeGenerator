import random

# Define possible categories for the recipe
proteins = ['chicken', 'tofu', 'beef', 'pork', 'fish', 'lentils', 'beans']
vegetables = ['spinach', 'broccoli', 'carrot', 'zucchini', 'tomato', 'bell pepper', 'potato']
grains = ['rice', 'pasta', 'quinoa', 'couscous', 'barley', 'bread']
spices = ['garlic', 'cumin', 'paprika', 'turmeric', 'black pepper', 'oregano', 'chili powder']
herbs = ['basil', 'parsley', 'cilantro', 'rosemary', 'thyme', 'mint']

# Function to generate a recipe based on available ingredients
def generate_recipe(ingredients):
    # Extract ingredients by category
    protein = ingredients.get('protein')
    vegetable = ingredients.get('vegetable')
    grain = ingredients.get('grain')
    spice = ingredients.get('spice')
    herb = ingredients.get('herb', "None")  # Default to "None" if no herb is selected

    # Check if we have all necessary components to generate a recipe
    if not protein or not vegetable or not grain or not spice:
        return "Sorry, not enough ingredients to generate a recipe."

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

# Function to ask user for each ingredient category
def get_user_ingredients():
    print("Welcome to the Recipe Generator!")
    
    # Ask user for ingredients, one category at a time
    protein = input(f"Enter an ingredient for protein (options: {', '.join(proteins)}): ").strip().lower()
    while protein not in proteins:
        print("Invalid protein. Please choose from the following: ", ', '.join(proteins))
        protein = input(f"Enter an ingredient for protein (options: {', '.join(proteins)}): ").strip().lower()

    vegetable = input(f"Enter an ingredient for vegetable (options: {', '.join(vegetables)}): ").strip().lower()
    while vegetable not in vegetables:
        print("Invalid vegetable. Please choose from the following: ", ', '.join(vegetables))
        vegetable = input(f"Enter an ingredient for vegetable (options: {', '.join(vegetables)}): ").strip().lower()

    grain = input(f"Enter an ingredient for grain (options: {', '.join(grains)}): ").strip().lower()
    while grain not in grains:
        print("Invalid grain. Please choose from the following: ", ', '.join(grains))
        grain = input(f"Enter an ingredient for grain (options: {', '.join(grains)}): ").strip().lower()

    spice = input(f"Enter an ingredient for spice (options: {', '.join(spices)}): ").strip().lower()
    while spice not in spices:
        print("Invalid spice. Please choose from the following: ", ', '.join(spices))
        spice = input(f"Enter an ingredient for spice (options: {', '.join(spices)}): ").strip().lower()

    # Optionally ask for an herb
    herb = input(f"Enter an ingredient for herb (optional, options: {', '.join(herbs)}), or press enter to skip: ").strip().lower()
    if herb not in herbs and herb != "":
        print("Invalid herb. Herb will be skipped.")
        herb = "None"  # Default if the herb is not valid or left blank

    # Return the ingredients as a dictionary
    ingredients = {
        'protein': protein,
        'vegetable': vegetable,
        'grain': grain,
        'spice': spice,
        'herb': herb
    }
    
    return ingredients

# Example usage
user_ingredients = get_user_ingredients()

# Generate recipe only if valid ingredients are provided
if user_ingredients:
    generated_recipe = generate_recipe(user_ingredients)
    print("\nGenerated Recipe:")
    print(generated_recipe)
else:
    print("No ingredients provided. Please enter at least one ingredient to generate a recipe.")
