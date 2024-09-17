coffee = 100
water = 300
milk = 200
money = 0
continuing = True

def espresso():
    global coffee
    global water
    espresso_success = False

    # if enough ingredients, print statement and call payment
    if coffee >= 18 and water >= 50:
        print("\nEspresso chosen. Please begin inserting $1.50 in coins.")
        espresso_success = True
        espresso_success = payment(1.5, "espresso")
    else:
        print("\nSorry, but there is not enough ingredients to craft an espresso. Please contact an employee.")

    # if payment succeeded, deduct ingredients from global variables
    if espresso_success:
        coffee -= 18
        water -= 50

def latte():
    global coffee
    global water
    global milk
    latte_success = False

    # if enough ingredients, print statement and call payment
    if coffee >= 24 and water >= 200 and milk >= 150:
        print("\nLatte chosen. Please begin inserting $2.50 in coins.")
        latte_success = True
        latte_success = payment(2.5, "latte")
    else:
        print("\nSorry, but there is not enough ingredients to craft an espresso. Please contact an employee.")
    
    # if payment succeeded, deduct ingredients from global variables
    if latte_success:
        coffee -= 24
        water -= 200
        milk -= 150

def cappuccino():
    global coffee
    global water
    global milk
    cappuccino_success = False
    
    # if enough ingredients, print statement and call payment
    if coffee >= 24 and water >= 250 and milk >= 100:
        print("\nCappuccino chosen. Please begin inserting $3.00 in coins.")
        cappuccino_success = True
        cappuccino_success = payment(3, "cappuccino")
    else:
        print("\nSorry, but there is not enough ingredients to craft a cappuccino. Please contact an employee.")
    
    # if payment succeeded, deduct ingredients from global variables
    if cappuccino_success:
        coffee -= 24
        water -= 250
        milk -= 100

def report():
    global coffee
    global water
    global milk
    global money
    print(f"\nEarnings and Ingredients:")
    print(f"   Money: $%.2f\n   Coffee grounds: {coffee} g\n   Water: {water} ml\n   Milk: {milk} ml" % money)

def request(command):
    match command:
        case "report":
            report()
        case "espresso" | "e":
            espresso()
        case "latte" | "l":
            latte()
        case "cappuccino" | "c":
            cappuccino()
        case "off":
            global continuing
            continuing = False

def payment(price, beverage):
    global money
    continuing = True

    while continuing:
        quarters = input("How many quarters? ")
        dimes = input("How many dimes? ")
        nickels = input("How many nickels? ")
        pennies = input("How many pennies? ")

        # list for quick if comparison
        inputs = [quarters, dimes, nickels, pennies]

        # all are numeric, assign change values to inputs
        if all(inp.isnumeric() for inp in inputs):
            quarters = int(quarters) * 0.25
            dimes = int(dimes) * 0.1
            nickels = int(nickels) * 0.05
            pennies = int(pennies) * 0.01
            continuing = False
        else:
            print("\nOne or more of your coins is not recognized. Please re-insert your coins.")

    total = quarters + dimes + nickels + pennies
    
    # updating money and returning success boolean
    if total < price:
        print("\nSorry. That isn't enough money to purchase your beverage. Money refunded.")
        return False
    elif total == price:
        money += total
        print(f"\nHere is your {beverage}. Enjoy!")
        return True
    else:
        money += price
        change = total - price
        print(f"\nHere is $%.2f in change and your {beverage}. Enjoy!" % change)
        return True
    

while continuing:
    command = input("\nWould you like an espresso, latte, or cappuccino? ").lower()

    # the "report" and "off" commands are known by managers only
    if command in ("report", "espresso", "latte", "cappuccino", "off"):
        request(command)
    else:
        print("Invalid input.")
        continuing = False