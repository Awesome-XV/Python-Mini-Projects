import random

guess = input("Guess a number from 1-100: ")
guess = int(guess)

if 1 <= guess <= 100:
    print("Pick a number between 1 and 100")

number = random.randint(1, 100)


guesses = 1

if (guess == number) and (guess == 0):
    print("Man your good you need to get a life")
elif (guess == number) and (guess >= 0):
    print("You got the right answer in ", guesses, "guesses try again to get it first try")

while guess != number:
    if guess > number:
        guess = int(input("Try guessing lower this time "))
        guesses += 1
    elif guess < number:
        guess = int(input("Try guessing higher this time "))
        guesses += 1
    elif (guess == number) and (guess >= 0):
        print("You got the right answer in ", guesses, "guesses try again to get it first try")
    else:
        print("Error")
        
try:
    from pause_on_exit import pause_on_exit
    pause_on_exit()
except Exception:
    pass