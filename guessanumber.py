
# import random module.
import random

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

random_number = random.randint(lower_limit, upper_limit)
print("You will have to choose a number between", upper_limit, " and ", lower_limit)

# while True:
chances = 6
while chances < 7:
    print("You have ", chances+1, " chances to guess a number ")
    guess = int(input("Enter your guess: "))
    if random_number == guess:
        print("Congrats !!!, you did it. The number is ", random_number)
        break
    elif guess < random_number:
        print("You guessed a small number.")
    elif guess > random_number:
        print("You guessed a larger number.")
    if chances == 0:
        print("\n You've run out of chances")
        print("\n The number is ", random_number)
        print("Better luck next time")
        break
    print("\n")
    chances -= 1
