def removedupsloop(a):
    list = []

    for x in a:
        if x not in list:
            list.append(x)

    print(list)

def removedupsset(a):
    list = set(a)

    print(list)

def listOverlapSet(a,b):
    list1 = set(a)
    list2 = set(b)

    list3 = list1.intersection(list2)

    print(list3)
    
