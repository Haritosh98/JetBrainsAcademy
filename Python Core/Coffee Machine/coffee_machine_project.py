water_input = int(input("Write how many ml of water the coffee machine has:\n"))
milk_input = int(input("Write how many ml of milk the coffee machine has:\n"))
beans_input = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
cups_input = int(input("Write how many cups of coffee you will need:\n"))


def ingredients(cups, water, milk, beans):
    water_amount = 200
    milk_amount = 50
    coffee_beans_amount = 15
    exact_water = water//water_amount

    exact_milk = milk//milk_amount

    exact_beans = beans//coffee_beans_amount

    if cups == 0 and water == 0 or milk == 0 or beans == 0:
        return "Yes, I can make that amount of coffee"
    if exact_water == 0 or exact_milk == 0 or exact_beans == 0:
        return "No, I can make only 0 cups of coffee"
    else:
        total_cups = min([exact_water, exact_milk, exact_beans])

        if total_cups == cups:
            return f"Yes, I can make that amount of coffee"
        elif total_cups > cups:
            return f"Yes, I can make that amount of coffee (and even {total_cups - cups} more than that)"
        else:
            return f"No, I can make only {total_cups} cup{'s' if total_cups > 1 else ''} of coffee"


print(ingredients(cups=cups_input, water=water_input, milk=milk_input, beans=beans_input))
