import sys
from plans import missile_building
import time
import random
import msvcrt

def main():
    print("Well hello there you have been found in 5747 and have been asleep for some amount of years we don't know but we need your help.")
    print("There was a nuclear fallout and half of the world has been destroyed and we need your knowledge to make the nukes again or at least a few missiles.")

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
        result = input("You have reached an enemy force of 2 soldiers in the way. Do you confront them?")
    else:
        print("You have been found in 5747 and have been asleep for some amount of years we don't know but we need your help.")
        print("There was a nuclear fallout and half of the world has been destroyed and we need your knowledge to make the nukes again or at least a few missiles.")
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
            answer = input("How do you fight the enemies? Make this choice wisely there is only 1 right answer any others and you will die.").lower()
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

        RED = "\033[91m"
        GREEN = "\033[92m"
        RESET = "\033[0m"

        def reaction():
            print("The enemy is about to launch their own missile you need to click launch at exactly the right moment")
            print("Wait for green and press 'c' within 500ms otherwise you will die")
            time.sleep(7.5)
            print(f"{RED}RED{RESET}")
            time.sleep(random.uniform(2, 5)) 
            print(f"{GREEN}GREEN{RESET}")

            start_time = time.time()
            timeout = 0.5

            def check_key():
                while time.time() - start_time < timeout:
                    if msvcrt.kbhit():
                        key = msvcrt.getch().decode('utf-8').lower()
                        if key == 'c':
                            print("I guess you did it.")
                            return True
                print("Sorry to say it but you were too slow")
                return False

            if check_key():
                handle(True)
            else:
                print("You have died due to slow reflexes.")
                handle("Dead")

        reaction()
        missile_building()
    elif answer == "no":
        print("You BETRAY us after all of this so you deserve this death")
        handle("Dead")
    else:
        handle("Fail")

main()