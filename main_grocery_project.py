from recipe_ingredients import get_ingredients
from recipe_list import recipes
import random
grocery_list = dict()

def create_menue() :
    """Retunrns a list of recipies"""
    menue = list()
    while True :
        new_meal = input("Enter a meal: ").lower()
        if new_meal == "done" : break
        # Add check that item is available (object created for it)
        menue.append(new_meal)
    return menue

    
def random_menue(num_of_meals) :
    """Returns a certain number of randomly selected meals"""
    i = 0
    num_list = list()
    menue = list()
    groceries = {}
    while len(menue) < num_of_meals :
        num = random.randint(0, len(recipes) - 1)
        if num in num_list : continue
        num_list.append(num)
        # Adds meal to menue
        new_meal = recipes[num]['name']
        menue.append(new_meal)
        # Adds ingredients to grocery list
        new_ingredients = recipes[num]['ingredients']
        for k, v in new_ingredients.items() :
            q = float(v)
            groceries[k] = groceries.get(k,0) + q
        i += 1
    return menue, groceries
    

def original() :
    """Original attempt, returns a grocery list created as user inputs meal names"""
    while True :
        recipe = input('recipe to add: ').lower()
        if recipe == 'done' : break
        if len(recipe) < 1 : recipe = 'grilled cheese' ###Remove when done, for quicker testing
        ingredients = get_ingredients(recipe)
        if ingredients == False :
            print('Recipe not found. Try again.\n')
            continue
        
        #loop to add ingredients to grocery list.
        for item in ingredients :
            #print(item)
            grocery_list[item] = grocery_list.get(item,0) + 1 #idium: retreive/create/update
    return grocery_list



def grocery_list(menue) :
    """Retuns a grocery list from a menue, using recipe objects"""

        
        #locate the item on other file
        #for each key in ingredients dict, .get(item,o) + 1




x = random_menue(3)
menue = x[0]
groceries = x[1]
print(menue)
print(groceries)
#print(original())
#print(create_menue())




### Future feature: Create seperate grocery lists based on section of the store (Dairy, Meat, Veggie, Pantry, Other)
### (Optional?) Random selection of (4?) recipies rather than inputting your own