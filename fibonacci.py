def fibonacci(num):
    a, b = 0, 1
    fib = []

    for i in range(num):
        a, b = b, a + b
        fib.append(a)

    print(fib)
