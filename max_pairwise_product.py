# Maximum pairwise prodcut
# Python 3.4.3
# Date: 11/5/2016
# Author: harryjrocha@gmail.com
# Finds two integers in a sequence that will give the largest product
# Assumes all integers are positive

import random

def maximum_pairwise_product(a):
    # Goes through every possible pair of integers in a list; Naive solution O(n^2)

    result = 0
    for x in range(len(a)):
        for y in range(x + 1, len(a)):
            if a[x] * a[y] > result:
                result = a[x] * a[y]
    return result

def maximum_pairwise_product_fast(a):
    # Finds the two largest integers in a list

    max_index1 = -1 # why are we initializing the index with -1?
    for i in range(len(a)):
        if((max_index1 == -1) or (a[i] > a[max_index1])):
            max_index1 = i
    
    max_index2 = -1
    for j in range(len(a)):
        if((j != max_index1) and ((max_index2 == -1) or (a[j] > a[max_index2]))):
            max_index2 = j

    return a[max_index1] * a[max_index2]

def user_input():
    # Gets list of integers from user

    size = int(input())
    numbers = [int(n) for n in input().split()]
    return numbers

def random_input():
    # Generates random list of integers
    max_list_size = 5
    max_val = 10
    n = random.randint(2, max_list_size)
    numbers = [random.randint(0, max_val) for i in range(n)]
    return numbers

def stress_test():
    # Tests algorithm with a randomly generated list of integers

    while (True):
        a = random_input()
        print(len(a))
        print(a)
        if(run_test(a)):
            break
    return

def manual_test():
    # Tests algorithm with a user generated list of integers

    while(True):
        a = user_input()
        if(run_test(a)):
            break
    return

def run_test(a):
    # Runs both MPP algorithms and determines whether they both give equal results

    result1 = maximum_pairwise_product(a)
    result2 = maximum_pairwise_product_fast(a)
    if(result1 != result2):
        print("Wrong answer: " + str(result1) + ' ' + str(result2))
        return True
    else:
        print("OK")
        return False

# Select the type of test you'd like to run

#stress_test()
#manual_test()