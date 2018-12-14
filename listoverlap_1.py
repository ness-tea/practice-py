def listoverlap(list1, list2):
    list3 = [x for x in list1 if x in list2]
    list_overlap = []
    
    for x in list3:
        if not(x in list_overlap):
            list_overlap.append(x)

    print(list_overlap)
