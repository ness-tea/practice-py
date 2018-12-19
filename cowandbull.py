# Program that plays the game 'Cows and Bulls' with the user. The game does
# the following:

# Randomly generate a 4-digit number. It then asks the user to make a guess.
# Compares the 4-digit number with the user's guess.
# For every correct digit in the user's guess that's also at the right index,
# they'll receive 1 cow.
# For every correct digit in the user's guess that's at the wrong index, they'll
# receive 1 bull.
# At the end of every guess, the program will return to the user the amount of
# cows and the amount of bulls they have.
# The program will continue to prompt the user for guesses until they arrive at
# the correct guess.
# Author: Vanessa Truong

import random
import sys

def bulls(guess, num):
    # Iterate through 'guess' indices to find all bulls (correct digits at the
    # wrong indices). Ignore all 'cow' placeholders.
    bull = 0
    for i in range(len(guess)):
        if guess[i] in num:
            bull += 1
            index = num.index(guess[i])
            del(num[index])
    return bull

def cows(guess, num):
    guess, num = list(guess), list(num)
    cow = 0

    # Iterate through 'guess' digits to find all cows first. Put placeholders
    # at the indices so they will not be read again when looking for bulls.
    for i in range(4):
        if guess[i] == num[i]:
            cow += 1
            guess[i],num[i] = '',''

    guess = [digit for digit in guess if digit != '']
    num = [digit for digit in num if digit != '']

    bull = bulls(guess, num)
    return cow, bull

        

if __name__=="__main__":
    print('\n' + "---------- COWS & BULLS ----------" + '\n')
    print("The How-to-play's:")
    print("I'll generate a random 4-digit number. Your job is to guess what" + '\n'
          + "this number is. You'll get an infinite amount of chances. For every" + '\n'
          + "CORRECT DIGIT that you guess IN THE RIGHT PLACE, I'll give you a cow." + '\n'
          + "For every CORRECT DIGIT that you guess IN THE WRONG PLACE, I'll give you a bull."
          + '\n' + "So, to summarize:" + '\n')
    print("(1) You get an infinite amount of chances to guess the 4-digit number.")
    print("(2) For every CORRECT DIGIT you guess in the RIGHT PLACE, you get a cow.")
    print("(3) For every CORRECT DIGIT you guess in the WRONG PLACE, you get a bull.")
    print("(4) The game ends when you guess the correct number.")

    start = str(input('\n' + "Are you ready to start? (Y/N): "))

    if start[0] == 'y' or start[0] == 'Y':
        newGame = True
        while (True):
            if (newGame):
                attempts = 0
                num = ""
                for i in range(4):
                    num += str(random.randint(1,9))
                    newGame = False
                print(num)
                    
            guess = str(input("Guess a 4-digit number: "))
            num_dup = num

            # calls cow(), which will handle the game logics for cows and bulls
            cow, bull = cows(guess, num_dup)
    
            if cow == 4 and bull == 0:
                attempts += 1
                if attempts > 1:
                    print(str(cow) + " cows.... you won! (After " + str(attempts) + " attempts)")
                else:
                    print(str(cow) + " cows.... you won! (After " + str(attempts) + " attempt)")

                response = str(input("Play again? (Y/N): "))
                if response[0] == 'y' or response[0] == 'Y':
                    newGame = True
                if response[0] == 'n' or response[0] == 'N':
                    print("Thanks for playing!")
                    sys.exit()
                
            else:
                print(str(cow) + " cows, " + str(bull) + " bulls.")
                attempts += 1
            
    elif start[0] == 'n' or start[0] == 'N':
        print("Thanks for playing! :)")
        sys.exit()

    else:
        print("Not a valid response... goodbye!")
        sys.exit()
                        
    
          

