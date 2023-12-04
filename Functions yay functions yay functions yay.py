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
    if first_name:
        return f"{first_name} {last_name}".rstrip()
    # There's not an else because the if statement returns, so if the function is running beyond that, the condition wasn't met
    print("No name passed in")
    return "Anonymous"

def emc_squ(mass, c=299800000):
    """Gets the energy of a mass

    Args:
        mass (float): mass of the object in kg
        c (int, optional): Constant speed of light. Defaults to 2.998*10^8.

    Returns:
        float: The energy of the object in J
    """
    return mass*(c**2)

def student_messenger(name="", grade_level="", school=""):
    """Greet the students

    Args:
        name (str, optional): Name of the student. Defaults to "".
        grade_level (str, optional): Grade of the student, the one we don't obsess over. Defaults to "".
        school (str, optional): Our families name :). Defaults to "".

    Returns:
        str: the greeting
    """
    if name and grade_level and school:
        return f'Hello {name} from {school}! Welcome to another day in grade {grade_level}!'
    if name and grade_level:
        return f'Hello {name}! Welcome to another day in grade {grade_level}!'
    if name and school:
        return f'Hello {name} from {school}!'
    if grade_level and school:
        return f'Hello from {school}! Welcome to another day in grade {grade_level}!'
    if grade_level:
        return f'Hello! Welcome to another day in grade {grade_level}!'
    if school:
        return f'Hello from {school}!'
    if name:
        return f'Hello {name}!'

def show_employee(name, salary=9000):
    """Gives employee what they're due

    Args:
        name (str): name of the employee
        salary (float, optional): employee salary. Defaults to 9000.

    Returns:
        float: How much they're paid
    """
    return f'Hey {name}, here\'s your pay of ${salary}'

def reverse(string):
    reversed_str = ""
    for i in string:
        reversed_str = i + reversed_str

next_exercise("Essentially, I have this totally real 100% off coupon")

money_owed(input("What are you buying? >  "), float(input("How much is it? (USD) >  ")))
money_owed(input("What are you buying? >  "), float(input("How much is it? (USD) >  ")), 2)

next_exercise("What are you a cop?")

print(f"Hi there {format_name('James', 'Cameron')}")
print(f"Hi there {format_name('Greg')}")
print(f"Hi there {format_name()}")

next_exercise("I'm not Einstein,\n\nThat's it")

print(f"I love the fact {emc_squ(float(input('What is the mass of the object? (kg) >  ')))}J is the energy")

next_exercise("If a school database is running off a terminal, I swear")

print(student_messenger("john", "11th", "SDHS"))
print(student_messenger( school="SDHS", grade_level="11th", name="john"))
print(student_messenger("john", school="SDHS", grade_level="11th" ))

next_exercise("WORKWORKWORKWORKWORK hey money WORKWORKWORK...")

print(show_employee("James", 80000))
print(show_employee("James"))