from meal_list import recipes

def goal():
    instructions = {
        'pg 1' : {
            'ingredients' : {},  # same as meal[ingredients] exact
            'prep' : {},         # key is key of meal[ingredients], value is 'see cookbook'
            'directions' : ''    # 'see cookbook'
        }
    }
def instruction_setup():
    """Return the instructions dict this file will hold. 
    Intended to be used once to create the format that will be filled in with recipe instructions."""
    instructions = dict()
    for meal in recipes:
        #create meals dict with ingredients, prep, directions
        meal_dict = dict()
        meal_dict['ingredients'] = meal['ingredients']
        prep = dict()
        for k in meal['ingredients']:
            prep[k] = 'see cookbook'
        meal_dict['prep'] = prep
        meal_dict['directions'] = 'see cookbook'
        #add meals dict to instructions with the key inctrictions_location
        instruction_location = meal['instructions']
        instructions[instruction_location] = meal_dict
    print(instructions)

instruction_setup()

instructions = {
    'pg 1': {
        'ingredients': {'potato (oz)': 12, 'garlic clove': 2, 'yellow onion': 1, 'ground beef (#)': 0.6, 'shredded monty jack (oz)': 4, 'potato bun': 2, 'creamy horseradish sauce (tbsp)': 2},
        'prep': {'potato (oz)': 'see cookbook', 'garlic clove': 'see cookbook', 'yellow onion': 'see cookbook', 'ground beef (#)': 'see cookbook', 'shredded monty jack (oz)': 'see cookbook', 'potato bun': 'see cookbook', 'creamy horseradish sauce (tbsp)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 2': {
        'ingredients': {'lime': 1, 'garlic clove': 2, 'peanuts (oz)': 3, 'coleslaw mix (oz)': 6, 'sour cream (oz)': 2, 'ground pork (#)': 0.6, 'sweet thai chili sauce (oz)': 1, 'ponzu sauce (oz)': 2, 'cornstarch (tbsp)': 1, 'taco tortillas': 6},
        'prep': {'lime': 'see cookbook', 'garlic clove': 'see cookbook', 'peanuts (oz)': 'see cookbook', 'coleslaw mix (oz)': 'see cookbook', 'sour cream (oz)': 'see cookbook', 'ground pork (#)': 'see cookbook', 'sweet thai chili sauce (oz)': 'see cookbook', 'ponzu sauce (oz)': 'see cookbook', 'cornstarch (tbsp)': 'see cookbook', 'taco tortillas': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 3': {
        'ingredients': {'garlic clove': 2, 'chicken sausage (#)': 0.6, 'rigatoni (oz)': 6, 'peas (oz)': 10, 'cream sauce base (oz)': 4, 'mushroom stock concentrate': 1, 'garlic powder (tbsp)': 1},
        'prep': {'garlic clove': 'see cookbook', 'chicken sausage (#)': 'see cookbook', 'rigatoni (oz)': 'see cookbook', 'peas (oz)': 'see cookbook', 'cream sauce base (oz)': 'see cookbook', 'mushroom stock concentrate': 'see cookbook', 'garlic powder (tbsp)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 4': {
        'ingredients': {'carrot (oz)': 12, 'side green': 1, 'shallot': 1, 'chicken breast (#)': 2, 'chicken stock concentrate': 1, 'dijon mustard (tbsp)': 1, 'apricot jam (tbsp)': 2},
        'prep': {'carrot (oz)': 'see cookbook', 'side green': 'see cookbook', 'shallot': 'see cookbook', 'chicken breast (#)': 'see cookbook', 'chicken stock concentrate': 'see cookbook', 'dijon mustard (tbsp)': 'see cookbook', 'apricot jam (tbsp)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 5': {
        'ingredients': {'garlic pepper (tsp)': 0.24, 'scallion': 2, 'mushroom seasoning (tsp)': 2, 'shredded cheddar cheese (oz)': 1, 'yukon potato (oz)': 12, 'mirepoix stock concentrate (tsp)': 2, 'cream cheese (oz)': 1, 'steak strips (oz)': 10},
        'prep': {'garlic pepper (tsp)': 'see cookbook', 'scallion': 'see cookbook', 'mushroom seasoning (tsp)': 'see cookbook', 'shredded cheddar cheese (oz)': 'see cookbook', 'yukon potato (oz)': 'see cookbook', 'mirepoix stock concentrate (tsp)': 'see cookbook', 'cream cheese (oz)': 'see cookbook', 'steak strips (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 6': {
        'ingredients': {'red pepper flakes (tsp)': 0.25, 'garlic salt (tsp)': 0.5, 'butter (tbsp)': 1, 'sour cream (oz)': 2, 'russet potato (oz)': 10, 'side green': 1, 'bbq spice rub (tsp)': 1, 'boneless pork chop': 2},
        'prep': {'red pepper flakes (tsp)': 'see cookbook', 'garlic salt (tsp)': 'see cookbook', 'butter (tbsp)': 'see cookbook', 'sour cream (oz)': 'see cookbook', 'russet potato (oz)': 'see cookbook', 'side green': 'see cookbook', 'bbq spice rub (tsp)': 'see cookbook', 'boneless pork chop': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 7': {
        'ingredients': {'peas (oz)': 10, 'red pepper flakes (tsp)': 0.25, 'cream cheese (oz)': 1, 'scallion': 2, 'goat cheese (oz)': 1, 'grated parmesan (oz)': 0.5, 'penne pasta (oz)': 5, 'flour (oz)': 0.25, 'marinara sauce (oz)': 4, 'italian pork sausage (#)': 0.75},
        'prep': {'peas (oz)': 'see cookbook', 'red pepper flakes (tsp)': 'see cookbook', 'cream cheese (oz)': 'see cookbook', 'scallion': 'see cookbook', 'goat cheese (oz)': 'see cookbook', 'grated parmesan (oz)': 'see cookbook', 'penne pasta (oz)': 'see cookbook', 'flour (oz)': 'see cookbook', 'marinara sauce (oz)': 'see cookbook', 'italian pork sausage (#)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 8': {
        'ingredients': {'roma tomato': 1, 'yellow onion': 1, 'tex-mex paste (oz)': 1, 'jasmine rice': 1, 'black bean can (oz)': 10, 'cream cheese (oz)': 1, 'burrito tortilla': 2, 'guacamole': 1},
        'prep': {'roma tomato': 'see cookbook', 'yellow onion': 'see cookbook', 'tex-mex paste (oz)': 'see cookbook', 'jasmine rice': 'see cookbook', 'black bean can (oz)': 'see cookbook', 'cream cheese (oz)': 'see cookbook', 'burrito tortilla': 'see cookbook', 'guacamole': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 9': {
        'ingredients': {'ground beef (#)': 0.5, 'jasmine rice': 1, 'garlic clove': 3, 'carrot (oz)': 3, 'mini cucumber': 1, 'sriracha': 1, 'ponzu sauce (oz)': 4, 'lime': 1, 'yellow onion': 1, 'scallion': 1},
        'prep': {'ground beef (#)': 'see cookbook', 'jasmine rice': 'see cookbook', 'garlic clove': 'see cookbook', 'carrot (oz)': 'see cookbook', 'mini cucumber': 'see cookbook', 'sriracha': 'see cookbook', 'ponzu sauce (oz)': 'see cookbook', 'lime': 'see cookbook', 'yellow onion': 'see cookbook', 'scallion': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 10': {
        'ingredients': {'parsley bunch': 1, 'garlic clove': 1, 'potato (oz)': 12, 'sliced almonds (oz)': 1, 'ranch steak': 2, 'green beans (oz)': 12},
        'prep': {'parsley bunch': 'see cookbook', 'garlic clove': 'see cookbook', 'potato (oz)': 'see cookbook', 'sliced almonds (oz)': 'see cookbook', 'ranch steak': 'see cookbook', 'green beans (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 11': {
        'ingredients': {'pablano': 1, 'scallion': 1, 'garlic clove': 1, 'roma tomato': 1, 'cornstarch (tbsp)': 1, 'tex-mex paste (oz)': 1, 'southwest spice': 1, 'black bean can (oz)': 10, 'taco tortillas': 6, 'shredded monty jack (oz)': 3},
        'prep': {'pablano': 'see cookbook', 'scallion': 'see cookbook', 'garlic clove': 'see cookbook', 'roma tomato': 'see cookbook', 'cornstarch (tbsp)': 'see cookbook', 'tex-mex paste (oz)': 'see cookbook', 'southwest spice': 'see cookbook', 'black bean can (oz)': 'see cookbook', 'taco tortillas': 'see cookbook', 'shredded monty jack (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 12': {
        'ingredients': {'roma tomato': 1, 'garlic clove': 2, 'linguine': 1, 'italian pork sausage (#)': 0.5, 'italian seasoning': 1, 'cream cheese (oz)': 1, 'chicken stock concentrate': 1, 'cream sauce base (oz)': 4, 'ciabatta': 1},
        'prep': {'roma tomato': 'see cookbook', 'garlic clove': 'see cookbook', 'linguine': 'see cookbook', 'italian pork sausage (#)': 'see cookbook', 'italian seasoning': 'see cookbook', 'cream cheese (oz)': 'see cookbook', 'chicken stock concentrate': 'see cookbook', 'cream sauce base (oz)': 'see cookbook', 'ciabatta': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 13': {
        'ingredients': {'chipotle pesto (tbsp)': 1, 'mirepoix stock concentrate (tsp)': 2, 'sour cream (oz)': 1, 'yellow onion': 0.5, 'pepper': 1, 'lime': 1, 'taco tortillas': 6, 'fajita seasoning (tsp)': 2, 'sliced pork (#)': 0.6},
        'prep': {'chipotle pesto (tbsp)': 'see cookbook', 'mirepoix stock concentrate (tsp)': 'see cookbook', 'sour cream (oz)': 'see cookbook', 'yellow onion': 'see cookbook', 'pepper': 'see cookbook', 'lime': 'see cookbook', 'taco tortillas': 'see cookbook', 'fajita seasoning (tsp)': 'see cookbook', 'sliced pork (#)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 14': {
        'ingredients': {'potato (oz)': 12, 'green beans (oz)': 12, 'garlic clove': 1, 'pork chop': 2, 'balsamic vinegar (oz)': 1, 'cherry jam (tbsp)': 3, 'chicken stock concentrate': 1, 'soy sauce (oz)': 1},
        'prep': {'potato (oz)': 'see cookbook', 'green beans (oz)': 'see cookbook', 'garlic clove': 'see cookbook', 'pork chop': 'see cookbook', 'balsamic vinegar (oz)': 'see cookbook', 'cherry jam (tbsp)': 'see cookbook', 'chicken stock concentrate': 'see cookbook', 'soy sauce (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 21': {
        'ingredients': {'shredded mozzarella (oz)': 2, 'red pepper flakes (tsp)': 0.25, 'grated parmesan (oz)': 2, 'marinara sauce (oz)': 8, 'baby spinach (oz)': 5, 'bolognese meat sauce (oz)': 12, 'gemelli pasta (oz)': 6},
        'prep': {'shredded mozzarella (oz)': 'see cookbook', 'red pepper flakes (tsp)': 'see cookbook', 'grated parmesan (oz)': 'see cookbook', 'marinara sauce (oz)': 'see cookbook', 'baby spinach (oz)': 'see cookbook', 'bolognese meat sauce (oz)': 'see cookbook', 'gemelli pasta (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 15': {
        'ingredients': {'garlic clove': 2, 'yellow onion': 1, 'celery stalk': 1, 'italian seasoning': 1, 'tomato paste (oz)': 2, 'chicken stock concentrate': 1, 'mushroom stock concentrate': 1, 'cream cheese (oz)': 1, 'ciabatta': 1, 'carrot (oz)': 3, 'italian pork sausage (#)': 0.4},
        'prep': {'garlic clove': 'see cookbook', 'yellow onion': 'see cookbook', 'celery stalk': 'see cookbook', 'italian seasoning': 'see cookbook', 'tomato paste (oz)': 'see cookbook', 'chicken stock concentrate': 'see cookbook', 'mushroom stock concentrate': 'see cookbook', 'cream cheese (oz)': 'see cookbook', 'ciabatta': 'see cookbook', 'carrot (oz)': 'see cookbook', 'italian pork sausage (#)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 16': {
        'ingredients': {'red bell pepper': 1, 'garlic clove': 1, 'cavatappi pasta (oz)': 1, 'chicken sausage (#)': 0.5, 'tomato paste (oz)': 1, 'garlic powder (tbsp)': 1, 'cream sauce base (oz)': 4},
        'prep': {'red bell pepper': 'see cookbook', 'garlic clove': 'see cookbook', 'cavatappi pasta (oz)': 'see cookbook', 'chicken sausage (#)': 'see cookbook', 'tomato paste (oz)': 'see cookbook', 'garlic powder (tbsp)': 'see cookbook', 'cream sauce base (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 17': {
        'ingredients': {'side green': 1, 'garlic clove': 1, 'italian seasoning': 1, 'panko (c)': 0.25, 'ciabatta': 1, 'chicken breast (#)': 0.6, 'sour cream (oz)': 1, 'marinara sauce (oz)': 3, 'shredded monty jack (oz)': 2},
        'prep': {'side green': 'see cookbook', 'garlic clove': 'see cookbook', 'italian seasoning': 'see cookbook', 'panko (c)': 'see cookbook', 'ciabatta': 'see cookbook', 'chicken breast (#)': 'see cookbook', 'sour cream (oz)': 'see cookbook', 'marinara sauce (oz)': 'see cookbook', 'shredded monty jack (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 18': {
        'ingredients': {'enchilada sauce (oz)': 5, 'corn (oz)': 5, 'black bean can (oz)': 15, 'jalapeno': 1, 'red onion': 1, 'pablano': 1, 'taco seasoning (tsp)': 2, 'taco tortillas': 6, 'shredded white cheddar cheese (oz)': 2, 'sour cream (oz)': 2},
        'prep': {'enchilada sauce (oz)': 'see cookbook', 'corn (oz)': 'see cookbook', 'black bean can (oz)': 'see cookbook', 'jalapeno': 'see cookbook', 'red onion': 'see cookbook', 'pablano': 'see cookbook', 'taco seasoning (tsp)': 'see cookbook', 'taco tortillas': 'see cookbook', 'shredded white cheddar cheese (oz)': 'see cookbook', 'sour cream (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'R': {
        'ingredients': {'cream of chicken soup (can)': 1, 'tuna in water canned': 1, 'peas (oz)': 10, 'egg noodles': 1},
        'prep': {'cream of chicken soup (can)': 'see cookbook', 'tuna in water canned': 'see cookbook', 'peas (oz)': 'see cookbook', 'egg noodles': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 19': {
        'ingredients': {'potato (oz)': 12, 'garlic clove': 2, 'carrot (oz)': 3, 'celery stalk': 1, 'yellow onion': 1, 'dried thyme': 1, 'chicken stock concentrate': 1, 'sour cream (oz)': 1},
        'prep': {'potato (oz)': 'see cookbook', 'garlic clove': 'see cookbook', 'carrot (oz)': 'see cookbook', 'celery stalk': 'see cookbook', 'yellow onion': 'see cookbook', 'dried thyme': 'see cookbook', 'chicken stock concentrate': 'see cookbook', 'sour cream (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 20': {
        'ingredients': {'pablano': 1, 'taco seasoning (tsp)': 1, 'salsa verde (oz)': 12, 'scallion': 2, 'taco tortillas': 6, 'sour cream (oz)': 2, 'shredded mexican cheese blend (oz)': 2, 'cream cheese (oz)': 1},
        'prep': {'pablano': 'see cookbook', 'taco seasoning (tsp)': 'see cookbook', 'salsa verde (oz)': 'see cookbook', 'scallion': 'see cookbook', 'taco tortillas': 'see cookbook', 'sour cream (oz)': 'see cookbook', 'shredded mexican cheese blend (oz)': 'see cookbook', 'cream cheese (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 23': {
        'ingredients': {'basil pesto (oz)': 2, 'red pepper flakes (tsp)': 0.25, 'cream cheese (oz)': 1, 'chicken stock concentrate': 1, 'grated parmesan (oz)': 2, 'cooked chicken breast (#)': 1, 'cream sauce base (oz)': 4, 'grape tomatoes (oz)': 4, 'penne pasta (oz)': 5},
        'prep': {'basil pesto (oz)': 'see cookbook', 'red pepper flakes (tsp)': 'see cookbook', 'cream cheese (oz)': 'see cookbook', 'chicken stock concentrate': 'see cookbook', 'grated parmesan (oz)': 'see cookbook', 'cooked chicken breast (#)': 'see cookbook', 'cream sauce base (oz)': 'see cookbook', 'grape tomatoes (oz)': 'see cookbook', 'penne pasta (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 24': {
        'ingredients': {'potato (oz)': 10, 'green bell pepper': 1, 'yellow onion': 1, 'fry seasoning (tsp)': 3, 'bread (slice)': 1, 'ground beef (#)': 0.5, 'shredded pepper jack (oz)': 2, 'dijon mustard (tbsp)': 1},
        'prep': {'potato (oz)': 'see cookbook', 'green bell pepper': 'see cookbook', 'yellow onion': 'see cookbook', 'fry seasoning (tsp)': 'see cookbook', 'bread (slice)': 'see cookbook', 'ground beef (#)': 'see cookbook', 'shredded pepper jack (oz)': 'see cookbook', 'dijon mustard (tbsp)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 25': {
        'ingredients': {'roma tomato': 1, 'yellow onion': 1, 'lime': 1, 'garlic clove': 2, 'sour cream (oz)': 1, 'ground pork (#)': 0.7, 'southwest spice': 1, 'chicken stock concentrate': 1, 'taco tortillas': 6, 'shredded monty jack (oz)': 2},
        'prep': {'roma tomato': 'see cookbook', 'yellow onion': 'see cookbook', 'lime': 'see cookbook', 'garlic clove': 'see cookbook', 'sour cream (oz)': 'see cookbook', 'ground pork (#)': 'see cookbook', 'southwest spice': 'see cookbook', 'chicken stock concentrate': 'see cookbook', 'taco tortillas': 'see cookbook', 'shredded monty jack (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 26': {
        'ingredients': {'yellow onion': 1, 'garlic clove': 2, 'potato (oz)': 12, 'jalapeno': 1, 'corn (oz)': 10, 'chicken stock concentrate': 1, 'cream cheese (oz)': 2, 'sour cream (oz)': 4},
        'prep': {'yellow onion': 'see cookbook', 'garlic clove': 'see cookbook', 'potato (oz)': 'see cookbook', 'jalapeno': 'see cookbook', 'corn (oz)': 'see cookbook', 'chicken stock concentrate': 'see cookbook', 'cream cheese (oz)': 'see cookbook', 'sour cream (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 27': {
        'ingredients': {'jasmine rice': 1, 'green bell pepper': 1, 'ginger (nub)': 1, 'scallion': 1, 'garlic clove': 1, 'peanuts (oz)': 1, 'ground beef (#)': 0.5, 'sweet soy glaze (oz)': 2},
        'prep': {'jasmine rice': 'see cookbook', 'green bell pepper': 'see cookbook', 'ginger (nub)': 'see cookbook', 'scallion': 'see cookbook', 'garlic clove': 'see cookbook', 'peanuts (oz)': 'see cookbook', 'ground beef (#)': 'see cookbook', 'sweet soy glaze (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 28': {
        'ingredients': {'potato (oz)': 10, 'yellow onion': 1, 'roma tomato': 1, 'southwest spice': 1, 'chicken breast (#)': 0.7, 'burrito tortilla': 2},
        'prep': {'potato (oz)': 'see cookbook', 'yellow onion': 'see cookbook', 'roma tomato': 'see cookbook', 'southwest spice': 'see cookbook', 'chicken breast (#)': 'see cookbook', 'burrito tortilla': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 29': {
        'ingredients': {'chili garlic sauce (tsp)': 1, 'panko (c)': 0.13, 'toasted sesame oil (oz)': 0.25, 'sweet and sour sauce': 1, 'garlic sesame sauce (oz)': 1, 'peanuts (oz)': 0.5, 'green beans (oz)': 12, 'asian garlic, ginger, & chile seasoning (tsp)': 1, 'ground pork (#)': 0.7},
        'prep': {'chili garlic sauce (tsp)': 'see cookbook', 'panko (c)': 'see cookbook', 'toasted sesame oil (oz)': 'see cookbook', 'sweet and sour sauce': 'see cookbook', 'garlic sesame sauce (oz)': 'see cookbook', 'peanuts (oz)': 'see cookbook', 'green beans (oz)': 'see cookbook', 'asian garlic, ginger, & chile seasoning (tsp)': 'see cookbook', 'ground pork (#)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 30': {
        'ingredients': {'spaghetti (oz)': 5, 'lemon': 1, 'flour (oz)': 1, 'grated parmesan (oz)': 0.5, 'chicken cutlet (#)': 0.7, 'roasted garlic and herb butter (oz)': 0.75, 'capers (oz)': 0.5, 'butter (oz)': 0.6, 'garlic pepper (tsp)': 2, 'shallot': 1},
        'prep': {'spaghetti (oz)': 'see cookbook', 'lemon': 'see cookbook', 'flour (oz)': 'see cookbook', 'grated parmesan (oz)': 'see cookbook', 'chicken cutlet (#)': 'see cookbook', 'roasted garlic and herb butter (oz)': 'see cookbook', 'capers (oz)': 'see cookbook', 'butter (oz)': 'see cookbook', 'garlic pepper (tsp)': 'see cookbook', 'shallot': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 31': {
        'ingredients': {'chile and cumin rub (tsp)': 1, 'jasmine rice': 1, 'jalapeno': 1, 'lime': 1, 'adobo seasoning (tsp)': 1, 'chile lime butter (oz)': 0.8, 'shallot': 1, 'pineapple chunks (oz)': 2, 'corn (oz)': 3, 'steak strips (#)': 0.7},
        'prep': {'chile and cumin rub (tsp)': 'see cookbook', 'jasmine rice': 'see cookbook', 'jalapeno': 'see cookbook', 'lime': 'see cookbook', 'adobo seasoning (tsp)': 'see cookbook', 'chile lime butter (oz)': 'see cookbook', 'shallot': 'see cookbook', 'pineapple chunks (oz)': 'see cookbook', 'corn (oz)': 'see cookbook', 'steak strips (#)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 32': {
        'ingredients': {'yukon gold potato (oz)': 10, 'italian pork sausage (#)': 0.5, 'red bell pepper': 1, 'garlic powder (tbsp)': 0.5, 'dijon mustard (tbsp)': 1, 'ketchup': 1, 'italian seasoning': 1, 'yellow onion': 1, 'demi-baguette': 2, 'chicken stock concentrate': 1, 'shredded mozzarella (oz)': 3},
        'prep': {'yukon gold potato (oz)': 'see cookbook', 'italian pork sausage (#)': 'see cookbook', 'red bell pepper': 'see cookbook', 'garlic powder (tbsp)': 'see cookbook', 'dijon mustard (tbsp)': 'see cookbook', 'ketchup': 'see cookbook', 'italian seasoning': 'see cookbook', 'yellow onion': 'see cookbook', 'demi-baguette': 'see cookbook', 'chicken stock concentrate': 'see cookbook', 'shredded mozzarella (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 33': {
        'ingredients': {'corn (oz)': 3, 'scallion': 2, 'roma tomato': 1, 'pot-roast seasoning (tsp)': 1.5, 'arborio rice (oz)': 3.6, 'grated parmesan (oz)': 2, 'sour cream': 2, 'beef demi-glace (tsp)': 2, 'steak strips (#)': 0.7},
        'prep': {'corn (oz)': 'see cookbook', 'scallion': 'see cookbook', 'roma tomato': 'see cookbook', 'pot-roast seasoning (tsp)': 'see cookbook', 'arborio rice (oz)': 'see cookbook', 'grated parmesan (oz)': 'see cookbook', 'sour cream': 'see cookbook', 'beef demi-glace (tsp)': 'see cookbook', 'steak strips (#)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 34': {
        'ingredients': {'cream cheese (oz)': 1.5, 'yellow onion': 1, 'garlic clove': 2, 'potato (oz)': 12, 'kale': 1, 'chicken sausage (#)': 0.5, 'chicken stock concentrate': 1, 'italian seasoning': 1, 'sour cream (oz)': 2},
        'prep': {'cream cheese (oz)': 'see cookbook', 'yellow onion': 'see cookbook', 'garlic clove': 'see cookbook', 'potato (oz)': 'see cookbook', 'kale': 'see cookbook', 'chicken sausage (#)': 'see cookbook', 'chicken stock concentrate': 'see cookbook', 'italian seasoning': 'see cookbook', 'sour cream (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 35': {
        'ingredients': {'shredded red cabbage (oz)': 3, 'scallion': 2, 'cornstarch (tbsp)': 0.25, 'soy sauce (oz)': 0.2, 'brown stir fry sauce': 4, 'asian noodles (oz)': 10, 'sliced pork (#)': 0.7, 'sesame seeds (tsp)': 1, 'hot sauce (oz)': 0.25},
        'prep': {'shredded red cabbage (oz)': 'see cookbook', 'scallion': 'see cookbook', 'cornstarch (tbsp)': 'see cookbook', 'soy sauce (oz)': 'see cookbook', 'brown stir fry sauce': 'see cookbook', 'asian noodles (oz)': 'see cookbook', 'sliced pork (#)': 'see cookbook', 'sesame seeds (tsp)': 'see cookbook', 'hot sauce (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 36': {
        'ingredients': {'potato (oz)': 12, 'pablano': 1, 'red onion': 1, 'lime': 1, 'bbq sauce (oz)': 2, 'sour cream (oz)': 1, 'ground beef (#)': 0.5, 'shredded cheddar cheese (oz)': 1},
        'prep': {'potato (oz)': 'see cookbook', 'pablano': 'see cookbook', 'red onion': 'see cookbook', 'lime': 'see cookbook', 'bbq sauce (oz)': 'see cookbook', 'sour cream (oz)': 'see cookbook', 'ground beef (#)': 'see cookbook', 'shredded cheddar cheese (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 37': {'ingredients': {'potato': 10, 'yellow onion': 1, 'garlic clove': 1, 'demi-bagguette': 2, 'italian pork sausage (#)': 0.4, 'marinara sauce (oz)': 6, 'shredded monty jack (oz)': 3},
    'prep': {'potato': 'see cookbook', 'yellow onion': 'see cookbook', 'garlic clove': 'see cookbook', 'demi-bagguette': 'see cookbook', 'italian pork sausage (#)': 'see cookbook', 'marinara sauce (oz)': 'see cookbook', 'shredded monty jack (oz)': 'see cookbook'},
    'directions': 'see cookbook'
    },
    'pg 38': {
        'ingredients': {'yukon gold potato (oz)': 10, 'panko (c)': 0.5, 'sweet and smokey bbq seasoning (tbsp)': 1, 'chicken breast (#)': 0.75, 'sour cream (oz)': 2, 'side green': 1, 'hot honey (oz)': 0.75},
        'prep': {'yukon gold potato (oz)': 'see cookbook', 'panko (c)': 'see cookbook', 'sweet and smokey bbq seasoning (tbsp)': 'see cookbook', 'chicken breast (#)': 'see cookbook', 'sour cream (oz)': 'see cookbook', 'side green': 'see cookbook', 'hot honey (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 39': {
        'ingredients': {'scallion': 2, 'tex-mex paste (oz)': 1, 'queso blanco (oz)': 3, 'cream cheese (tbsp)': 2, 'cornstarch (tbsp)': 1, 'mexican cheese blend (oz)': 2, 'cavatappi pasta (oz)': 6, 'shredded monty jack (oz)': 6, 'panko (c)': 0.5},
        'prep': {'scallion': 'see cookbook', 'tex-mex paste (oz)': 'see cookbook', 'queso blanco (oz)': 'see cookbook', 'cream cheese (tbsp)': 'see cookbook', 'cornstarch (tbsp)': 'see cookbook', 'mexican cheese blend (oz)': 'see cookbook', 'cavatappi pasta (oz)': 'see cookbook', 'shredded monty jack (oz)': 'see cookbook', 'panko (c)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 40': {'ingredients': {'roma tomato': 1, 'yellow onion': 1, 'lime': 1, 'garlic cloves': 2, 'ground beef (#)': 0.5, 'southwest spice blend': 1, 'beef stock concentrate': 1, 'taco tortillas': 6, 'shredded mozzarella (oz)': 3},
    'prep': {'roma tomato': 'see cookbook', 'yellow onion': 'see cookbook', 'lime': 'see cookbook', 'garlic cloves': 'see cookbook', 'ground beef (#)': 'see cookbook', 'southwest spice blend': 'see cookbook', 'beef stock concentrate': 'see cookbook', 'taco tortillas': 'see cookbook', 'shredded mozzarella (oz)': 'see cookbook'},
    'directions': 'see cookbook'
    },
    'pg 41': {
        'ingredients': {'yukon gold potato (oz)': 12, 'shallot': 1, 'rosemary': 1, 'lemon': 1, 'side green': 1, 'chicken breast (#)': 0.7, 'balsamic vinegar (oz)': 2, 'fig jam (tbsp)': 2, 'chicken stock concentrate': 1},
        'prep': {'yukon gold potato (oz)': 'see cookbook', 'shallot': 'see cookbook', 'rosemary': 'see cookbook', 'lemon': 'see cookbook', 'side green': 'see cookbook', 'chicken breast (#)': 'see cookbook', 'balsamic vinegar (oz)': 'see cookbook', 'fig jam (tbsp)': 'see cookbook', 'chicken stock concentrate': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 42': {
        'ingredients': {'scallion': 1, 'white wine vinegar (oz)': 1, 'yukon gold potato (oz)': 12, 'smokey cinnamon paprika spice (tbsp)': 1, 'cherry jam (oz)': 1, 'carrot, shredded (oz)': 4, 'pork tenderloin (#)': 0.8, 'apple': 1, 'sour cream (oz)': 1},
        'prep': {'scallion': 'see cookbook', 'white wine vinegar (oz)': 'see cookbook', 'yukon gold potato (oz)': 'see cookbook', 'smokey cinnamon paprika spice (tbsp)': 'see cookbook', 'cherry jam (oz)': 'see cookbook', 'carrot, shredded (oz)': 'see cookbook', 'pork tenderloin (#)': 'see cookbook', 'apple': 'see cookbook', 'sour cream (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 43': {
        'ingredients': {'garlic clove': 2, 'yogurt (tbsp)': 4, 'shawarma spice blend (tbsp)': 1, 'chicken cutlet (#)': 0.7, 'zucchini': 1, 'roma tomato': 1, 'scallion': 2, 'lemon': 1, 'sour cream (oz)': 2, 'chicken stock concentrate': 1, 'turmeric (tsp)': 1, 'couscous (c)': 0.5, 'hummus (oz)': 2, 'hot sauce (tsp)': 1},
        'prep': {'garlic clove': 'see cookbook', 'yogurt (tbsp)': 'see cookbook', 'shawarma spice blend (tbsp)': 'see cookbook', 'chicken cutlet (#)': 'see cookbook', 'zucchini': 'see cookbook', 'roma tomato': 'see cookbook', 'scallion': 'see cookbook', 'lemon': 'see cookbook', 'sour cream (oz)': 'see cookbook', 'chicken stock concentrate': 'see cookbook', 'turmeric (tsp)': 'see cookbook', 'couscous (c)': 'see cookbook', 'hummus (oz)': 'see cookbook', 'hot sauce (tsp)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 44': {
        'ingredients': {'lime': 1, 'scallion': 2, 'mayo (oz)': 0.8, 'hot sauce (oz)': 0.5, 'slaw mix (oz)': 4, 'gochujang red pepper paste (tbsp)': 1, 'ginger (nub)': 1, 'taco tortilla': 6},
        'prep': {'lime': 'see cookbook', 'scallion': 'see cookbook', 'mayo (oz)': 'see cookbook', 'hot sauce (oz)': 'see cookbook', 'slaw mix (oz)': 'see cookbook', 'gochujang red pepper paste (tbsp)': 'see cookbook', 'ginger (nub)': 'see cookbook', 'taco tortilla': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 45': {
        'ingredients': {'scallion': 2, 'roma tomato': 1, 'lemon': 1, 'italian chicken sausage (#)': 0.5, 'italian seasoning': 1, 'spinach and cheese ravioli (oz)': 9, 'chicken stock concentrate': 1, 'sour cream (oz)': 2},
        'prep': {'scallion': 'see cookbook', 'roma tomato': 'see cookbook', 'lemon': 'see cookbook', 'italian chicken sausage (#)': 'see cookbook', 'italian seasoning': 'see cookbook', 'spinach and cheese ravioli (oz)': 'see cookbook', 'chicken stock concentrate': 'see cookbook', 'sour cream (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 46': {
        'ingredients': {'potato (oz)': 10, 'yellow onion': 1, 'garlic clove': 1, 'potato bun': 2, 'ground beef (#)': 0.6, 'dijon mustard (tbsp)': 2},
        'prep': {'potato (oz)': 'see cookbook', 'yellow onion': 'see cookbook', 'garlic clove': 'see cookbook', 'potato bun': 'see cookbook', 'ground beef (#)': 'see cookbook', 'dijon mustard (tbsp)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 47': {
        'ingredients': {'taco tortilla': 6, 'chipotle crema (oz)': 2, 'shredded mozzarella (oz)': 4, 'red onion': 0.5, 'taco seasoning (tbsp)': 1, 'cilantro (oz)': 0.25, 'lime': 1, 'jalapeno': 1, 'ground turkey (#)': 0.6},
        'prep': {'taco tortilla': 'see cookbook', 'chipotle crema (oz)': 'see cookbook', 'shredded mozzarella (oz)': 'see cookbook', 'red onion': 'see cookbook', 'taco seasoning (tbsp)': 'see cookbook', 'cilantro (oz)': 'see cookbook', 'lime': 'see cookbook', 'jalapeno': 'see cookbook', 'ground turkey (#)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 48': {
        'ingredients': {'gemelli pasta (oz)': 6, 'pablano': 1, 'roma tomato': 1, 'grated parmesan (oz)': 1, 'scallion': 2, 'cream sauce base (oz)': 4, 'cajun seasoning (tsp)': 2, 'italian pork sausage (#)': 0.5},
        'prep': {'gemelli pasta (oz)': 'see cookbook', 'pablano': 'see cookbook', 'roma tomato': 'see cookbook', 'grated parmesan (oz)': 'see cookbook', 'scallion': 'see cookbook', 'cream sauce base (oz)': 'see cookbook', 'cajun seasoning (tsp)': 'see cookbook', 'italian pork sausage (#)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 49': {
        'ingredients': {'scallion': 1, 'garlic clove': 2, 'jasmine rice': 1, 'carrot (oz)': 12, 'lime': 1, 'soy sauce (oz)': 1, 'sweet thai chili sauce (oz)': 3, 'chicken breast (#)': 10},
        'prep': {'scallion': 'see cookbook', 'garlic clove': 'see cookbook', 'jasmine rice': 'see cookbook', 'carrot (oz)': 'see cookbook', 'lime': 'see cookbook', 'soy sauce (oz)': 'see cookbook', 'sweet thai chili sauce (oz)': 'see cookbook', 'chicken breast (#)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 50': {
        'ingredients': {'crushed tomatoes (oz)': 4, 'fettuccine (oz)': 4, 'red pepper flakes (tsp)': 0.25, 'peas (oz)': 3, 'cream sauce base (oz)': 4, 'italian seasoning': 1, 'garlic clove': 2, 'italian pork sausage (#)': 0.5},
        'prep': {'crushed tomatoes (oz)': 'see cookbook', 'fettuccine (oz)': 'see cookbook', 'red pepper flakes (tsp)': 'see cookbook', 'peas (oz)': 'see cookbook', 'cream sauce base (oz)': 'see cookbook', 'italian seasoning': 'see cookbook', 'garlic clove': 'see cookbook', 'italian pork sausage (#)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 51': {
        'ingredients': {'potato (oz)': 12, 'green beans (oz)': 12, 'yellow onion': 1, 'garlic clove': 2, 'pork chops (#)': 0.6, 'worcestershire sauce (oz)': 0.75},
        'prep': {'potato (oz)': 'see cookbook', 'green beans (oz)': 'see cookbook', 'yellow onion': 'see cookbook', 'garlic clove': 'see cookbook', 'pork chops (#)': 'see cookbook', 'worcestershire sauce (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 22': {
        'ingredients': {'garlic clove': 2, 'lime': 1, 'roma tomato': 1, 'yellow onion': 1, 'tex-mex paste': 1, 'sour cream (oz)': 2, 'pork chops (#)': 0.75, 'taco tortillas': 6},
        'prep': {'garlic clove': 'see cookbook', 'lime': 'see cookbook', 'roma tomato': 'see cookbook', 'yellow onion': 'see cookbook', 'tex-mex paste': 'see cookbook', 'sour cream (oz)': 'see cookbook', 'pork chops (#)': 'see cookbook', 'taco tortillas': 'see cookbook'},
        'directions': 'see cookbook'
    }
}
