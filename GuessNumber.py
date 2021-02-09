def random_number():
    #Returns a random number 
    from random import randint
    return randint(1,10)

def count_and_compere_guessednumber():
    #Take a number as an input and compere to a random number and call a function for printing the resault
    count = 1
    while count <= 3:
        print('Guess a number: ')
        guess = int(input())
        if guess != random_number():
            if guess < random_number():
                print_guess_status('to low',count)
                count += 1
            elif guess > random_number():
                print_guess_status('to high',count)
                count += 1
        else:
            print_guess_status('right',count)

    print('Do you want to play again? y/n')
    answer = input()
    if answer == 'y':
        count_and_compere_guessednumber()
    elif answer == 'n':
        main_menu()
    else:
        print('You can onley select y for yes or n for no.')

count_and_compere_guessednumber()