import sys

def oddeven():
    print("---- The ODD/EVEN Machine ----")
    print("Hi! I can check two things for you: ")
    print("(1) Whether your number is even or odd.")
    print("(2) Whether your first number is a multiple of your second number." + '\n')
    answer = int(input("Which option are you picking? (1/2): "))

    if answer == 1:
        num = int(input('\n' + "Enter a number: "))

        if num % 2 == 1:
            print("Your number is odd!")
        elif num % 2 == 0:
            if num % 4 == 0:
                print("Your number is even... and divisible by 4! BONUS!")
            else:
                print("Your number is even!")
    elif answer == 2:
        num1 = int(input('\n' + "Enter your first number: "))
        num2 = int(input('\n' + "Enter your second number: "))

        if num1 % num2 == 0:
            print("Your second number divides evenly by your first number!")
        else:
            print("Your second number does not divide evenly by your first number.")
    else:
        print("Not a valid option... have a good day :)")
        sys.exit()
                   
                  

    
