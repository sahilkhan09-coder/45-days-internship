import random

secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 7


print("Guess the number between 1 and 100")


while attempts < max_attempts:

    guess = int(input("Enter your guess: "))

    attempts += 1


    if guess > secret_number:
        print("Too high")

    elif guess < secret_number:
        print("Too low")

    else:
        print("Correct!")
        print("You guessed it in", attempts, "attempts")
        break



else:
    print("Game Over!")
    print("The correct number was", secret_number)
