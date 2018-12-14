def reverseString():
    string = str(input("Hi! Type in a sentence about your day :) : "))

    list1 = string.split()
    list2 = [x for x in list1[::-1]]

    newString = " ".join(list2)

    print(newString)

