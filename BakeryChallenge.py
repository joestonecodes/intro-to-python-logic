ingredient_costs = {
    "flour": 2.5,  # per kg
    "sugar": 1.5,  # per kg
    "butter": 3.0,  # per kg
    "water": 0.01,  # per liter
    "salt": 1,  # per kg
    "yeast": 0.05,  # per oz
    "eggs": 0.2,  # per egg
    "milk": 0.8,  # per liter
    "chocolate_chips": 4.0,  # per kg
    "vanilla_extract": 20,  # per liter
    "baking_powder": 0.02,  # per gram
    "baking_soda": 0.015,  # per gram
    "cinnamon": 0.03,  # per gram
    "raisins": 5.0  # per kg
}

dinner_rolls_recipe = {
    "recipe_name": "Dinner Rolls",
    "flour": 1,  # kg
    "water": 0.3,  # liter
    "yeast": 0.02,  # oz
    "salt": 0.01,  # kg
    "butter": 0.1  # kg
}
cinnamon_raisin_bread = {
    "recipe_name": "Cinnamon Raisin Bread",
    "flour": 0.8,  # kg
    "sugar": 0.1,  # kg
    "butter": 0.1,  # kg
    "milk": 0.5,  # liter
    "yeast": 0.02,  # oz
    "salt": 0.01,  # kg
    "cinnamon": 0.02,  # kg
    "raisins": 0.15  # kg
}

def calculate_total_cost(recipe, ingredient_costs): #recipe is the first dictionary and ingrediants cost or new_ingrediants_cost will be the second dictionary
    recipe_name = recipe["recipe_name"] #brackets reference the value of the key in the brackets
    total_cost = 0 #starts total cost at zero

    for ingredient,amount in recipe.items(): #Gets Keys and values from the recipes dictionary recipe.items will go through all of the items in a dictionary
        if not ingredient == "recipe_name":  #ignore recipe name
            
            #for every ingrediant that is in the recipe dictionary we are finding in the ingrediant_costs dictionary
            #for each of those keys we are finding the values pf the proices from the ingrediants cost dictionary
            ingredient_cost = ingredient_costs[ingredient]
            
            #multiply price by amount from recipe dictionary and add to previous total cost
            total_cost = total_cost + (ingredient_cost * amount) 

    print (f"total cost to make {recipe_name}: ${total_cost:.2f}") 

    return total_cost   #retuns final cost after iteration throught the dictionary

def change_price(ingredient_costs, ingredient_name, change_percent ):
    
    
        ## update the ingredient_costs dictionary
        ## multiply the ingredient's current cost by change_percent
    ingredient_costs[ingredient_name] = ingredient_costs[ingredient_name] * (1 + change_percent) #to change the value you must use the key in this case its the ingrediant name
    #new value is equal to the value plus percentage 

def change_all_prices(ingredient_costs, change_percent):
    new_ingrediant_costs = ingredient_costs.copy() #copies ingredients prices into a new dictionary
    
    for ingrediant,cost in new_ingrediant_costs.items(): # ingrediant is the new key and cost is the new value
        change_price(new_ingrediant_costs, ingrediant, change_percent) #calls the change_price method
      
    return new_ingrediant_costs  #returns new prices

markup_20 = change_all_prices(ingredient_costs, 0.20) #adds 20% to change all prices
markdown_20 = change_all_prices(ingredient_costs, -0.20) #adds -20% to all prices

total_cost = calculate_total_cost(dinner_rolls_recipe, ingredient_costs)
markup_total_cost = calculate_total_cost(dinner_rolls_recipe, markup_20)
markdown_total_cost = calculate_total_cost(dinner_rolls_recipe, markdown_20)


