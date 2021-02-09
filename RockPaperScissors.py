
def print_winner_and_score(winner,player1,player2):
    #Print who won the round and the current score.
    print(f'{winner} has won!\nThe score is: \nPlayer 1: {player1}\nPlayer 2: {player2}')

def computer_choice():
    from random import randint
    return randint(1,3)

def play_rock_paper_scissors():
    #Take a user input and compere it to the computers choise. Call a print function to print the score of every round. Call a print function to print the winner of the game. 

    count = 1
    comput_choice = computer_choice()
    user_win = 0
    computer_win = 0
    tie = 0

    while count <= 10:
        print('Select 1 (for rock), 2 (for paper), 3 (for scissors)')
        user_choice = int(input())
        
        if user_choice == comput_choice:
            tie = tie + 1
        elif user_choice == 1:
            if comput_choice == 2:
                computer_win = computer_win + 1
            else:
                user_win = user_win + 1
        elif user_choice == 2:
            if comput_choice == 1:
                user_win = user_win + 1
            else:
                computer_win = computer_win + 1
        elif user_choice == 3:
            if comput_choice == 1:
                computer_win = computer_win + 1
            else:
                user_win = user_win + 1
    
        print_winner_and_score(1,user_win,computer_win)
    
    
    best_of_winner(computer_win,user_win)
    

      

