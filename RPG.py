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
