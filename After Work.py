import random, time, sys

def typingEffect(text):
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

def typingInput(text):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value
def typingEffectSlow(text):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.75)

class Favfood:
        def __init__(self, main, side, side2):
            self.main = main
            self.side = side
            self.side2 = side2


def l_money():

            while True:


                lendmoney = typingInput("'Say can I borrow $20??' (y/n)\n")

                if lendmoney == "y":
                    typingEffect("'Thanks!'\n")
                    play_again()

                elif lendmoney =="n":
                    typingEffect("'Really? Wow, what are friends for?...'\n")
                    play_again()

                else:
                    typingEffect("Huh? {Type 'y' or 'n'}\n")
                    l_money()

def f_dinner(): 
       
            while True:

                friends_dinner = typingInput("'You don't mind me staying over for some, do ya, huh?' (y/n)\n")

                

                if friends_dinner =="y":
                    typingEffect("'Hey thanks man! You know, it's just as they say, 'What are good friends for?', orr something like that.'\n")
                    time.sleep(0.5)
                    typingEffect("\nIndeed.\nWhat else are friends for?\n" \
                    "After dinner, which indeed was quickly devoured,\nyour friend spends the rest of the night explaining\nto you how he can't pay his energy bill this month \n" \
                    "He asks you for a loan of $150 promising to pay you back next month.\n" \
                    "You pay him just so he'll leave.\nHe gives you a big kiss and quickly leaves.\nHe mentions something about being away for the next 4 months for urgent business.\n")
                    time.sleep(1.0)
                    typingEffect("\nYou're exhausted, have eaten little, and down $150.\nAtleast you can take a nap before work tomor- \n")
                    time.sleep(0.5)
                    typingEffect("Wait,")
                    time.sleep(1.0)
                    typingEffect(" are those birds chirping?\n")
                    play_again()
                
                elif friends_dinner =="n":
                    typingEffect("'Hey that's no good! We're pals, buddies, friends... amigos! Where do you get off treating me as if I'm some stranger?!'\n" \
                    "'You know what, you look tired so you're forgiven. Besides, all that working's probably got you going deaf haha!'\n" \
                    "'It's OK, I'll ask again.'\n")
                else:
                    typingEffect("Huh? What did you say? {Type 'y' or 'n'}\n")


def happyending():
      typingEffect("She laughs.\n 'To each their own'\n You both spend the rest of the night talking to the sound of the rain.\n" \
      "You both end up falling asleep, snuggled in each other's arms.\n")
      play_again() 

def tvshow():
    typingEffect("You turn on the TV.\n" \
    "The weatherman appears as he points toward the weekly forecast.\n"
    "'It's expected to rain tonight', she says.\n" \
    "No sooner after the words are spoken that a bolt of lightning flashes through the window.\n"
    "The sound of a strong rainfall soon follows.\n")
    time.sleep(1.0)
    typingEffect("'I love rain,'she purrs as she stretches out her arms and rests her head against your shoulder.\n")

    while True:
        opinion = typingInput("'Dont you?' she asks. (y/n)\n")

        if opinion == "y":
            happyending()
        elif opinion == "n":
            happyending()
        else:
            typingEffect("'What was that?' {Type 'y' or 'n'}\n")


def sit_down():
    typingEffect("You decide to lead her to the living room instead and show her to a seat...\n")
    typingEffect("'Hey thanks! Do you want to watch TV?'\n")

    while True:
            tv = typingInput("Turn on the TV? (y/n)\n")

            if tv == "y":
                tvshow()
            elif tv == "n":
                typingEffect("No. You don't want to watch TV,\n" \
                "'Wait a minute... this is MY time', you observe silently.\n" \
                "As you think it over you realize you want nothing to do with this stranger.\n" \
                "'Get out...', you say calmly.\n")
                time.sleep(1.25)
                typingEffect("'Uh wha-?, she says.\n" \
                "'GET OUT!', you yell at the top of your lungs.\n" \
                "She quickly perks up and flies out the door.\n" \
                "You can hear her crying as she runs down hall.\n")
                play_again()
            else:
                typingEffect("Invalid choice option {Type 'y' or 'n'}\n")
                return False
            
def sit_down2():
    typingEffect("You decide to lead her to the living room and show her to a seat...\n")
    typingEffect("'Hey thanks! Do you want to watch TV?'\n")

    while True:
            tv = typingInput("Turn on the TV? (y/n)\n")

            if tv == "y":
                tvshow()
            elif tv == "n":
                typingEffect("No. You don't want to watch TV,\n" \
                "'Wait a minute... this is MY time', you observe silently.\n" \
                "As you think it over you realize you want nothing to do with this stranger.\n" \
                "'Get out...', you say calmly.\n")
                time.sleep(1.25)
                typingEffect("'Uh wha-?, she says.\n" \
                "'GET OUT!', you yell at the top of your lungs.\n" \
                "She quickly perks up and flies out the door.\n" \
                "You can hear her crying as she runs down hall.\n")
                play_again()
            else:
                typingEffect("Invalid choice option {Type 'y' or 'n'}\n")
                return False




