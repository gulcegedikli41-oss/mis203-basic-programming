import math
import random

print("Welcome to the Number Lab!")
name = input("Enter your name: ")
print(f"Hello, {name}! Let's explore some numbers.")
repetition = "e"
while repetition == "e":
    amount = int(input("How many numbers would you like to enter? "))
    print(f"{int(amount)} random numbers are being generated.")
    for counter in range(1, int(amount) + 1):
        number = random.randint(1, 50)
        print(f"Number {counter}: {number}")
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
        if number > 35:
            print(f"{number} is a great number.")
        elif 15 <= number <= 35:
            print(f"{number} is a middle number.")
        else:
            print(f"{number} is a small number.")
        number = math.sqrt(number)
        print(f"The square root of number is {number:.2f}.")
    repetition = input("Would you like to repeat the process? (enter 'e' to repeat): ")
if repetition == "h":
    print(f"Thank you for using the Number Lab, {name}! Goodbye!")





