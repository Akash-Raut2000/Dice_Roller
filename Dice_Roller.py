import random

def roll_dice(sides):
    return random.randint(1, sides)

while True:
    print("Options:")
    print("Enter 'roll' to roll a dice")
    print("Enter 'exit' to end the program")

    user_input = input(": ")

    if user_input == "exit":
        break

    if user_input == "roll":
        sides = int(input("Enter the number of sides on the dice: "))
        result = roll_dice(sides)
        print(f"You rolled a {sides}-sided dice and got: {result}")
    else:
        print("Invalid input. Please enter a valid option.")