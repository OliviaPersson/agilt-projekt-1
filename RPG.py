<<<<<<< HEAD
#Implements a start menu for a adventure type game.

def start():
    count = 0
    while True:
        #Prints an intro message to player
        print("Suddenly you awake...")
        print("You are in a empty dark room...")
        print("You see two doors: one on the [right] and one on the [left]...")
        print("Which door do you choose ?")

        user_input = input("> ")
        #All possible choices
        if user_input  == "right" and count  < 3:
            #call a room function
            pass
        if user_input == "left" and count < 3:
            #Call a room function
            pass
        if count >=3:
            #Death function call 
            cause = "This will be printed by Death() function"
            
            death(cause)
            pass
        else:
            #No valid input from player
            print("You look to your [left] and [right]...")
            print("and decide to take a nap.")
            count = count +1 

#def death(cause):
#    #prints cause variable
#    print(cause + " nice try!")
#    # Returns to main menu
#    start()


def dragon_room():
    while True:

        print("You see a dragon...")
        print("Beside the dragon there is a pot of gold... ")
        print("In the distance you spot a door...")
        print("The dragon seems to not notice you...")
        print("Do you [flee] the dragon through the door... ")
        print("Do you [steal] the gold from the dragon ...")
        print("Do you ")
        print("\n" * 3)

        user_input = input("> ")

        if user_input == "flee":
            print("You sprint as fast as possible toward the nearest exit...")
            start()
        elif user_input == "fight" or user_input == "attack":
            print("You decided to attack the dragon...")
            cause = "You died"
            death(cause)
        elif user_input == "steal":
            print("You tried to steal from the dragon...")
            print("It stared at you, and in blink of an eye you disappear in flash of light...")
            skeleton_room()

            pass
        else:
            print(f"I have no idea what that {user_input} is")
    

def skeleton_room():
        print("You are  in a room with a skeleton..")
        print("It stands before you and challenges you to a guess the number game. ")
        print("Do you accept [y] or [n] ?")

        user_input = input("> ")
        
        if user_input == "y" :
            #Guess number game call here
            #if guess_game return true
            #Calls next room 
            #else calls main_menu()
            pass
        else:
            print("You do nothing but stand still and die!!!")
            main_menu()
        
        
        #calls guessnumber() game
    #

def mysterious_old_man_room():
        while True:
            print("You are in a room.. suddenly a mysterious old walks up to you... ")
            print("He challenges you to a evil game of ... tic tac toe.")
            print("Do you accept [y] or [n] .")

            user_input = input("> ")

            if user_input.capitalize == "Y":
                
                print("The old man is happy with your choice...")
                #calls TIcTicToe()game
                if True:#TicTactoe == True 
                    #
                    pass
                pass
            elif user_input.capitalize == "N":
                print("The mysteroious old man is disappointed and whispers a spell... ")
                print("You disappear instantly")
                pass
            elif user_input == "":
                pass
            else:
                print(f"I don't know what {user_input} is.")


def gold_room():
    print
    

=======

#Implements a start menu for a adventure type game.

def start():
    count = 0
    while True:
        #Prints an intro message to player
        print("Suddenly you awake...")
        print("You are in a empty dark room...")
        print("You see two doors: one on the [right] and one on the [left]...")
        print("Which door do you choose ?")

        user_input = input("> ")
        #All possible choices
        if user_input  == "right" and count  < 3:
            #call a room function
            pass
        if user_input == "left" and count < 3:
            #Call a room function
            pass
        if count >=3:
            #Death function call 
            print("This will be printed by Death() function")
            pass
        else:
            #No valid input from player
            print("You look to your [left] and [right]...")
            print("and decide to take a nap.")
            count = count +1 


def dragon_room():
    while True:

        print("You see a dragon...")
        print("Beside the dragon there is a pot of gold... ")
        print("In the distance you spot a door...")
        print("The dragon seems to not notice you...")
        print("Do you [flee] the dragon through the door... ")
        print("Do you [steal] the gold from the dragon ...")
        print("Do you ")
        print("\n" * 3)

        user_input = input("> ")

        if user_input == "flee":
            print("You sprint as fast as possible toward the nearest exit...")
            start()
        elif user_input == "fight" or user_input == "attack":
            print("You decided to attack the dragon...")
            cause = "You died"
            death(cause)
        elif user_input == "steal":
            print("You tried to steal from the dragon...")
            print("It stared at you, and in blink of an eye you disappear in flash of light...")
            skeleton_room()

            pass
        else:
            print(f"I have no idea what that {in_data} is")
    

def skeleton_room():
        print("You are  in a room with a skeleton..")
        print("It stands before you and challenges you to a guess the number game. ")
        print("Do you accept [y] or [n] ?")

        user_input = input("> ")
        
        if user_input == "y" :
            #Guess number game call here
            #if guess_game return true
            #Calls next room 
            #else calls main_menu()
            pass
        else:
            print("You do nothing but stand still and die!!!")
        
        
        #calls guessnumber() game
    #

def mysterious_old_man_room():
        print("You are in a room.. suddenly a mysterious old walks up to you... ")
        print("He challenges you to a evil game of ... tic tac toe.")
        print("")
        #calls TIcTicToe()game

def gold_room():
    print
    

>>>>>>> ca54b036353b6cfddceb5a406698ff7833391875
