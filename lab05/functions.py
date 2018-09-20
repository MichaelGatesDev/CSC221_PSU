#! /usr/bin/env python3

# Michael Gates
# 3 October 2017
# Various math functions
import testsuite

def absolute_value(x):
    # return the absolute value of x
    return x if x >= 0 else x * -1  

def is_divisible(x, y):
    # return true if x is divisible by y, false otherwise
    return x % y == 0

def to_power(x, y):
    # return x to the power y
    return x**y

def is_greater(x, y):
    # return true if x is greater than y, otherwise false
    return x > y

def sub_min_max(x, y):
    # return the difference between x and y as a positive integer
    return absolute_value(x - y)

def mymax(x, y):
    # return whichever value is the max, x or y
    return x if x > y else y

# Example of a function that returns the Nth number of the fibonnaci sequence
# The testsuite checks these values as an additional example
def fibo(n):
    a = 0
    b = 1
    for i in range(n):
        c = a
        a = b
        b = c + b
    return a

def main():
    # use this to test your functions
    print("Absolute value of -5 is " + str(absolute_value(-5)))
    print("Is 4 divisible by 2? " + str(is_divisible(4,2)))
    print("5 to the 2nd power is " + str(to_power(5,2)))
    print("Is 5 greater than 15? " + str(is_greater(5,15)))
    print("The (positive) difference between  30 and 4 is " + str(sub_min_max(4,30))) 
    print("The largest of the two numbers 5 and 50 is " + str(mymax(5,50)))
    print("The 7th number in the fibonacci sequence is " + str(fibo(7)))

if __name__ == '__main__':
    main()
