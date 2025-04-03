def get_ingredients(recipe) :
    if recipe == 'grilled cheese' :
        add_to_list = {'bread loaf' : 0.5, 'cheese block' : 0.5, 'butter stick' : 0.5}
   
    elif recipe == 'toast' :
        add_to_list= {'bread loaf' : 0.5, 'butter stick' : 0.5, 'peanut butter tbsp' : None}
   
    elif recipe == 'spaghetti' :
        add_to_list = {'marinara jar' : 1, 'spaghetti box' : 0.5, 'italian sausage pound' : 0.5}
   
    return add_to_list