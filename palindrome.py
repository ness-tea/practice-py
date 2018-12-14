def string():
    string = str(input("Please give me a word : "))
    a = string[::-1]
    if (a == string):
        print("You've given me a palindrome!")
        print(a + " == " + string)
    else:
        print("That ain't no palindrome")
        print(a + " != " + string)
