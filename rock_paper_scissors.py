import sys

def rps():
    print('\n' + "---- ROCK PAPER SCISSORS ----" + '\n')
    print("How to play:" + '\n')
    print(" (1) When prompted, Player 1 will input their play of either rock, paper, or scissors.")
    print(" (2) Likewise, when prompted, Player 2 will input their play.")
    print(" (3) Winner will be announced subsequently, with a choice to play again.")
    print(" (4) Remember, Rock beats Scissors, Scissors beats Paper, and Paper beats Rock!" + '\n')

    start = str(input("Ready to start the game? (Y/N) : "))

    if (start[0] == 'Y' or start[0] == 'y'):

        while (True):
            p1 = str(input('\n' + "Player 1, what do you choose? : "))
            p2 = str(input("Player 2, what do you choose? : "))


            if (((p1[0] == 'r' or p1[0] == 'R') and (p2[0] == 's' or p2[0] == 'S')) or
                ((p1[0] == 's' or p1[0] == 'S') and (p2[0] == 'p' or p2[0] == 'P')) or
                ((p1[0] == 'p' or p1[0] == 'P') and (p2[0] == 'r' or p2[0] == 'R'))):

                print('\n'+ "Congratulations Player 1; you win!" + '\n')

            elif (((p2[0] == 'r' or p2[0] == 'R') and (p1[0] == 's' or p1[0] == 'S')) or
                ((p2[0] == 's' or p2[0] == 'S') and (p1[0] == 'p' or p1[0] == 'P')) or
                ((p2[0] == 'p' or p2[0] == 'P') and (p1[0] == 'r' or p1[0] == 'R'))):

                print('\n' + "Congratulations Player 2; you win!" + '\n')

            else:
                print('\n' + "Uh oh... it's a draw...." + '\n')

            play_Again = str(input("Would you like to play again? (Y/N) : "))

            if (play_Again[0] == 'n' or play_Again[0] == 'N'):
                break

    elif (start[0] == 'N' or start[0] == 'n'):
        print("Your loss, but thanks anyway. Come back again soon ;)")
        sys.exit()
        
    
