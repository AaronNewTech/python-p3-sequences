#!/usr/bin/env python3

def print_fibonacci(length):
    fib = list()
    if length == 0:
        print(fib)
    elif length == 1:
        fib.append(0)
        print(fib)
    elif length == 2:
        fib.append(0)
        fib.append(1)
        print(fib)
    elif length > 2:
        fib.append(0)
        fib.append(1)
        for fib_count in range(2, length):
            fib.append(fib[-1] + fib[-2])
        print(fib)
    pass