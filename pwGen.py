import random
import requests
import sys

def password():
    # Remote accessing a txtfile with list of words using requests library
    dictionary = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(dictionary)
    Words = response.content.splitlines()
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    special = ['!','@','#','$','%','&','*']
    
    print('\n' + "------- PASSWORD GENERATOR -------")
    print('\n' + "Welcome... to the password generator,"
          + '\n' + 'Where all your passwords are generated... with care.'
          + '\n' + 'Weak, Strong, Short, Long,'
          + '\n' + 'Our library has it all :)' + '\n')

    print("Let's start off with determing a password strength. When prompted,"
          + '\n' + 'please answer with one of the following options:' + '\n')
    print("(1) Weak")
    print("(2) Medium")
    print("(3) Strong")

    retry = True
    while(retry):
        strength = str(input('\n' + "So, what will it be? : "))

        password = ""
        if not(strength[0] == 's' or strength[0] == 'S') or strength == "1" or strength == "2":
        
            index = random.randint(0, len(Words)-1)
            word = str(Words[index])
            ref = word[3:len(word)-1]
            password += ref

            # For medium passwords, append numbers to the end
            if strength[0] == 'm' or strength[0] == 'M':

                numNum = random.randint(1,2)

                for i in range(numNum):
                    index = random.randint(0, len(numbers)-1)
                    password += numbers[index]

            print("Password: " + password)

        elif strength[0] == 's' or strength[0] == 'S' or strength == "3":
            numWords = random.randint(1,2)
            capLetters = random.randint(3,4)
            numNum = 2
            lenWordSect = 0

            for w in range(numWords):
                index = random.randint(0, len(Words)-1)
                word = str(Words[index])
                ref = word[3:len(word)-1]
                password += ref
                lenWordSect = len(password)

            for n in range(numNum):
                index = random.randint(0, len(numbers)-1)
                password += numbers[index]

            # For strong passwords, append a special char to the end
            password += special[random.randint(0,len(special)-1)]

            for c in range(capLetters):
                index = random.randint(0,lenWordSect - 1)

                chars = list(password)
                chars[index] = chars[index].upper()
                password = "".join(chars)

            print("Password: " + password)


        ans = str(input('\n' + "Would you like to make another password? (Y/N): "))

        if ans[0] == 'Y' or ans[0] == 'y':
            retry = True
        else:
            retry = False
            print("Hope I serviced you well :) ")
            sys.exit()

if __name__ =="__main__":
    password()
        
            
        
            
            
        
        
            

    
