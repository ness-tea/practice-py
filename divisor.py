def divisor():
    num = int(input("What's your favourite number? : "))
    for i in range(1, num+1):
        if ((num % i) == 0):
            print(str(i) + " is a divisor of " + str(num))
        
