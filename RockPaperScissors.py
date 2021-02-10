def print_winner_and_score(winner,player1,player2):
    #Print who won the round and the current score.
    print(f'{winner} has won!\nThe score is: \nPlayer 1: {player1}\nPlayer 2: {player2}')

def computer_choice():
    #Generates random choice for computer
    from random import randint
    return randint(1,3)


def play_rock_paper_scissors(op):
    #Take a user input and compere it to the computers choise. Call a print function to print the score of every round. Call a print function to print the winner of the game. 

    count = 1
    user_win = 0
    computer_win = 0
    tie = 0

    if op == 'm':

        while count <= 10:
            print('Select 1 (for rock), 2 (for paper), 3 (for scissors)')
            user_choice = int(input())
            comput_choice = computer_choice()
       
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
            count += 1   
            print_winner_and_score(1,user_win,computer_win)
    
    
        best_of_winner(computer_win,user_win)

    else:
        while count <= 10:
            print('Select 1 (for rock), 2 (for paper), 3 (for scissors)')
            user_choice = int(input())
            comput_choice = computer_choice()

            if user_choice == comput_choice:
                print('Tie!')
                tie = tie + 1
            else:
                if user_choice == 1:
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
            count += 1 

        if user_win > computer_win:
            return True
        elif user_win < computer_win:
            return False
    

      

def best_of_winner(comp_score, player_score):
    #Checks who has the most wins
    if player_score > comp_score:
        print("You win!!")
    elif player_score == comp_score:
        print("Tie!!")
    else:
        print("You lose!!")

#play
play_rock_paper_scissors('r')