data = {"water": {"quantity": 300, "units": "ml"}, "milk": {"quantity": 200, "units": "ml"}, "coffee": {"quantity": 100, "units": "g"}, "money": 0}

def coffee_machine():

    user_prompt = input("What would you like? (espresso/latte/cappuccino) ")

    if user_prompt == 'report':
        for item in data:
            if item == "money":
                print(f"{item}: ${data[item]}")
            else:
                print(f"{item}: {data[item]['quantity']}{data[item]['units']}")

    coffee_machine() 
                
coffee_machine()