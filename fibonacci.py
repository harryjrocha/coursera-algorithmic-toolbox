# Uses python3
# Fibonacci
# Python 3.4.3
# Date: 11/11/2016
# Author: harryjrocha@gmail.com
# Finds two integers in a sequence that will give the largest product
# Assumes all integers are positive

import random
import time

def calc_fib_naive(n):
    # Slower algorithm for calculating the nth fibonacci number

    if (n <= 1):
        return n

    return calc_fib_naive(n - 1) + calc_fib_naive(n - 2)

def calc_fib_fast(n):
	# Faster algorithm for calculating the nth fibonacci number
    
    fib_list = []
    fib_list.append(0)
    fib_list.append(1)

    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])

    return fib_list[n]

def stress_test():
	# Performs a stress test to compare results from both algorithms

    max_fib = 40
    
    while(True):
        n = random.randint(0, max_fib)
        print("Fibonacci: " + str(n))
        result1 = calc_fib_naive(n)
        result2 = calc_fib_fast(n)
        if(result1 != result2):
            print("Wrong answer: " + str(result1) + ' ' + str(result2))
            break
        else:
            print("OK")

    return

def manual_test():
    # Performs a test with user defined input on both algorithms
    
    n = int(input())
    #start_time = time.clock()
    print(calc_fib_fast(n))
    #print(calc_fib_naive(n))
    #print("--- %s seconds ---" % (time.clock() - start_time))
 
# ------------- Select the type of test you'd like to run:

manual_test()
#stress_test()