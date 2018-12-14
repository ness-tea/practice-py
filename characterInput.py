def hundred():
        name = str(input("What's your name my dude? : "))
        age = int(input("How old are you? : "))
        year = int(input("I lose track of time, what year is it? : "))
        dif = 100-age
        answer = str(year + dif)
        print(name + ", you'll turn 100 in " + answer +". Congratulations on being so old!" + '\n')
        numOfTimes = int(input("But one last question... what's your favourite number? (Think BIG ;]) : "))
        for i in range(numOfTimes):
            print("SPAMMING TIME" + '\n')