def food_test():
            typingEffect("Roll atleast a 5 to succeed in feeding her.")
            feed = random.randint(1,15)
            typingInput("Press Enter to roll.")
            print = feed
            if feed >= 5:
                typingEffectSlow("'mh mhh")
                typingEffect("MMMMH!'\n'This is so good!'\n'Truthfully, this is the best thing I've ate this month!'\n")
                typingEffect("As the food finishes cooking, you both talk about recipes and cooking techniques.\n")
                typingEffect("You share the small dinner under simple and intriguing conversation.\n")
                typingEffectSlow("...\n")
                typingEffect("'Wooooo! That was good!', she says.\n'Thank you so much for allowing me to dine with you.'\n")

                while True:
                             
                    smthn_else = typingInput("'Do you want to do something else??' (y/n)")
                    if smthn_else == "y":
                        sit_down2()
                    elif smthn_else =="n":
                        typingEffect("'Ok, well thanks for having me over! Hope to see you again!' she says as she heads out the door.\n"
                        "Yes enjoying someone's company is nice for a while, but that it's important to know when enough is enough.\n After all, this is YOUR time you're using.\n")
                        play_again()
                    else:
                        typingEffect("Huh? {Type 'y' or 'n'}\n")
                      
            else:
                typingEffect("OOPS! Instead of landing the spoon in her mouth,\n you accidentally spill the hot gravy onto her legs!\n" \
                "'AAAEEEIIIII!!!' she yells.\nShe quickly brushes the scalding gravy off her legs and, flushing red, hurries out the door.\n" \
                "Never to be seen again.\n") 
                play_again()

def kitchen():
            typingEffect("You both move inside to the kitchen.\nThere the you see the bustling pots of food pouring out steam.\n" \
            "'Hmmm! It smells so good in here,' she says.\n")
            typingInput("'Do you normally cook for yourself?' (y/n)\n")
            typingEffect("'Oh wow. You see, I would cook more, but at the moment I just don't have the time...'\n")

            while True:
                  
                trysome = typingInput("Let her try some? (y/n)\n")

                if trysome == "y":
                    food_test()
                elif trysome == "n":
                    typingEffect("You decide she doesn't need to try any of the food.\nBesides, you barely know this person...\n")
                    sit_down()
                else:
                    typingEffect("Invalid choice option {Type 'y' or 'n'}\n")
            
def invite_():
                
                while True:
                        invite = typingInput("'It smells really good...' (y/n)\n")
                        
                        if invite =="y":
                            kitchen()
                        elif invite =="n":
                            typingEffect("'Oh, forgive me...', she says embarrassed.\n'... Excuse me!'\n")
                            typingEffect("With that she turns and hurriedly heads down the hall back towards\nher apartment.\n" \
                            "As she walks away you're stuck wondering what could've been...\n")
                            play_again()
                        else:
                            typingEffect("'...What was that?'{Type 'y' or 'n'}\n")
                            return False

def girlfriend():
                typingEffect("'Oh perfect! I figured it was!'\n" \
                "'You've walked past with it before. Glad to have it back, huh?'\n" \
                "'I found it out in the hall a couple days ago.\n"
                "'It must've been on the afternoon with the huuuuuuge rainstorm...'\n")
                remember()
                
                
def remember():
            
            while True:
                remember = typingInput("'You remember the one?' (y/n)\n")

                if remember == "y":
                    typingEffect("'Yep! Crazy day, huh?'\n'I heard Ms. Green down the street had her dog blown away in the wind.'\n")
                    typingEffectSlow("...\n")
                    typingEffect("'Are you cooking something?,' she asks,")
                    invite_()

                elif remember == "n":
                    typingEffect("'Really?? How weird. It would have been hard to miss...'\n'Did you hear Ms. Green's dog was blown away in the strong winds??'\n")
                    typingEffectSlow("...\n")
                    typingEffect("'Are you cooking something?,' she asks,")
                    invite_()

                else:
                    typingEffect("'...What was that?' {Type 'y' or 'n'}\n")

                    


def f_smalltalk():
                typingEffectSlow("'MH MHH")
                typingEffect("MMMMH! Whatever you're cooking back there it sure smells good!'\n" \
                "'Well anyways I was at this new deli on 153rd Street and guess what???'\n")
                    
                time.sleep(0.3)

                typingEffect("'They had your favorite drink!!!'\n" \
                "'Hey here you go and don't mention it! You know as they say 'What else are friends for?'\n" \
                "Anyways, I'm in a hurry so I'll be off! Enjoy your dinner, good night!\n")

                time.sleep(1.0)

                while True:
                    food_ready = typingInput("Is the food ready yet? (y/n)\n")

                    if food_ready == "y":
                        typingEffect("\nAnd that, you did. Your favorite meal, accompanied by your favorite drink (thanks to a good friend)\n" \
                        "surely makes life worth it. As they say, 'What are friends for?'\n")
                        play_again()
                    
                    elif food_ready =="n":
                        play_game2()

                    else:
                        typingEffect("Invalid choice option {Type 'y' or 'n'}\n")


