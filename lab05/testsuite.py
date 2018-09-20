#! /usr/bin/env python3

# Tyler Whitney
# 02/09/2017
# Test suite for lab05

import sys
import functions # import our lab04 functions.py file

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def main():
    """ Run the suite of tests for code in this module (this file). """
    test(functions.absolute_value(17) == 17)
    test(functions.absolute_value(-17) == 17)
    test(functions.absolute_value(0) == 0)
    test(functions.absolute_value(3.14) == 3.14)
    test(functions.absolute_value(-3.14) == 3.14)
  
    test(functions.is_divisible(6, 4) == False)
    test(functions.is_divisible(6, 3) == True)
    test(functions.is_divisible(10, 5) == True)
    test(functions.is_divisible(10, 2) == True)
    test(functions.is_divisible(2, 3) == False)

    test(functions.to_power(5, 10) == 9765625)
    test(functions.to_power(10, 5) == 100000)
    test(functions.to_power(7, 3) == 343)
    test(functions.to_power(2, 5) == 32)
    test(functions.to_power(25, 1) == 25)
    test(functions.to_power(101, 0) == 1)
    test(functions.to_power(5, 4) == 625)

    test(functions.is_greater(10, 5) == True)
    test(functions.is_greater(200, 1) == True)
    test(functions.is_greater(1, 2) == False)
    test(functions.is_greater(-10, 10) == False)
    test(functions.is_greater(-25, -10) == False)

    test(functions.sub_min_max(5, 10) == 5)
    test(functions.sub_min_max(10, 5) == 5)
    test(functions.sub_min_max(7, 3) == 4)
    test(functions.sub_min_max(2, 5) == 3)
    test(functions.sub_min_max(25, 100) == 75)
    test(functions.sub_min_max(-5, 10) == 15)
    test(functions.sub_min_max(-10, -25) == 15)

    test(functions.mymax(10, 5) == 10)
    test(functions.mymax(200, 1) == 200)
    test(functions.mymax(1, 2) == 2)
    test(functions.mymax(-10, 10) == 10)
    test(functions.mymax(-25, -10) == -10)

    test(functions.fibo(4) == 3)
    test(functions.fibo(5) == 5)
    test(functions.fibo(17) == 1597)
    test(functions.fibo(13) == 233)
    test(functions.fibo(23) == 28657)
    test(functions.fibo(26) == 121393)
    test(functions.fibo(75) == 2111485077978050)

if __name__ == '__main__':
    main()
