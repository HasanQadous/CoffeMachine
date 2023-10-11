def game():
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "milk":100,
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
        "Cash": 0
    }

    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    def cost(drink):
        x = MENU[drink]["cost"]
        return x

    def check(user_choice_cost, inserted):
        if inserted >= user_choice_cost:
            change = inserted_coins - user_choice_cost
            return print(f'Here is a ${change} change!\nHere is ur {user_choice}')
        elif user_choice_cost > inserted:
            return print('Sorry! u did not insert enough coins, Here is ur refund')

    trial = ["water", "milk" , "coffee"]

    def material_count(machine_resourses, drink):
        for x in trial:
            if machine_resourses[x] < MENU[drink]["ingredients"][x]:
                print('Sorry no enough material')
                return False
            else:
                machine_resourses["water"] -= MENU[drink]["ingredients"]["water"]
                machine_resourses["milk"] -= MENU[drink]["ingredients"]["milk"]
                machine_resourses["coffee"] -= MENU[drink]["ingredients"]["coffee"]
                return machine_resourses

    coffee_machine = True
    while coffee_machine:
        user_choice = input('What would you like? (espresso/latte/cappuccino):')
        if resources != False:
            if user_choice == 'report':
                print(resources)
                user_choice = input('What would you like? (espresso/latte/cappuccino):')
                resources = material_count(resources, user_choice)
            else:
                user_choice = input('What would you like? (espresso/latte/cappuccino):')
                resources = material_count(resources, user_choice)
                if resources != False:
                    cost_of_drink = cost(user_choice)
                    print('Please insert coins!')
                    inserted_coins = (float(input('how many quarters?')) * quarters + float(input('how many dimes?')) * dimes +
                                     float(input('how many nickels?')) * nickles + float(input('how many pennies?')) * pennies)
                    w = round(inserted_coins)
                    resources["Cash"] += cost_of_drink
                    check(cost_of_drink, w)

                    on_off = input('do u want to turn off the machine?')

                    if on_off == 'yes':
                        coffee_machine = False
                else:
                    coffee_machine = False

game()
