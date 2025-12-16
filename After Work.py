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

def l_money():

            while True:


                lendmoney = typingInput("'Say can I borrow $20??' (y/n)\n")

                if lendmoney == "y":
                    typingEffect("'Thanks!'\n")
                    playagain = typingInput("Play Again? (y/n)\n")

                    if playagain == "y":
                            menu()
                    elif playagain == "no":
                             typingEffect("OK.")
                             return False
                    else:
                             typingEffect("Invalid choice option {Type 'y' or 'n'}\n")
                             return False
                elif lendmoney =="n":
                    typingEffect("'Really? Wow, what are friends for?...'\n")
                    
                    playagain = typingInput("Play Again? (y/n)\n")

                    if playagain == "y":
                            menu()
                    elif playagain == "no":
                             typingEffect("OK.")
                             return False
                    else:
                             typingEffect("Invalid choice option {Type 'y' or 'n'}\n")
                             return False

                else:
                    typingEffect("Huh? {Type 'y' or 'n'}\n")
                    l_money()

def f_dinner(): 
       
            while True:

                friends_dinner = typingInput("'You don't mind me staying over for some, do ya, huh?' (y/n)\n")

                

                if friends_dinner =="y":
                    typingEffect("'Hey thanks man! You know, it's just as they say, 'What are good friends for?', orr something like that.'\n")
                    time.sleep(0.5)
                    typingEffect("Indeed. What else are friends for?\n" \
                    "After dinner, which indeed was quickly devoured,\nyour friend spends the rest of the night explaining\nto you how he can't pay his energy bill this month \n" \
                    "due to 'these forsaken AI engineers inflating the cost of water'.\nHe asks you for a loan of $150 promising to pay you back next month.\n" \
                    "You cave in for anything more than to see him go.\nHe kisses you emphatically and promptly leaves\nquickly mentioning he'll be away for the next 4 months for urgent business.\n")
                    time.sleep(0.5)
                    typingEffect("You're exhausted, have eaten little, and down $150.\nAtleast you can take a nap before work tomor- \n")
                    time.sleep(0.5)
                    typingEffectSlow("Wait,")
                    typingEffect(" are those birds chirping?\n")
                    playagain = typingInput("Play Again? (y/n)\n")

                    if playagain == "y":
                            menu()
                    elif playagain == "no":
                             typingEffect("OK.")
                             return False
                    else:
                             typingEffect("Invalid choice option {Type 'y' or 'n'}\n")
                             return False
                
                elif friends_dinner =="n":
                    typingEffect("'Hey that's no good! We're pals, buddies, friends... amigos! Where do you get off treating me like some stranger?!'\n" \
                    "'You know what, you look tired so you're forgiven. Besides, all that working's probably got you going deaf haha!'\n" \
                    "'It's OK, I'll ask again.'\n")
                else:
                    typingEffect("Huh? What did you say? {Type 'y' or 'n'}\n")
                    f_dinner()

def talkative_friend():

                typingEffect("There stands your friend who lives 15 blocks up from you.\n")

                input("Press Enter to continue...")

                friends_mood = random.randint(1,3)

                if friends_mood == 1:
                    typingEffect("'Hey buddy, hows it goin! I was in the neighborhood and figured I'd stop by.'\n" \
                    "'Oooooh, what's that smell?? Are you cooking in here? What're you cheffing up tonight?'\n" \
                    "He steps in despite you standing between him and the doorframe.\n" \
                    "Your friend walks past you and steps into the kitchen looking for the culprit of such enticing aromas.\n" \
                    "'Ah FRIED CHICKEN??.. With MASHED POTATOES... AND GRAVYY???....'\n" \
                    "'MY FAVORITE!!'\n")
                    output = f_dinner()

                

                elif friends_mood == 2:
                    typingEffect("'Hey old pal, hows it goin! I was in the neighborhood and figured I'd see how my good pal anon is doing!'\n" \
                    "'Say, I'm in a bit of hurry, so I can't stay for long...'\n")
                    typingEffectSlow("'MH MHH")
                    typingEffect("MMMMH! Whatever you're cooking back there it sure smells good!'\n" \
                    "'Well anyways I was at this new deli on 153rd Street and guess what???'\n")
                    
                    time.sleep(0.3)

                    typingEffect("'They had your favorite drink!!!'\n" \
                    "'Hey here you go and don't mention it! You know as they say 'What else are friends for?'\n" \
                    "Anyways, I'm in a hurry so I'll be off! Enjoy your dinner, good night!\n")

                    time.sleep(0.3)

                    typingEffect("And that, you did. Your favorite meal, accompanied by your favorite drink (thanks to a good friend)\n" \
                    "surely makes life worth it. As they say, 'What are friends for?'\n")
                    playagain = typingInput("Play Again? (y/n)\n")

                    if playagain == "y":
                            menu()
                    elif playagain == "no":
                             typingEffect("OK.")
                             return False
                    else:
                             typingEffect("Invalid choice option {Type 'y' or 'n'}\n")
                             return False
                
                elif friends_mood == 3:
                    typingEffect("'Hey buddy! How's it going??'\n")
                    output = l_money()
 
def unexpected_beauty():
                typingEffect("There stands a woman you've never seen before\n"
                "She stands with one arm folded while the other holds what looks\n"
                "to be your your umbrella. You haven't seen this umbrella in 3 days.\n" \
                "Her brown eye stare at you intently with a sincere mischeviousness, as if\n" \
                "she haaad be the one to somehow have your property and honestly know who to\n" \
                "return it to... 3 days later. "
                "She had intense dark eyes that shown through her dirty tan face.\n")
                playagain = typingInput("Play Again? (y/n)\n")

                if playagain == "y":
                            menu()
                elif playagain == "no":
                    typingEffect("OK.")
                    return False
                else:
                    typingEffect("Invalid choice option {Type 'y' or 'n'}\n")
                    return False
 
def nobodys_home():
                typingEffect("The doorway stands empty. Must've been the wind...\n")  
                playagain = typingInput("Play Again? (y/n)\n")

                if playagain == "y":
                            menu()
                elif playagain == "no":
                    typingEffect("OK.")
                    return False
                else:
                    typingEffect("Invalid choice option {Type 'y' or 'n'}\n")
                    return False
                     

def play_game():
    typingEffect("Your stomach growls right as you enter the door,\nYou're starving!\n" \
    "Opening the fridge, you get started on your favorite dinner:\nFried Chicken, Mashed Potatoes and Gravy.\n" \
    "As the food begins to cook, you start getting settled in to unwind.\n") 
    typingEffectSlow("...\n") 
    typingEffect("There's a knock...\nYou walk over to the door...\n")
    
    time.sleep(0.1)

    choice2 = typingInput("Do you open the door? (y/n)\n")

    if choice2 == "y":

        guest = random.randint(1,3)
        
        if guest == 1:
              talkative_friend()
        elif guest == 2:
              unexpected_beauty()
        elif guest == 3:
              nobodys_home()

        typingEffect("You open the door.\n")
        talkative_friend()
    elif choice2 == "n":
         
         typingEffect("You decide to leave it alone.\nYou've worked long enough today.\nThis is your time to relax.\n")
         menu()

def menu():
    while True:
        time.sleep(0.25)
        typingEffect("You get home from a long day's work...\n")
        choice1 = typingInput ("Continue? (y/n)\n")

        if choice1 =="y":
            play_game()
        elif choice1 =="n":
            typingEffect("OK.")
            return False
        else:
            typingEffect("Not a correct choice: {Type 'y' or 'n'}\n")
            menu()

if __name__=="__main__":
    menu()


