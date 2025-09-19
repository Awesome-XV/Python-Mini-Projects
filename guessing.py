import random

guess = input("Guess a number from 1-100: ")

try:
    guess = int(guess)
except ValueError:
    print("Error: Please enter a number.")
else:

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
            guess = input("Try guessing lower this time ")
            try:
                guess = int(guess)
            except ValueError:
                print("Error: Please enter a number.")
                break
            guesses += 1
        elif guess < number:
            guess = input("Try guessing higher this time ")
            guess = int(guess)
            guesses += 1
        elif (guess == number) and (guess >= 0):
            print("You got the right answer in ", guesses, "guesses try again to get it first try")
        else:
            print("Error")
            
    if guess == number:
        print("You got it! The number was", number)
        print("And it only took you", guesses, "tries!")

try:
    from pause_on_exit import pause_on_exit
    pause_on_exit()
except Exception:
    pass