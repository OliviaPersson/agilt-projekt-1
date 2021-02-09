def print_guess_status(string,count):
    #Print if guess is to low/hight or right and amount of guesses taken 
    if string.lower() == "right":
        print("Good job! Your guess is {0} and you managed it in {1} guesses".format(string,count))
    else:    
        print("Your guess is {0} and you have guessed {1} times".format(string,count))
