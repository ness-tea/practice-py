## File Overlap
#  Finds the numbers that overlap both number lists from each txt file.

def overLap(file1, file2):
    with open(file1, 'r') as open_file:
        list1 = open_file.read().split('\n')
        for i in range(len(list1)):
            list1[i] = int(list1[i])

    with open(file2, 'r') as open_file:
        list2 = open_file.read().split('\n')
        for j in range(len(list2)):
            list2[j] = int(list2[j])
        
    list3 = [x for x in list1 if x in list2]

    return list3

if __name__=="__main__":
    file1 = str(input("Please input the name of the first txt file: "))
    file2 = str(input("Please input the name of the second txt file: "))

    # If the inputs are not 0, use the txt files inputted.
    if file1 != '0' and file2 != '0':
        overlap = overLap(file1, file2)
    # Else use the default txt files for this exercise.
    else:
        overlap = overLap('primenumbers.txt', 'happynumbers.txt')
    print("The following numbers overlap both file number lists: ")
    for num in overlap:
        print(num)
