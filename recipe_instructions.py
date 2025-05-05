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

#instruction_setup()

instructions = {
    'pg 1': {
        'ingredients': {'potato (oz)': 12, 'garlic clove': 2, 'red onion': 1, 'ground beef (#)': 0.6, 'shredded monty jack (oz)': 4, 'potato bun': 2, 'creamy horseradish sauce (tbsp)': 2, 'balsamic vinegar (tsp)': 5},
        'prep': {'potato (oz)': '1/2 inch wedges', 'garlic clove': 'mince', 'red onion': 'Halve, thinly slice'},
        'directions': """
        1.
        Set oven to 425, do prep if needed.
        2.
        Toss potatoes on baking sheet with a drizzle of oil and fry seasoning, salt and pepper. Roast on top rack 20-25 min
        3.
        Heat a drizzle of oil in a large pan. Add onion and cook until brown and softened. Stir in vinegar & 1 tsp sugar and caramelize. Set aside in small bowl.
        4.
        In a small bowl, 2 tsp combine mayo and a pinch of minced garlic. Season with salt and pepper.
        5.
        Shape beef into patties and season (at least w/ salt and pepper). Cook patties in pan /drizzle of oil heated on med-high. Towards the last 1-2 min of cooking, top with cheese and cover pan.
        6.
        Halve and toast buns, spread with garlis mayo and ketchup. Fill with patty and onion jam, serve potatoes on the side.
        """
    },
    'pg 2': {
        'ingredients': {'lime': 1, 'garlic clove': 2, 'peanuts (oz)': 3, 'coleslaw mix (oz)': 6, 'sour cream (oz)': 2, 'ground pork (#)': 0.6, 'sweet thai chili sauce (oz)': 1, 'ponzu sauce (oz)': 2, 'cornstarch (tbsp)': 1, 'taco tortillas': 6},
        'prep': {'lime': 'quarter', 'garlic clove': 'finely chop', 'peanuts (oz)': 'roughly chop'},
        'directions': """
        1.
        Prep if needed
        2.
        In small bowl, combin juice from half the lime, 1/2 tsp sugar, a lil salt, and 1/4 of the coleslaw mix.
        In a separate small bowl combine sour cream, pinch of garlic, (optional lime zest), a lil salt and pepper. Add water 1 tsp at a time until the sauce is a drizzling consistency.
        3.
        Cook port in a pan with a drizzle of oil heated on med-high. Once browned, add salt and pepper and remaining cabbage and garlic. Cook until cabbage is wilted and pork cooked through.
        4.
        Add chili sauce, ponzu, 2tsp cornstarch, 1/3 c water to pork. Cook and stir until thickened (2-3 min).
        5.
        Meanwhile, warm tortillas (wrap in damp paper towel and microwave 30 seconds.)
        divide pork mixture into tortillas, top w/ cabbage slaw, crema, and peanuts
        
        https://www.everyplate.com/recipes/sweet-chili-pork-tacos-60e8549b73705e09bf60c296
        """
    },
    'pg 3': {
        'ingredients': {'garlic clove': 2, 'chicken sausage (#)': 0.6, 'rigatoni (oz)': 6, 'peas (oz)': 10, 'cream sauce base (oz)': 4, 'mushroom stock concentrate': 1, 'garlic powder (tbsp)': 1},
        'prep': {'garlic clove': 'mince', },
        'directions': """1.  *****NOT DONE****
        Boil large pot of water. prep if needed
        """
    },
    'pg 4': {
        'ingredients': {'carrot (oz)': 12, 'side green': 1, 'shallot': 0.5, 'chicken breast (#)': 2, 'chicken stock concentrate': 1, 'dijon mustard (tbsp)': 1, 'apricot jam (tbsp)': 2},
        'prep': {'carrot (oz)': 'Cut in 1/2 inch slices', 'side green': 'prep if needed', 'shallot': 'finely chop'},
        'directions': """
        1.
        Heat oven to 425. Prep if needed.
        2.
        Toss carrots on one side of baking sheet (otherside for side green if needed). Drizzle with oil, salt and pepper. Roast 20-25 minute.
        3.
        place chicken between 2 peices of plastic wrap ad pound with mallet until about 1/3 inch.
        Place 1/4 c flour in shallow disk, press chickin into flour until fully coated.
        Heat 2 tbsp oil in large pan over med-high heat. Add chicken, cook till golden brown and cooked through, then transfer to paper-towel-lined plate.
        4.
        In same pan, heat a drizzle of oil. Add shallot and cook 3-4 min. Whist in stock concentrate, mustard, jam, 1/4c water. Simmer 1-2 min until reduced to a glossy sauce.
        5.
        Turn chicken in sauce to coat, then transfer to cutting board and slice. Plate chicken and sides and spoon remaining sauce over chicken.
        
        https://www.everyplate.com/recipes/apricot-dijon-chicken-6563fe9cac1dddb9ab0e9dab
        
        """
    },
    'pg 5': {
        'ingredients': {'garlic pepper (tsp)': 0.24, 'scallion': 2, 'mushroom seasoning (tsp)': 2, 'shredded cheddar cheese (oz)': 1, 'yukon potato (oz)': 12, 'mirepoix stock concentrate (tsp)': 2, 'cream cheese (oz)': 1, 'steak strips (oz)': 10},
        'prep': {'scallion': 'thinly sliced','yukon potato (oz)': '1/2 inch wedges'},
        'directions': """
        1.
        Heat oven to 425. Prep if needed, keep scallions whites and greens separate
        2.
        Toss potatoes with a drizzle of oil and half mushroom seasoning onto baking sheet. Roast 25-30 min.
        Coursely chop steak strips
        3.
        Toast buns in large pan with 1tsp of oil by placing them cut side down 2-3 min.
        4.
        Once buns are done, add 1stp oil to pan with scallion white, steak strips, and garlic pepper. Cook through.
        Add mirepoix base and 1 tbsp water. Stir occasionally until combined, then set aside to rest.
        5.
        Heat med pan on med-low. Add cream cheese and 1/4 c water until fully melted. Add shredded cheese and salt.
        6.
        Plate: bottom bun topped with steak strips then cheese sauce then scallion greens.
        
        https://www.homechef.com/meals/beef-cheddar-melt?srsltid=AfmBOopkZmprulBIMUggYrAZnwy_o5TAq0aEqh6RMfke_Aso3zdCSdfj
        
        """
    },
    'pg 6': {
        'ingredients': {'red pepper flakes (tsp)': 0.25, 'garlic salt (tsp)': 0.5, 'butter (tbsp)': 1, 'sour cream (oz)': 2, 'russet potato (oz)': 10, 'side green': 1, 'bbq spice rub (tsp)': 1, 'boneless pork chop': 2},
        'prep': {'sour cream (oz)': 'see cookbook', 'russet potato (oz)': 'see cookbook', 'side green': 'see cookbook', 'boneless pork chop': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 7': {
        'ingredients': {'peas (oz)': 10, 'red pepper flakes (tsp)': 0.25, 'cream cheese (oz)': 1, 'scallion': 2, 'goat cheese (oz)': 1, 'grated parmesan (oz)': 0.5, 'penne pasta (oz)': 5, 'flour (oz)': 0.25, 'marinara sauce (oz)': 4, 'italian pork sausage (#)': 0.75},
        'prep': {'scallion': 'slice thinly, separate whites and greens','penne pasta (oz)': 'follow box directions',},
        'directions': """
        1.
        Set medium pot of water on to boil. Prep if needed.
        Save 1c pasta water when pasta is done
        2.
        Cook italian sausage and scallion whites in pan w/ lil oil heated on med-high heat.
        3.
        Make sauce-- Add flour to pan and stir into meat. Add 3/4 c pasta water, marinara, cream cheese, S&P.
        Simmer 2-4 min until thickened (add extra pasta water if too thick).
        4.
        Stir in peas, S&P, pasta, and parmesan until cheese is melted. Remove from burner.
        dish and top with scallion greens, and goat cheese crumbles, red pepper flakes.
        
        https://www.homechef.com/meals/creamy-tomato-and-italian-sausage-penne-0ed0e1ef-d781-4a79-a7a4-e8626faaff12?srsltid=AfmBOoqM-PXE3mPmbbMWzWrc8ycIE1Ikmxa9UWjfLjWDg1fa1zZ5wliY
        
        """
    },
    'pg 8': {
        'ingredients': {'roma tomato': 1, 'lime': 0.5, 'yellow onion': 0.5, 'tex-mex paste (oz)': 1, 'jasmine rice': 1, 'black bean can (oz)': 10, 'cream cheese (oz)': 1, 'burrito tortilla': 2, 'guacamole': 1},
        'prep': {'roma tomato': 'Dice small', 'yellow onion': 'dice, divided', 'lime': 'quarter', 'guacamole': 'see cookbook'},
        'directions': """
        1.
        Prep. Combine 2 TBSP diced onion, squeeze of lime, tomato, lil oil, S&P in small bowl.
        2.
        In sm pot, combine rice, half tex-mex paste, water (according to rice directions), salt.
        Bring to a boil, cover, reduce to simmer. Cook according to directions, likely 18-20 min.
        Cook beef in med pot over med-high heat. Set aside when done and wipe out pan.
        3.
        Heat lil oil in a med pot over med-high heat. Add remaining onion, S&P and brown.
        Add beans AND their liquid, 1tbsp butter, heat till warmed through. Set aside and cover to keep warm.
        4.
        In same pot, meld 1 tbsp butter on med-high heat. Whisk in 1 tbsp flour, stirring till lightly browned.
        whisk in cream cheese, 1/2 c water and Tex-Mex paste.
        Cook until sauce has thickened and cream cheese is melted in.
        5.
        Drain beans. Fill tortilla with rice, beans, meat. Top with guac and roll up.
        6.
        Melt 1 tbsp butter in large pan over med-high heat. Add burritoes seam side down until crispy/golden.
        Plate burritos, drizzle with Tex-Mex, garnish with pico (step 1), serve with remaining rice and beans.
        
        https://www.everyplate.com/recipes/crispy-beef-and-bean-burritos-64e4e440d47578530b7e6df4
        
        """
    },
    'pg 9': {
        'ingredients': {'ground beef (#)': 0.5, 'jasmine rice': 1, 'garlic clove': 3, 'carrot (oz)': 3, 'mini cucumber': 1, 'sriracha': 1, 'ponzu sauce (oz)': 4, 'lime': 1, 'yellow onion': 1, 'scallion': 1},
        'prep': {'garlic clove': 'minced, divided', 'carrot (oz)': 'grated', 'mini cucumber': 'half slices', 'lime': 'quarter', 'yellow onion': 'diced', 'scallion': 'Slice thinley, keeping whites and greens separate'},
        'directions': """
        1.
        Start rice according to directions (bring to boil, cover and reduce to simmer likely 15-20 min)
        2.
        Prep if needed while rice cooks
        3.
        In med bowl, combine cucumber, half lime juice, 1/4 tsp sugar, pinch of salt. Set aside to pickle.
        In small bowl combine 2 TSBP mayo, squeeze of lime, pinch of garlic, sriracha according to taste, S&P.
        4.
        When rice has cooked 15 min, heat lil oil in a large pan over med/high heat. Add onion, scallion whites and cook a few minutes.
        Add beef, remaining garlic, 2 tsp sugar and cook. Stir in ponzu and S&P according to taste.
        5.
        Fluff rice with a fork, stir in 1 TBSP butter lil salt. Divide between bowls top w/ beef, cucumbers, and carrot.
        Top scallion greens and drizzle Sriracha aioli.
        
        https://www.hellofresh.com/recipes/sweet-umami-beef-bowls-67520f8f53225fdd9d2bd278
        
        """
    },
    'pg 10': {
        'ingredients': {'parsley bunch': 1, 'garlic clove': 1, 'potato (oz)': 12, 'sliced almonds (oz)': 1, 'ranch steak': 2, 'green beans (oz)': 12},
        'prep': {'parsley bunch': 'finely chopped', 'garlic clove': 'minced, divided', 'potato (oz)': 'sliced into 1/4 inch rounds'},
        'directions': """
        1.
        Preheat oven to 450. Prep if needed.
        Microwave 2 TBSP butter until softened, Stir in parlsey, pinch of salt, pinch of garlic.
        2.
        Toss potato rounds with 1 TBSP oil, S&P, spread evenly on baking sheet and raost about 20 min.
        3.
        Heat a large pan over med/high heat, Add almonds and cook until toasted (about 5-6 min)
        4.
        Season steak w/ S&P. Heat 1 TBSP oil in same pan as step 3.
        Add steak and cook until browned and done to desired doneness. Transfer to cutting board to rest.
        5.
        Add green beans to same pan, cook on med, stirring until bright green (about 2 min).
        Pour in 1/4 c water and cover pan. Let steam until tender (about 3 min). Season w/ S&P.
        6.
        Thinly slice steak against the grain. Divid steak, beans, potatoes between plates.
        Sprinkly beans w/ almonds to taste. Dollop steak w/ butter mix, garnish w/ extra parsley.
        
        https://www.everyplate.com/recipes/week-31-hotel-butter-steak-5c9e3ea2c445fa5dd7138e32
        
        """
    },
    'pg 11': {
        'ingredients': {'pablano': 1, 'scallion': 1, 'garlic clove': 1, 'roma tomato': 1, 'cornstarch (tbsp)': 1, 'tex-mex paste (oz)': 1, 'southwest spice': 1, 'black bean can (oz)': 10, 'taco tortillas': 6, 'shredded monty jack (oz)': 3},
        'prep': {'pablano': 'halve and thinly slice', 'scallion': 'Thinly slice, keeping white and greens seperate', 'garlic clove': 'minced', 'roma tomato': 'dice 1/2 inch', 'black bean can (oz)': 'see cookbook'},
        'directions': """
        1.
        Preaheat oven to 425. Prep if needed.
        2.
        In med bowl, whisk half cornstarch, half Tex-Mex paste, and 1/2 c hot water.
        Mix until smooth, microwave  until thickened until consistency of gravy (30 sec). 
        3.
        Heat lil oil in large pan over med/high. Add pepper and cook 4-5 min. Add scallion whites and garlic, cook 1 min.
        Add tomato, southwest spice, remaining Tex-Mex paste and stir to coat.
        Add black beans AND their liquid, 1 tsp salt. Stir to combine and cook until beans are saucy (3-4 min).
        4.
        Place a small amount of fillinf on hald of each tortilla. Roll up starting with filled side and place seam side down in baking dish (8x8).
        5.
        Pour Tex-Mex sauce over enchiladas to thoroughly coat, sprinkly w/ cheese and bake until sauce is bubbling and cheese is melted (3-5 min)
        6.
        Plate enchiladas and top with scallions.
        
        https://www.hellofresh.com/recipes/spicy-tex-mex-black-bean-enchiladas-646b686512455b7f40092a92
        
        """
    },
    'pg 12': {
        'ingredients': {'roma tomato': 1, 'garlic clove': 2, 'linguine': 1, 'italian pork sausage (#)': 0.5, 'italian seasoning': 1, 'cream cheese (oz)': 1, 'chicken stock concentrate': 1, 'cream sauce base (oz)': 4, 'ciabatta': 1},
        'prep': {'roma tomato': '1/2 inch dice', 'garlic clove': 'mince'},
        'directions': """
        1.
        Preheat oven to 425. Start a large pot of water to boil. Set out 1 TBSP butter to warm up.
        prep if needed. Start on step 5 whenever you are waiting for something to heat/cook.
        2.
        Once water boild, add pasta and cook according to box directions (likely 9-11 min for al dente).
        Reserve 1 c pasta water when draining.
        3.
        Cook sausage in pan heated w/ lil oil over med/high heat. Cook with tomato, half garlic, 2 tsp italian seasoning, S&P.
        4.
        Add 1 TBSP butter and 2 tsp flour, stir until mixed. Reduce heat to med and add cream cheese, cream sauce base (wing it if from scratch), 1/4 c pasta water, S&P.
        Cook until thickened (1-2 min) **Good time to start step 5. You can add chili flakes now if you want it a little spicy.
        Add drained pasta and toss until coated
        5. Combine softened butter, remaining garlic, pinch of salt, 1/2 tsp italian seasoning in a small bowl.
        Halve ciabatta, spread w/ butter mix, toast on top rack 3-5 min
        6.
        Halve garlic bread on diagonal. Divide pasta and bread between bowls.
        
        https://www.hellofresh.com/recipes/tomato-pork-sausage-linguine-643ea752abfb4b673a0e2119
        
        """
    },
    'pg 13': {
        'ingredients': {'chipotle pesto (tbsp)': 1, 'mirepoix stock concentrate (tsp)': 2, 'sour cream (oz)': 1, 'yellow onion': 0.5, 'pepper': 1, 'lime': 1, 'taco tortillas': 6, 'fajita seasoning (tsp)': 2, 'sliced pork (#)': 0.6},
        'prep': {'yellow onion': 'sliced', 'pepper': 'sliced', 'lime': 'quartered'},
        'directions': """
        
        https://www.homechef.com/meals/sizzling-chipotle-pork-tacos?srsltid=AfmBOopEtLiZEpUgO0ooOLs4Jz2McUJMrhXQ5JzXMtJiQwk8zw04Hz3a
        
        """
    },
    'pg 14': {
        'ingredients': {'potato (oz)': 12, 'green beans (oz)': 12, 'garlic clove': 1, 'pork chop': 2, 'balsamic vinegar (oz)': 1, 'cherry jam (tbsp)': 3, 'chicken stock concentrate': 1, 'soy sauce (oz)': 1},
        'prep': {'potato (oz)': '1/2 inch wedges', 'green beans (oz)': 'trimmed', 'garlic clove': 'minced'},
        'directions': """
        
        https://www.hellofresh.com/recipes/saucy-cherry-balsamic-pork-chops-645134926a3fb8d2c704e72b
        
        """
    },
    'pg 21': {
        'ingredients': {'shredded mozzarella (oz)': 2, 'red pepper flakes (tsp)': 0.25, 'grated parmesan (oz)': 2, 'marinara sauce (oz)': 8, 'baby spinach (oz)': 5, 'bolognese meat sauce (oz)': 12, 'gemelli pasta (oz)': 6},
        'prep': {'bolognese meat sauce (oz)': 'Make w/ sausage or ground meat of choice'},
        'directions': """
        
        https://www.homechef.com/meals/lasagna-style-beef-and-pork-bolognese-gemelli?srsltid=AfmBOoqOtSuNQst_0QdxmgjsEX7AmUcxdjIFNQedDU2e9pGulJjGhfBn
        
        """
    },
    'pg 15': {
        'ingredients': {'garlic clove': 2, 'yellow onion': 1, 'celery stalk': 1, 'italian seasoning': 1, 'tomato paste (oz)': 2, 'chicken stock concentrate': 1, 'mushroom stock concentrate': 1, 'cream cheese (oz)': 1, 'ciabatta': 1, 'carrot (oz)': 3, 'italian pork sausage (#)': 0.4},
        'prep': {'garlic clove': 'mince', 'yellow onion': 'finely chopped', 'celery stalk': 'thinley sliced', 'carrot (oz)': 'diced'},
        'directions': """
        
        https://www.everyplate.com/recipes/creamy-couscous-pork-sausage-soup-63b48f568411c07ee20741e8
        
        """
    },
    'pg 16': {
        'ingredients': {'red bell pepper': 1, 'garlic clove': 1, 'cavatappi pasta (oz)': 1, 'chicken sausage (#)': 0.5, 'tomato paste (oz)': 1, 'garlic powder (tbsp)': 1, 'cream sauce base (oz)': 4},
        'prep': {'red bell pepper': 'Halved', 'garlic clove': 'peeled, whole', 'cream sauce base (oz)': 'roux based cream sauce'},
        'directions': """
        
        https://www.everyplate.com/recipes/creamy-tomato-chicken-sausage-cavatappi-67f297af23aa2ac244887e59?week=2025-W19
        
        """
    },
    'pg 17': {
        'ingredients': {'side green': 1, 'garlic clove': 1, 'italian seasoning': 1, 'panko (c)': 0.25, 'ciabatta': 1, 'chicken breast (#)': 0.6, 'sour cream (oz)': 1, 'marinara sauce (oz)': 3, 'shredded monty jack (oz)': 2},
        'prep {'side green': 'prep as needed', 'garlic clove': 'minced'},
        'directions': """
        
        https://www.everyplate.com/recipes/chicken-parm-6796fe23183b5afa145041da
        
        """
    },
    'pg 18': {
        'ingredients': {'enchilada sauce (oz)': 5, 'corn (oz)': 5, 'black bean can (oz)': 15, 'jalapeno': 1, 'red onion': 1, 'pablano': 1, 'taco seasoning (tsp)': 2, 'taco tortillas': 6, 'shredded white cheddar cheese (oz)': 2, 'sour cream (oz)': 2},
        'prep': {'enchilada sauce (oz)': 'see cookbook', 'corn (oz)': 'see cookbook', 'black bean can (oz)': 'see cookbook', 'jalapeno': 'see cookbook', 'red onion': 'see cookbook', 'pablano': 'see cookbook', 'taco seasoning (tsp)': 'see cookbook', 'taco tortillas': 'see cookbook', 'shredded white cheddar cheese (oz)': 'see cookbook', 'sour cream (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'R_1': {
        'ingredients': {'cream of chicken soup (can)': 1, 'tuna in water canned': 1, 'peas (oz)': 10, 'egg noodles': 1},
        'prep': {'cream of chicken soup (can)': 'see cookbook', 'tuna in water canned': 'see cookbook', 'peas (oz)': 'see cookbook', 'egg noodles': 'see cookbook'},
        'directions': """
        
        Ask Rowan or look in his cookbook
        
        """"
    },
    'pg 19': {
        'ingredients': {'potato (oz)': 12, 'tomato paste': 4, 'garlic clove': 2, 'carrot (oz)': 3, 'celery stalk': 1, 'yellow onion': 1, 'dried thyme': 1, 'chicken stock concentrate': 1, 'sour cream (oz)': 1},
        'prep': {'potato (oz)': 'diced, 1/2 inch', 'garlic clove': 'minced', 'carrot (oz)': 'halved and sliced', 'celery stalk': 'sliced', 'yellow onion': 'diced'},
        'directions': """
        
        https://www.hellofresh.com/recipes/pub-style-chicken-shepherds-pie-66cf65c9df3b8ec6a279e138
        
        """
    },
    'pg 20': {
        'ingredients': {'pablano': 1, 'taco seasoning (tsp)': 1, 'salsa verde (oz)': 12, 'scallion': 2, 'taco tortillas': 6, 'sour cream (oz)': 2, 'shredded mexican cheese blend (oz)': 2, 'cream cheese (oz)': 1},
        'prep': {'pablano': 'Halved and sliced into strips', 'scallion': 'Thinly slices, keeping greens and whites separate'},
        'directions': '"""

        https://www.homechef.com/meals/pulled-chicken-salsa-verde-taquitos?srsltid=AfmBOop3ZJ1bMVjaGyvvFg4YABvPwwmSw02bKDw7dpSgyzTIiLL7E8de

        """
    },
    'pg 23': {
        'ingredients': {'basil pesto (oz)': 2, 'red pepper flakes (tsp)': 0.25, 'cream cheese (oz)': 1, 'chicken stock concentrate': 1, 'grated parmesan (oz)': 2, 'cooked chicken breast (#)': 1, 'cream sauce base (oz)': 4, 'grape tomatoes (oz)': 4, 'penne pasta (oz)': 5},
        'prep': {'cooked chicken breast (#)': 'Cook if needed', 'cream sauce base (oz)': 'from a Roux if from scratch', 'penne pasta (oz)': 'Cook based on box directions'},
        'directions': """

        https://www.homechef.com/meals/creamy-basil-pesto-chicken-pasta-4a22fd05-830d-4e57-a2ff-018288aec452?srsltid=AfmBOopRNAYwRKj4dlCPUDUkoxRurqmnRRLs8_1-hanf8zPDf6oZ0CT_

        """
    },
    'pg 24': {
        'ingredients': {'potato (oz)': 10, 'green bell pepper': 1, 'yellow onion': 1, 'fry seasoning (tsp)': 3, 'bread (slice)': 1, 'ground beef (#)': 0.5, 'shredded pepper jack (oz)': 2, 'dijon mustard (tbsp)': 1},
        'prep': {'potato (oz)': '1/2 inch wedges', 'green bell pepper': 'Halved and thinly sliced', 'yellow onion': 'Haled and thinly sliced'},
        'directions': """

        https://www.everyplate.com/recipes/smothered-and-stuffed-meatloaves-65cf6d9bb3001828bde57a28

        """
    },
    'pg 25': {
        'ingredients': {'roma tomato': 1, 'yellow onion': 1, 'lime': 0.5, 'garlic clove': 2, 'sour cream (oz)': 1, 'ground pork (#)': 0.7, 'southwest spice': 1, 'chicken stock concentrate': 1, 'taco tortillas': 6, 'shredded monty jack (oz)': 2},
        'prep': {'roma tomato': 'Diced', 'yellow onion': 'Diced', 'lime': 'Quartered', 'garlic clove': 'Minced'},
        'directions': """

        https://www.hellofresh.com/recipes/southwest-pork-flautas-6462745106d34c35d66b7c7c

        """
    },
    'pg 26': {
        'ingredients': {'yellow onion': 1, 'garlic clove': 2, 'potato (oz)': 12, 'jalapeno': 1, 'corn (oz)': 10, 'chicken stock concentrate': 1, 'cream cheese (oz)': 2, 'sour cream (oz)': 4},
        'prep': {'yellow onion': 'Diced', 'garlic clove': 'Minced', 'potato (oz)': 'Diced, 1/2 inch', 'jalapeno': 'Finely chopped', 'corn (oz)': 'Drain and rinse if canned'},
        'directions': """

        https://www.everyplate.com/recipes/creamy-corn--bacon-chowder-64edf66813ca23109fd563e4

        """
    },
    'pg 27': {
        'ingredients': {'jasmine rice': 1, 'green bell pepper': 1, 'ginger (nub)': 1, 'scallion': 1, 'garlic clove': 1, 'peanuts (oz)': 1, 'ground beef (#)': 0.5, 'sweet soy glaze (oz)': 2},
        'prep': {'green bell pepper': 'Diced, 1 inch', 'ginger (nub)': 'Finely chopped', 'scallion': 'Thinly sliced, keeping whites and greens separated', 'garlic clove': 'Minced', 'peanuts (oz)': 'Roughly chopped'},
        'directions': """

        https://www.everyplate.com/recipes/kung-pao-beef-bowls-60141ffb9597422b24504bc4

        """
    },
    'pg 28': {
        'ingredients': {'potato (oz)': 10, 'yellow onion': 1, 'roma tomato': 1, 'southwest spice': 1, 'chicken breast (#)': 0.7, 'burrito tortilla': 2},
        'prep': {'potato (oz)': 'see cookbook', 'yellow onion': 'see cookbook', 'roma tomato': 'see cookbook', 'southwest spice': 'see cookbook', 'chicken breast (#)': 'see cookbook', 'burrito tortilla': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 29': {
        'ingredients': {'chili garlic sauce (tsp)': 1, 'panko (c)': 0.13, 'toasted sesame oil (oz)': 0.25, 'sweet and sour sauce': 1, 'garlic sesame sauce (oz)': 1, 'peanuts (oz)': 0.5, 'green beans (oz)': 12, 'asian garlic, ginger, & chile seasoning (tsp)': 1, 'ground pork (#)': 0.7},
        'prep': {'peanuts (oz)': 'Roughly chopped', 'green beans (oz)': 'Trim if needed'},
        'directions': """

        https://www.homechef.com/meals/general-tso-s-pork-meatballs-standard?srsltid=AfmBOooHFEO6mOupDoVtnPuL1OBF8CnB0xu7ccMUrn-RWqC0mjn44dPg

        """
    },
    'pg 30': {
        'ingredients': {'spaghetti (oz)': 5, 'lemon': 1, 'flour (oz)': 1, 'grated parmesan (oz)': 0.5, 'chicken cutlet (#)': 0.7, 'roasted garlic and herb butter (oz)': 0.75, 'capers (oz)': 0.5, 'butter (oz)': 0.6, 'garlic pepper (tsp)': 2, 'shallot': 1},
        'prep': {'lemon': 'Halved', 'roasted garlic and herb butter (oz)': 'Mix up if needed', 'shallot': 'Halved and thinly sliced'},
        'directions': """

        https://www.homechef.com/meals/classic-chicken-cutlet-piccata?srsltid=AfmBOopNegQ_R8LcxdaB8m0peiXkilN8t6xbtsq0Zc0QGm-dtmP7gQC8

        """
    },
    'pg 31': {
        'ingredients': {'chile and cumin rub (tsp)': 1, 'jasmine rice': 1, 'jalapeno': 1, 'lime': 1, 'adobo seasoning (tsp)': 1, 'chile lime butter (oz)': 0.8, 'shallot': 1, 'pineapple chunks (oz)': 2, 'corn (oz)': 3, 'steak strips (#)': 0.7},
        'prep': {'jalapeno': 'Halve, seed, mince', 'lime': 'halve and juice', 'shallot': 'Minced', 'pineapple chunks (oz)': '1/4 in dice', 'corn (oz)': 'drain if canned'},
        'directions': """

        https://www.homechef.com/meals/chile-lime-sliced-steak-rice-bowl?srsltid=AfmBOoqtmi54Zy5mYHSls5i5yjSVeCg4EPs7OJr7MIRnvcnYHO_8mKn8

        """
    },
    'pg 32': {
        'ingredients': {'yukon gold potato (oz)': 10, 'italian pork sausage (#)': 0.5, 'red bell pepper': 1, 'garlic powder (tbsp)': 0.5, 'dijon mustard (tbsp)': 1, 'ketchup': 1, 'italian seasoning': 1, 'yellow onion': 1, 'demi-baguette': 2, 'chicken stock concentrate': 1, 'shredded mozzarella (oz)': 3},
        'prep': {'yukon gold potato (oz)': '1/2 in wedges', 'red bell pepper': 'Thinly sliced', 'yellow onion': 'Halve and slice', 'demi-baguette': 'Cut like a hotdog bun'},
        'directions': """

        https://www.hellofresh.com/recipes/italian-pork-sausage-and-pepper-subs-5d8122173d53df49934db0cb

        """
    },
    'pg 33': {
        'ingredients': {'corn (oz)': 3, 'scallion': 2, 'roma tomato': 1, 'pot-roast seasoning (tsp)': 1.5, 'arborio rice (oz)': 3.6, 'grated parmesan (oz)': 2, 'sour cream': 2, 'beef demi-glace (tsp)': 2, 'steak strips (#)': 0.7},
        'prep': {'scallion': 'Thinly slice', 'roma tomato': 'Coarsely chop'},
        'directions': """

        https://www.homechef.com/meals/corn-and-steak-strip-risotto?srsltid=AfmBOoqYoESnPqQQ5HrtA7ZnfbE5UHpKBDCiftRCVgdZdOA78L47lN_f


        """
    },
    'pg 34': {
        'ingredients': {'cream cheese (oz)': 1.5, 'yellow onion': 1, 'garlic clove': 2, 'potato (oz)': 12, 'kale': 1, 'chicken sausage (#)': 0.5, 'chicken stock concentrate': 1, 'italian seasoning': 1, 'sour cream (oz)': 2},
        'prep': {'cream cheese (oz)': 'Set out to warm', 'yellow onion': 'Dice', 'garlic clove': 'Mince', 'potato (oz)': 'Dices small', 'kale': 'Remove large stems, chop roughly'},
        'directions': """

        https://www.hellofresh.com/recipes/hearty-chicken-sausage-and-kale-soup-6463942e8ab1333a8ca24bdd

        """
    },
    'pg 35': {
        'ingredients': {'shredded red cabbage (oz)': 3, 'scallion': 2, 'cornstarch (tbsp)': 0.25, 'soy sauce (oz)': 0.2, 'brown stir fry sauce': 4, 'asian noodles (oz)': 10, 'sliced pork (#)': 0.7, 'sesame seeds (tsp)': 1, 'hot sauce (oz)': 0.25},
        'prep': {'scallion': 'Thinly slice, keep whites and greens separated'},
        'directions': """

        https://www.homechef.com/meals/sliced-pork-lo-mein?srsltid=AfmBOoqedORhPH3aJ6YhDDW43-YNeE3WZebdplX4OI3Y4MlxLucwj-bX

        """
    },
    'pg 36': {
        'ingredients': {'potato (oz)': 12, 'pablano': 1, 'red onion': 1, 'lime': 1, 'bbq sauce (oz)': 2, 'sour cream (oz)': 1, 'ground beef (#)': 0.5, 'shredded cheddar cheese (oz)': 1},
        'prep': {'potato (oz)': 'see cookbook', 'pablano': 'see cookbook', 'red onion': 'see cookbook', 'lime': 'see cookbook', 'bbq sauce (oz)': 'see cookbook', 'sour cream (oz)': 'see cookbook', 'ground beef (#)': 'see cookbook', 'shredded cheddar cheese (oz)': 'see cookbook'},
        'directions': 'see cookbook'
    },
    'pg 37': {
        'ingredients': {'potato': 10, 'yellow onion': 1, 'garlic clove': 1, 'demi-bagguette': 2, 'italian pork sausage (#)': 0.4, 'marinara sauce (oz)': 6, 'shredded monty jack (oz)': 3},
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
    'pg 40': {
        'ingredients': {'roma tomato': 1, 'yellow onion': 1, 'lime': 1, 'garlic cloves': 2, 'ground beef (#)': 0.5, 'southwest spice blend': 1, 'beef stock concentrate': 1, 'taco tortillas': 6, 'shredded mozzarella (oz)': 3},
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
