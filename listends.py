def listends(a):
    b = [x for x in a if x == a[0] or x == a[len(a)-1]]
    print(b)
