money = 0
drink_data = {"water": {"quantity": 300, "units": "ml"}, "milk": {"quantity": 200, "units": "ml"}, "coffee": {"quantity": 100, "units": "g"}}
recipes = {"espresso": {"water": 50, "coffee": 18}, "latte": {"water": 200, "coffee": 24, "milk": 150}, "cappuccino": {"water": 250, "coffee": 24, "milk": 100}}

def sufficient_quantity(drink):
    drink_requirements = recipes[drink]
    global drink_data
    error_message = False
    for item in drink_data:
        quantity = drink_data[item]["quantity"]
        
        if item == 'water':
            remaining_supply = quantity - drink_requirements["water"]
            if  remaining_supply > 0:
                drink_data[item]["quantity"] -= drink_requirements["water"]
            else:
                print("Sorry there is not enough water.")
                error_message = True
        elif item == 'milk':
            remaining_supply = quantity - drink_requirements["milk"]
            if  remaining_supply > 0:
                drink_data[item]["quantity"] -= drink_requirements["milk"]
            else:
                print("Sorry there is not enough milk.")
                error_message = True
        elif item == 'coffee':
            remaining_supply = quantity - drink_requirements["coffee"]
            if  remaining_supply > 0:
                drink_data[item]["quantity"] -= drink_requirements["coffee"]
            else:
                print("Sorry there is not enough coffee.")
                error_message = True
    
    if error_message == True:
        return False
    else:
        return True        
    
    

    #return True or False


def coffee_machine():

    user_prompt = input("What would you like? (espresso/latte/cappuccino) ")

    if user_prompt == 'report':
        for item in drink_data:
            print(f"{item.title()}: {drink_data[item]['quantity']}{drink_data[item]['units']}")    
        print(f"Money: ${money}")          
    else:
        if sufficient_quantity(user_prompt):
            print("can make drink")
        else:
            print("cannot make drink")        
    
    coffee_machine() 
                
coffee_machine()