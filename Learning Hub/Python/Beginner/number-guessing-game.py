import random

num = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Please enter a valid integer!")
        continue

    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
    else:
        print("Congratulations! You guessed the correct number.")
        break