def talkative_friend(main, side, side2):

                typingEffect("There stands your friend of 7 years.\n")

                friends_mood = random.randint(1,3)

                if friends_mood == 1:
                    friends_mood1(main, side, side2)
                
                elif friends_mood == 2:
                    typingEffect("'Hey old pal, hows it goin! I'd figure I'd see how you're doing since I was in the neighborhood...'\n" \
                    "'Say, I can't stay for long. I'm in a bit of hurry...'\n")

                    smalltalk = typingInput("'Do you have a minute?' (y/n)\n")
                    if smalltalk == "y":
                        f_smalltalk()
                          
                    elif smalltalk == "n":
                        time.sleep(0.5)
                        typingEffect("'Goodbye!'\n")
                        time.sleep(0.5)
                        typingEffect("No, you don't 'have a minute.' You've worked long enough today.\nThis is your time to relax.\n")
                        play_again()
                    else:
                        typingEffect("What was that? {Type 'y' or 'n'}\n")
                
                elif friends_mood == 3:
                    typingEffect("'Hey buddy! How's it going??'\n")
                    l_money()
 
def unexpected_beauty():

                typingEffect("There stands a woman you've never met before.\n"
                "She stands with one arm folded while the other holds what looks to be your umbrella!\n" \
                "She spins the umbrella playfully.\n")

                while True:
                      
                    umbrella = typingInput("'Is this yours?', she asks. (y/n)\n")
                    if umbrella == "y":
                        girlfriend()
                    elif umbrella =="n":
                        typingEffect("'Oh, forgive me...', she says embarrassed.\n'... Excuse me!'\n")
                        typingEffect("With that she turns and hurriedly heads down the hall back towards\nher apartment.\n" \
                            "As she walks away you're stuck wondering what could've been...\n")
                        play_again()
                    else:
                            typingEffect("What was that? {Type 'y' or 'n'}\n")
                            return False
 
def nobodys_home():
                typingEffect("The doorway stands empty. Must've been the wind...\n")  
                play_again()


def play_game():
    typingEffect("You get home from a long day's work...\n")
    typingEffect("As you enter the door, the pit of your stomach howls.\nYou're starving!\n")
    time.sleep(0.5)
    typingEffect("Opening the fridge, you get started on your favorite dinner...\n")
    time.sleep(0.25)
    main = typingInput("What is your favorite food?:\n").upper()
    side = typingInput("What is your favorite side?:\n").upper()
    side2 = typingInput("What is your favorite side (2)?:\n").upper()
    time.sleep(1.0)
    typingEffect("Thank you.\n")  

    play_game2(main, side, side2)

def play_game2(main, side, side2):            
    typingEffect("The food continues to cook. You plop yourself on the couch, finally getting comfortable when...\n") 
    typingEffectSlow("...\n") 
    typingEffect("There's a knock...\nYou walk over to the door...\n")
    
    time.sleep(0.1)

    while True:

        choice2 = typingInput("Do you open the door? (y/n)\n")

        if choice2 == "y":

            guest = random.randint(1,3)
            
            if guest == 1:
                talkative_friend(main, side, side2)
            elif guest == 2:
                unexpected_beauty()
            elif guest == 3:
                nobodys_home()

        elif choice2 == "n":
            
            typingEffect("You decide to leave it alone.\nYou've worked long enough today. This is your time to relax.\n")
            play_again()
        else:
            typingEffect("Invalid choice option {Type 'y' or 'n'}\n")

          
def friends_mood1(main, side, side2):
        typingEffect("'Hey buddy, hows it goin! I was in the neighborhood and figured I'd stop by here.'\n")

        while True:
            skip1 = typingInput("Would you like to skip text? (y/n)\n")
            if skip1 == "y":
                f_dinner()
            elif skip1 == "n":
                typingEffect("'Oooooh, what's that smell?? Are you cooking in here?'\n" \
                "He steps in despite you standing between him and the doorframe.\n" \
                "Your friend walks past you, stepping into the kitchen.\n")
                typingEffect(f"'Ah {main.upper()} ??.. With {side.upper()}... AND {side2.upper()}???....'\n" \
                    "'MY FAVORITE!!'\n")
                f_dinner()
            else:
                typingEffect("Invalid choice option {Type 'y' or 'n'}\n")

def menu():
    while True:
        time.sleep(0.25)
        choice1 = typingInput ("Continue? (y/n)\n")

        if choice1 =="y":
            play_game()
        elif choice1 =="n":
            typingEffect("OK, take care.")
            sys.exit()
        else:
            typingEffect("Invalid choice option {Type 'y' or 'n'}\n")
            menu()

def play_again():
            
        while True:

            playagain = typingInput("Play Again? (y/n)\n")

            if playagain == "y":
                    play_game()
            elif playagain == "n":
                    typingEffect("OK, take care.\n")
                    sys.exit()
            else:
                    typingEffect("Invalid choice option {Type 'y' or 'n'}\n")
                    

def start_game():
     typingEffect("You get home from a long day's work...\n")
     menu()
     
if __name__=="__main__":
    start_game()





