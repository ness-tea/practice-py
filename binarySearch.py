# Binary Search

# Program will prompt user to input an ordered sequence of numbers (with no spaces)
# and convert the string input into a List.
# Next, it prompts the user to input an element to search the sequence for.
# Outputs whether the inputted element was found.
def binarysearch(List, elem):
    found = False
    
    if len(List) > 1:
        mid = len(List)//2
    else:
        mid = 0
        
    if len(List) > 0:
        if List[mid] == elem:
            found = True
        elif List[mid] > elem:
            List = List[0:mid]
            found = binarysearch(List, elem)
        elif List[mid] < elem:
            List = List[(mid+1):len(List)]
            found = binarysearch(List, elem)
        else:
            found = False
    else:
        found = False

    return found

if __name__=="__main__":
    while True:
        user_list = list(input("Please enter a sequence of numbers (no spaces): "))
        print(user_list)
        element = str(input("Please enter an element to search the sequence: "))
        print("Binary search time!")
        found = binarysearch(user_list, element)

        if (found):
            print(str(element) + " was found!")
        else:
            print(str(element) + " was not found.")
    
    
