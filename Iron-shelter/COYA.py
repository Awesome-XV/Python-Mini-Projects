import sys

def main():
    print("Well hello there you have been found in 5747 and he been asleep for some amout of years we don't know but we need your help.")
    print("There was a nuclear fallout and half of the world is destoryed and we need your knowledge to make the nukes again or at least a few missiles.")

    result = input("Do you accept this task? Yes or No")

    def handle(result):
        if result == True:
            print("You have completed the task")
            input("Press enter to continue to the next task")
        elif result == "Fail":
            print("You have failed try again you have been given one more chance")
            main()
            result = input("Do you accept this task? Yes or No")
        elif result == "Dead":
            print("You have died game over")
            sys.exit()
        else:
            print("What did you do since you failed your assignment you have died")

    if (result == "Yes") or (result == "yes"):
        print("You're in the field and your first task is to navigate to our research center and you have been given a weapon (Gun).")
        result = input("You have reached a enemy force of 2 soldiers in the way to you confront them?")
    else:
        print("you have been found in 5747 and he been asleep for some amout of years we don't know but we need your help.")
        print("There was a nuclear fallout and half of the world is destoryed and we need your knowledge to make the nukes again or at least a few missiles.")
        result = input("Do you accept this task? Yes or No")

    if (result == "Yes") or (result == "yes"):
        handle("Dead")
    elif (result == "No") or (result == "no"):
        handle(True)
    else:
        handle("Fail")
    answer = input("Now you find a empty tank do you want to command it?").lower()
    if answer == "yes":
        print("You have chosen to command the tank.")
        handle(True)
    elif answer == "no":
        print("So you continue your journey and you are ambushed by enemy forces.")
        answer = input("How do you want to defend? Run or Fight").lower()
        if answer == "fight":
            answer == input("How do you fight the enimies make this choice wisley there is only 1 right answer any others and you will die.").lower()
            if answer == "gun":
                handle(True)
            else:
                handle("Dead")
        elif answer == "run":
            handle("Dead")
    else:
        handle("Fail")
    
    print("So you have survived this far good job")
    answer = input("You have reached the research center now you need to build the missile before the enemy launches. Do you want to start building?").lower()
    if answer == "yes":
        print("You have chosen to start building the missile.")
        

main()
