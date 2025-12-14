import random
import time, sys

def typewriter_effect(text):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

def typewriter_input(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value
    


def play_game():
    typewriter_effect("Welcome to Store 519, roll atleast a 20 to enter.\n")

    random_number = random.randint(1,40)

    time.sleep(0.5)

    input("Press Enter to roll...")

    print(random_number)

    time.sleep(0.25)

    if random_number >= 20:
        typewriter_effect("Welcome! Enjoy your time shopping!\n")
    else:
        typewriter_effect("Aww... Sorry come back another time...\n")
        time.sleep(0.5)
        choice1 = typewriter_input("Would you like to force your way in?:(y/n)\n")

        time.sleep(0.5)

        if choice1 == "y":
            typewriter_effect("That's the spirit!\nRoll atleast a 10 to pass through security.\n")
            input("Press Enter to roll...")
            random_number2 = random.randint(1,20)
            time.sleep(0.5)
            print(random_number2)

            if random_number2 >= 10:
                typewriter_effect("Congratulations! You barged your way through. Enjoy your time shopping!\n")
            else:
                typewriter_effect("Aww... As you tried headbutting security to get in, you couldn't manage against their strength.\nYou were thrown out of the establishment...\n")

        else:
            time.sleep(0.25)
            typewriter_effect("OK, have a nice day.\n")
def menu():
    while True:
        time.sleep(0.25)
        choice2 = typewriter_input("Would you like to go shopping?:(y/n)\n")
        
        time.sleep(0.5)

        if choice2 =="y":
            play_game()
        elif choice2 == "n":
            typewriter_effect("OK.")
            return False
        else:
            typewriter_effect("Not a correct choice: {Type 'y' or 'n'}\n")
            menu()

if __name__=="__main__":
    menu()