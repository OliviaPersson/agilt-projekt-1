#Implements a start menu for a adventure type game.
loop = False

def start():
    while loop == False:
        #Prints an intro message to player
        print("Suddenly you awake...")
        print("You are in a empty dark room...")
        print("You see two doors: one on the [right] and one on the [left]...")
        print("Which door do you choose ?")

        user_input = input("> ")
        #All possible choices
        if user_input  == "right":
            print("You chose the right door...")
            dragon_room()
            pass
        if user_input == "left":
            print("You chose the left door")
            skeleton_room()
            pass
        else:
            #No valid input from player
            print("You look to your [left] and [right]...")
            print("and decide to take a nap.")



def dragon_room():

        print("You see a dragon...")
        print("Beside the dragon there is a pot of gold... ")
        print("In the distance you spot a door...")
        print("The dragon seems to not notice you...")
        print("Do you [flee] the dragon through the door... ")
        print("Do you [steal] the gold from the dragon ...")
        print("Do you [fight] the dragon  ")
        print("\n" * 3)

        user_input = input("> ")

        if user_input == "flee":
            print("You sprint as fast as possible toward the nearest exit...")
            start()
        elif user_input == "fight" or user_input == "attack":
            print("You decided to attack the dragon...")
            print("You died. Good job")
            start()
        elif user_input == "steal":
            print("You tried to steal from the dragon...")
            print("It stared at you, and in blink of an eye you disappear in flash of light...")
            skeleton_room()

            
        else:
            print(f"I have no idea what that {user_input} is")
    

def skeleton_room():
        print("You are  in a room with a skeleton..")
        print("It stands before you and challenges you to a guess the number game... ")
        print("Do you accept [y] or [n] ?")

        user_input = input("> ")
        
        if user_input == "y":
            from GuessNumber import count_and_compere_guessednumber
            yo = count_and_compere_guessednumber("r")

                        
            if yo == True: 
                print("You disappear in a flash of light ...")
                mysterious_old_man_room()
            else:
                death()
                loop = True   
            
            
        else:
            death()
            loop = True
        
        
    

def mysterious_old_man_room():
        while True:
            print("You are in a room.. suddenly a mysterious old walks up to you... ")
            print("He challenges you to a evil game of ... tic tac toe.")
            print("Do you accept [y] or [n] .")

            user_input = input("> ")

            if user_input.capitalize == "Y":
                
                print("The old man is happy with your choice...")
                #calls TIcTicToe() game 

                if True:#TicTactoe == True 
                    #calls gold_room()
                    pass
                pass
            elif user_input.capitalize == "N":
                print("The mysteroious old man is disappointed and whispers a spell... ")
                print("You disappear instantly")
                

            else:
                print(f"I don't know what {user_input} is.")

def death():
    print("You died!")

def gold_room():
    print("You are in a gold room ...")
    print("There is treasure everywhere...")
    print("How much do you take ? ...")

    user_input = input("> ")

    user_input = int(user_input)

    if user_input < 50 :
        print("Good job . You are not greedy. You Win")
        
    
    else:
        print("You greedy bastard.")

