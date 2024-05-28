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

def calculate_total_cost(recipe, ingredient_costs):
    recipe_name =recipe["recipe_name"]
    total_cost = 0

    for ingredient,amount in recipe.items():
        if not ingredient == "recipe_name":
            ingredient_cost = ingredient_costs[ingredient]
            total_cost = total_cost +(ingredient_cost * amount)
    print (f"total cost to make {recipe_name}: ${total_cost:.2f}")
    return total_cost   

calculate_total_cost(dinner_rolls_recipe)

total_cost = calculate_total_cost(dinner_rolls_recipe, ingredient_costs)

def change_price(ingredient_costs, ingredient_name, change_percent ):
    ## update the ingredient_costs dictionary
    ingredient_costs[ingredient_name] = ingredient_costs[ingredient_name] * (1 + change_percent)

def change_all_prices(ingredient_costs, change_percent):
    new_ingrediant_costs = ingredient_costs.copy
    for ingrediant,cost in new_ingrediant_costs.items(): 
        change_price(ingredient_costs,ingrediant, change_percent)  
    return new_ingrediant_costs  

markup20 = change_all_prices(ingredient_costs, 1.20)
markup_total_cost
