from meal_list import recipes
from meal_list import sections
from recipe_instructions import instructions
import random


def random_menu(num_of_meals):
    """Returns a certain number of randomly selected meals"""
    i = 0
    num_list = list()
    menu = dict()
    groceries = {}
    while len(menu) < num_of_meals:
        num = random.randint(0, len(recipes) - 1)
        if num in num_list: continue
        num_list.append(num)
        # Adds meal to menu
        new_meal = recipes[num]['name']
        instructions_location = recipes[num]['instructions']
        menu[new_meal] = instructions_location
        # Adds ingredients to grocery list
        new_ingredients = recipes[num]['ingredients']
        for k, v in new_ingredients.items():
            q = float(v)
            groceries[k] = groceries.get(k, 0) + q
        i += 1
    return menu, groceries


def sort_groceries(groceries):
    """Returns a grocery list sorted by section of the store based on whole grocery list"""
    # pantry, dairy, meat, produce, bakery, other
    pantry = dict()
    dairy = dict()
    meat = dict()
    produce = dict()
    bakery = dict()
    other = dict()
    # Check each item
    for k, v in groceries.items():
        if check_pantry(k):
            pantry[k] = pantry.get(k, 0) + v
        elif check_bakery(k):
            bakery[k] = bakery.get(k, 0) + v
        elif check_dairy(k):
            dairy[k] = dairy.get(k, 0) + v
        elif check_meat(k):
            meat[k] = meat.get(k, 0) + v
        elif check_produce(k):
            produce[k] = produce.get(k, 0) + v
        else:
            other[k] = other.get(k, 0) + v
        # Combine sections back into sorted dict
    sorted_list = {'PANTRY': pantry, 'DAIRY': dairy, 'MEAT': meat, 'PRODUCE': produce, 'BAKERY': bakery, 'OTHER': other}
    return sorted_list


def check_pantry(name):
    """Returns True if item is in produce section, otherwise False"""
    for k in sections['pantry']:
        if k in name:
            return True
    return False


def check_dairy(name):
    """Returns True if item is in dairy section, otherwise False"""
    for k in sections['dairy']:
        if k in name:
            return True
    return False


def check_meat(name):
    """Returns True if item is in meat section, otherwise False"""
    for k in sections['meat']:
        if k in name:
            return True
    return False

def check_produce(name):
    """Returns True if item is in produce section, otherwise False"""
    for k in sections['produce']:
        if k in name:
            return True
    return False


def check_bakery(name):
    """Returns True is item is in bakery, otherwise False"""
    for k in sections['bakery']:
        if k in name:
            return True
        return False

def itemize_ingredients():
    """Returns an alphabetized list of the ingredient names used in the recipies...to make adding new ones easier"""
    i=0
    store = list()
    while i < len(recipes):
        new_ingredients = recipes[i]['ingredients']
        for k in new_ingredients:
            if k not in store:
                store.append(k)
        i += 1
        store.sort()
    for item in store:
        print(item)


x = random_menu(3)
menu = x[0]
groceries = x[1]
for k in menu:
    print(k, menu[k])
#print(menu)
sorted_list= sort_groceries(groceries)
print('-------------------------------\n\nGrocery List')
print('PANTRY-- ', sorted_list['PANTRY'])
print('DAIRY-- ', sorted_list['DAIRY'])
print('MEAT-- ', sorted_list['MEAT'])
print('PRODUCE-- ', sorted_list['PRODUCE'])
print('OTHER-- ', sorted_list['OTHER'])
print('-------------------------------\n\nInstructions')
for k in menu:
    instructions_location = menu[k]
    print('\n' + k)
    print('Prep -- ')
    print(instructions[instructions_location]['prep'])
    print('Directions --')
    print(instructions[instructions_location]['directions'])
    

#itemize_ingredients()
