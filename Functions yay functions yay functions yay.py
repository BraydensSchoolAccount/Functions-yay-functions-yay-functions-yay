# Functions yay 3: Return to be
# Brayden Towner
# 11/13/2023

import os
exercise_int=1

# Just to keep it in one file, I'll use headers and cls to clarify exercises.
# This code repeats a lot
def next_exercise(exercise_name):
    # It tries to grab the local variable with this name which doesn't exist...
    # I knew of this keyword already
    global exercise_int
    # Only pause pre-exercise if this isn't the first
    if exercise_int > 1:
        os.system("pause")
    os.system("cls")
    print(f"Exercise {exercise_int}: {exercise_name}\n")
    exercise_int+=1

def money_owed(item, price, quantity=1):
    """prints how much someone owes based on price and quantity

    Args:
        item (str): The item that is being purchased
        price (float): The price of each item
        quantity (int, optional): The amount of items purchased. Defaults to 1.
    """
    total_cost = price*quantity
    print(f"After purchasing {quantity} {item} at ${price:.2f} each, you owe ${total_cost:.2f}")

def format_name(first_name="", last_name=""):
    """Formalizes names for you

    Args:
        first_name (str, optional): The first name of the user. Defaults to "".
        last_name (str, optional): The last name of the user. Defaults to "".

    Returns:
        str: The full name of the user if defined. Otherwise, it returns Anonymous
    """
    if first_name != "":
        return f"{first_name} {last_name}".rstrip()
    # There's not an else because the if statement returns, so if the function is running beyond that, the condition wasn't met
    print("No name passed in")
    return "Anonymous"

next_exercise("Essentially, I have this totally real 100% off coupon")

money_owed(input("What are you buying? >  "), float(input("How much is it? (USD) >  ")))
money_owed(input("What are you buying? >  "), float(input("How much is it? (USD) >  ")), 2)

next_exercise("What are you a cop?")

print(f"Hi there {format_name('James', 'Cameron')}")
print(f"Hi there {format_name('Greg')}")
print(f"Hi there {format_name()}")

