##  Guess Game 2.0
#   The program will prompt the user to think of a number from 1-100. It will guess the user's
#   number with provided feedback on whether their number is lower or higher than the guess.

import sys

def guessGame(ans, guess):
    if ans[0] == "h" or ans[0] == "H":
        offset = (guess[2] - guess[0]) // 2 
        guess[1] = guess[0]
        guess[0] += offset
    elif ans[0] == "l" or ans[0] == "L":
        offset = (guess[0] - guess[1]) // 2
        guess[2] = guess[0]
        guess[0] -= offset

    return guess

if __name__=="__main__":
    print("----- GUESSING GAME 2.0 -----")
    print("Welcome back! Gonna be guessing your number instead of you guessing mine." + '\n')
    begin = str(input("Shall we begin? (Y/N): "))

    if begin[0] == "y" or begin[0] == "Y":
        ready = str(input('\n' + "Great! Think of a number between 1-100. Hit Enter when you've thought of one. "))
        if ready == "":
            correct = False
            num_guesses = 0

            # Tuple that stores the guess, the low boundary, and high boundary
            guess = [50, 0, 100]

            while not correct:
                ans = str(input('\n' + "Is it " + str(guess[0]) + "? (Yes/Higher/Lower): "))
                if ans[0] == "Y" or ans[0] == "y":
                    num_guesses +=1
                    print("Yay! I won after " + str(num_guesses) + " guesses.")
                    break
                guess = guessGame(ans, guess)
                num_guesses += 1

    else:
        print("Okay, maybe next time. Have a great day!" )
        sys.exit()
