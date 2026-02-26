#quarters = 0.25 , dimes = 0.10 , nickles = 0.05 , pennies = 0.01

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

resources["profit"] = 0

espresso_coffee = MENU['espresso']
espresso_ingredients = espresso_coffee["ingredients"]
espresso_ingredients['milk'] = 0

coffee_machine = True
while coffee_machine:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink == 'espresso' or drink == 'latte' or drink == 'cappuccino':
        total_money = 0
        print("Please insert coins.")
        quaters = int(input("How many quaters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickles = int(input("How many nickles? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01

        total_money = round((pennies + nickles + dimes + quaters),2)

        users_coffee = MENU[drink]
        cost_of_coffee = users_coffee['cost']
        coffee_ingredinets = users_coffee['ingredients']


        if coffee_ingredinets["water"] <= resources["water"] and coffee_ingredinets["coffee"] <= resources["coffee"] and coffee_ingredinets["milk"] <= resources["milk"]:

            if total_money >= cost_of_coffee:
                resources["profit"] += cost_of_coffee
               
                resources["water"] = resources['water'] - coffee_ingredinets['water']
                resources["coffee"] = resources['coffee'] - coffee_ingredinets['coffee']
                resources["milk"] = resources['milk'] - coffee_ingredinets['milk']

                if total_money > cost_of_coffee:
                    print(f"Here is your ${total_money - cost_of_coffee} change")

                print(f"Here is your {drink}☕️ Enjoy!")
            else:
                print(f"Not enough money, here is your refund ${total_money}")
        else:
            if coffee_ingredinets["water"] > resources["water"]:
                print("Sorry there is'not enough water")
            elif coffee_ingredinets["coffee"] > resources["coffee"]:
                print("Sorry there is'not enough coffee")
            elif coffee_ingredinets["milk"] > resources["milk"]:
                print("Sorry there is'not enough milk")

    elif drink == 'off':
        coffee_machine = False

    elif drink == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${resources["profit"]}")





