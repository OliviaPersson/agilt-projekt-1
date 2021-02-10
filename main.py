from RPG import start
from RockPaperScissors import play_rock_paper_scissors
from GuessNumber import count_and_compere_guessednumber

def main_menu():
    #while True:
        
    #Prints a welcome message.
    #Prints choices
    print("******************************************")
    print("Welcome to group 5's project games ")
    print("Choose a game !!")
    print("Type [1] to play an adventure game.")
    print("Type [2] to play a guess a number game.")
    print("Type [3] to play rock papper scissors.")
    print("Type [4] to play tic-tac-toe.")
    print("Type [E] to exit application.")
    print("*******************************************")
    print("\n" * 3)
    in_data = input("> ")

    if in_data == "1":
        #RPG function call here.
        start()
    elif in_data == "2":
        #Guess a number function call herer.
        count_and_compere_guessednumber("m")
    
    elif in_data == "3":
        #Rock papper scissors function call here.
        play_rock_paper_scissors()

    elif in_data == "4":
        #Tic Tac Toe function call here.
        pass

    elif in_data.capitalize == "E":
        #Exits application on [E] command.

        exit(0)
        pass
    else:
        #
        print("You have not typed in a valid command")
        print("Please try again.")



    
    
    
    
