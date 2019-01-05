def maxOfThree(array):
    maxNum = 0
    print(array)
    
    if array[0] > array[1]:
        if array[0] > array[2]:
            maxNum = array[0]
        else:
            maxNum = array[2]
    elif array[1] > array[0]:
        if array[1] > array[2]:
            maxNum = array[1]
        else:
            maxNum = array[2]
    elif array[2] > array[0]:
        if array[2] > array[1]:
            maxNum = array[2]
        else:
            maxNum = array[1]

    return maxNum

if __name__=="__main__":
    threeNums = str(input("Please type in 3 numbers separated by spaces: "))
    array = threeNums.split()

    for i in range(3):
        array[i] = int(array[i])

    largestNum = maxOfThree(array)
    print("The largest number is " + str(largestNum) + ".")
