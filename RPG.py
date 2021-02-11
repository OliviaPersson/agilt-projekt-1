#Implements a start menu for a adventure type game.
from time import sleep

def print_slow(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.03)
    print() # go to new line

def start():
        #Prints an intro message to player
        print_slow("Suddenly you awake...")
        print_slow("You are in a empty dark room...")
        print_slow("You see two doors: one on the [right] and one on the [left]...")
        print_slow("Which door do you choose ?")

        user_input = input("> ")
        #All possible choices
        if user_input  == "right":
            print_slow("You chose the right door...")
            dragon_room()
            pass
        if user_input == "left":
            print_slow("You chose the left door")
            lava_room()
            pass
        else:
            #No valid input from player
            print_slow("You look to your [left] and [right]...")
            print_slow("and decide to take a nap.")

def lava_room():
    print_slow("The floor is lava...")
    print_slow("You see a haunting apperation on the other side of the room...")
    print_slow("He challenges you to a game of Tic Tac Toe...")
    print_slow("Do you accept [y] or [n] ?")

    user_input = input("> ")
        
    if user_input == "y":
        import TicTacToe
        if (TicTacToe.TicTacToe().play_vs_AI() == 0):
        #player has won
            print_slow("You disappear in a flash of light ...")
            skeleton_room()
        else:
            death()                        
    else:
        print_slow("The apperation pushes you into the lava")
        death()

def dragon_room():

        print_slow("You see a dragon...")
        print_slow("Beside the dragon there is a pot of gold... ")
        print_slow("In the distance you spot a door...")
        print_slow("The dragon seems to not notice you...")
        print("Do you [flee] the dragon through the door... ")
        print("Do you [steal] the gold from the dragon ...")
        print("Do you [fight] the dragon  ")
        print("\n" * 3)

        user_input = input("> ")

        if user_input == "flee":
            print_slow("You sprint as fast as possible toward the nearest exit...")
            start()
        elif user_input == "fight" or user_input == "attack":
            print_slow("You decided to attack the dragon...")
            death()
        elif user_input == "steal":
            print_slow("You tried to steal from the dragon...")
            print_slow("It stared at you, and in blink of an eye you disappear in flash of light...")
            skeleton_room()          
        else:
            print_slow(f"I have no idea what that {user_input} is")
    
def skeleton_room():
        print_slow("You are  in a room with a skeleton..")
        print_slow("It stands before you and challenges you to a guess the number game... ")
        print("Do you accept [y] or [n] ?")

        user_input = input("> ")
        
        if user_input == "y":
            from GuessNumber import count_and_compere_guessednumber
            truecheck = count_and_compere_guessednumber("r")
                       
            if truecheck == True: 
                print_slow("You disappear in a flash of light ...")
                mysterious_old_man_room()
            else:
                death()                        
        else:
            print_slow("The skeleton stabs you in the face")
            death()
        
def mysterious_old_man_room():
            print_slow("You are in a room.. suddenly a mysterious old man walks up to you... ")
            print_slow("He challenges you to a evil game of ... Rock paper Scissors.")
            print("Do you accept [y] or [n] .")

            user_input = input("> ")

            if user_input == "y":
                
                print_slow("The old man is happy with your choice...")
                from RockPaperScissors import play_rock_paper_scissors
                truecheck = play_rock_paper_scissors("r")

                if truecheck == True: 
                    gold_room()
                else:
                    death()
                
            elif user_input == "n":
                print_slow("The mysteroious old man is disappointed and whispers a spell... ")
                print_slow("You disappear instantly")
                death()
                
            else:
                print_slow(f"I don't know what {user_input} is.")

def death():
    print_slow("You died!")
    a = input("You want to play again y/n: ")
    if a == "y":
        start()
    else:
        from main import main_menu
        main_menu()

def gold_room():
    print_slow("You are in a gold room ...")
    print_slow("There is treasure everywhere...")
    print_slow("How much do you take ? ...")

    user_input = input("> ")

    user_input = int(user_input)

    if user_input < 50 :
        print_slow("Good job . You are not greedy. You Win")
        input("Press any key to return to main menu")
        from main import main_menu
        main_menu()
        
    
    else:
        print_slow("You greedy bastard.")
        death()

