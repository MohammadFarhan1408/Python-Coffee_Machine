from menu import MENU, resources
profit = 0


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coin():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    user_action = input("What would you like? (espresso/latte/cappuccino):")
    if user_action == 'off':
        is_on = False

    elif user_action == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif user_action == 'refill':
        refill_resources = input("What you want to refill? (Water/Milk/Coffee): ").lower()
        if refill_resources == 'water':
            refill_water = int(input("Please enter amount of water in ml to refill: "))
            resources[refill_resources] += refill_water
        elif refill_resources == 'milk':
            refill_milk = int(input("Please enter amount of milk in ml to refill: "))
            resources[refill_resources] += refill_milk
        elif refill_resources == 'coffee':
            refill_coffee = int(input("Please enter amount of coffee in gm to refill: "))
            resources[refill_resources] += refill_coffee
        else:
            print("Invalid resources")

    else:
        drink = MENU[user_action]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coin()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(user_action, drink['ingredients'])
