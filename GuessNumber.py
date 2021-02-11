def print_guess_status(string,count):
    #Print if guess is to low/hight or right and amount of guesses taken 
    if string.lower() == "right":
        print("Good job! Your guess is {0} and you managed it in {1} guesses".format(string,count))
    else:    
        print("Your guess is {0} and you have guessed {1} times".format(string,count))

def random_number():
    #Returns a random number 
    from random import randint
    return randint(1,10)

def count_and_compere_guessednumber(op):
    #Take a number as an input and compere to a random number and call a function for printing the resault

    if op == 'm':
        count = 1
        answer = random_number()
        while count <= 3:
            print('Guess a number from 1 to 10')
            guess = int(input())
            if guess != answer:
                if guess < answer:
                    print_guess_status('to low',count)
                    count += 1
                elif guess > answer:
                    print_guess_status('to high',count)
                    count += 1
            else:
                print_guess_status('right',count)
                break

        print('Do you want to play again? y/n')
        answer = input()
        if answer == 'y':
            count_and_compere_guessednumber('m')
        elif answer == 'n':
            from main import main_menu
            main_menu()
        else:
            print('You can onley select y for yes or n for no.')

    else:
        count = 1
        answer = random_number()
        while count <= 3:
            print('Guess a number from 1 to 10')
            guess = int(input())
            if guess != answer:
                if guess < answer:
                    print(f'to low - attempt {count}')
                    count += 1
                elif guess > answer:
                    print(f'to high - attempt {count}')

                    count += 1
            else:
                print("You won!")
                return True

