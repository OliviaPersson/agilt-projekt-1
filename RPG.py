#Implements a start menu for a adventure type game.

def start():
    count = 0
    while True:
        #Prints an intro message to player
        print("Suddenly you awake...")
        print("You are in a empty dark room...")
        print("You see two doors: one on the [right] and one on the [left]...")
        print("Which door do you choose ?")

        input = input("> ")
        #All possible choices
        if input  == "right" and count  < 3:
            #call a room function
            pass
        if input == "left" and count < 3:
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

def death(cause):
    #prints cause variable
    print(cause)
    # Returns to main menu
    main_menu()


def dragon_room():

    print("You see a dragon...")
    print("Beside the dragon there is a pot of gold... ")
    print("In the distance you spot a door...")
    print("The dragon seems to not notice you...")
    print("Do you [flee] the dragon through the door... ")
    print("Do you [steal] the gold from the dragon ...")
    print("Do you ")

    print()

def skeleton_room():
        print("You are  in a room with a skeleton..")
        print("It stands before you and challenges you to a guess the number game. ")
        print("Do you accept [y] or [n] ?")

        input = input("> ")
        
        if input == "y" :
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
        print("You are in a room.. suddenly a mysterious old walks up to you... ")
        print("He challenges you to a evil game of ... tic tac toe.")
        print("")
        #calls TIcTicToe()game

def gold_room():
    print
    

