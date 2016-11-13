# Uses python3
# Fibonacci Last Digit
# Python 3.4.3
# Date: 11/12/2016
# Author: harryjrocha@gmail.com
# Calculates the last digit of the nth Fibonacci number

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1): # why use _? why n - 1?
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, ((previous + current) % 10)

    return current

n = int(input())
print(get_fibonacci_last_digit_fast(n))
