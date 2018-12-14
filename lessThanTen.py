def LessThanTen(a):
    x = []
    for i in a:
        if (i < 5):
            x.append(i)
            print(str(i) + '\n')

## To accomplish this func in one line, print([x for x in a if x<5])
#   where output = x, element of list = x, array = a, condition = x < 5

        
