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