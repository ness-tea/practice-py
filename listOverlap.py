def overlap(a, b):
    overlap = []
    for i in a:
        if (not(i in overlap)) and (i in b):
            overlap.append(i)
            
    print(overlap)
