import random
import sys

def guess():
    print("---- Guessing Game ----" + '\n')
    print("Guess a number between 1 and 9 (including 1 and 9). Get it right & you win!")
    start = str(input('\n' + "Ready to play? (Y/N) : "))

    if (start[0] == 'Y' or start[0] == 'y'):

        ans = random.randint(1, 9)
        attempts = 0
        
        while (True):
            guess = input('\n' + "Guess a number between 1 and 9 : ")

            try:
                val = int(guess)
                if int(guess) < ans:
                    print('\n' + "A little too low...")
                    attempts += 1
                elif int(guess) > ans:
                    print('\n' + "A little too high...")
                    attempts += 1
                elif int(guess) == ans:
                    attempts += 1
                    print('\n' + "You won! In %s tries. Let's play again :)" % str(attempts))
                    ans = random.randint(1, 9)
                    attempts = 0
            except ValueError:
                if (str(guess)[0] == 'e' or str(guess)[0] == 'E'):
                    print('\n' + "Exiting game!")
                    sys.exit()
                else:
                    print("Not a valid input... Let's try again")

    elif (start[0] == 'N' or start[0] == 'n'):
        print('\n' + "Okay, come back next time! :) ")
        sys.exit()

    else:
        print('\n' + "Not a valid answer... but will take that as a no. Good day :) ")
        sys.exit()
