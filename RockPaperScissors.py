def computer_choice():
    from random import randint
    return randint(1,3)


def best_of_10_winner(comp_score, player_score):
    if player_score > comp_score:
        print("You win!!")
    elif player_score == comp_score:
        print("Tie!!")
    else:
        print("You lose!!")