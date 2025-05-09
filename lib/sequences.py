#!/usr/bin/env python3

def print_fibonacci(length):
    """ 
    Print the Fibonacci sequence up to a given length."""
    if length <= 0:
        print([])
        return

    fib_sequence = [0, 1]
    for i in range(2, length):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    print(fib_sequence[:length])


   
    

