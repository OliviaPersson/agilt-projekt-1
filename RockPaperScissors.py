def print_winner_and_score(winner,player1,player2):
    #Print who won the round and the current score.
    print(f'{winner} has won!\nThe score is: \nPlayer 1: {player1}\nPlayer 2: {player2}')

def computer_choice():
    #Generates random choice for computer
    from random import randint
    return randint(1,3)

def best_of_winner(comp_score, player_score):
    #Checks who has the most wins
    if player_score > comp_score:
        print("You win!!")
    elif player_score == comp_score:
        print("Tie!!")
    else:
        print("You lose!!")

