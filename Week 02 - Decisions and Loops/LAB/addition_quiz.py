"""
Addition Quiz

Step 1: Generate two single-digit intergers for number1 (e.g., 4) and number2 (e.g., 5)
Step 2:promt the student to answer, "what is 4 + 5?" (user input)
Step 3: Check if the student answer is correct. 
"""
import random

while True:
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    answer = int(input(f"What is {num1} + {num2}? "))

    if answer == num1 + num2:
        print("Correct!")
        break
    else:
        print("Try again")
