from logo import logo
print(logo)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 50,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order):
    """Check if enough resources are available to make the drink."""
    for item in MENU[order]["ingredients"]:
        if resources[item] < MENU[order]["ingredients"][item]:
            print(f"Sorry, there's not enough {item}.")
            return False
    return True


def process_payment(cost):
    """Process the payment and check if the customer has inserted enough money."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

    if total >= cost:
        change = round(total - cost, 2)
        if change > 0:
            print(f"Here is your change: ${change}")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(order):
    """Deduct the required ingredients from the resources and make the coffee."""
    for item in MENU[order]["ingredients"]:
        resources[item] -= MENU[order]["ingredients"][item]
    print(f"Here is your {order}. Enjoy!")


def report():
    """Print a report of the current resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")


def machine():
    print("Welcome to the Coffee Machine!")
    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order in MENU:
            if check_resources(order):
                if process_payment(MENU[order]["cost"]):
                    make_coffee(order)
        elif order == "report":
            report()
        elif order == "off":
            print("Turning off the machine. Goodbye!")
            break
        else:
            print("Invalid input, please try again.")


machine()
