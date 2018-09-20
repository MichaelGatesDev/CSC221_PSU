#! /usr/bin/env python3

# Tyler Whitney
# 10/20/2016
# Test suite for lab08

import sys
import lists # import our lab08 lists.py file

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def main():
    """ Run the suite of tests for code in this module (this file).
    """
    test(lists.productOfOdd([1,2,3,4]) == 3)
    test(lists.productOfOdd([2,2,2,2]) == 1)
    test(lists.productOfOdd([1,2,1,2]) == 1)
    test(lists.productOfOdd([4,6,7,8]) == 7)
    test(lists.productOfOdd([1,1,1,3]) == 3)

    test(lists.sumOfEven([1,2,3,4]) == 6)
    test(lists.sumOfEven([2,2,2,2]) == 8)
    test(lists.sumOfEven([1,2,1,2]) == 4)
    test(lists.sumOfEven([4,6,7,8]) == 18)
    test(lists.sumOfEven([1,1,1,3]) == 0)
  
    test(lists.evenMembers([1,2,3,4]) == [2,4])
    test(lists.evenMembers([2,4,6,8]) == [2,4,6,8])
    test(lists.evenMembers([1,2,3,4,5,6,7,8,9,10]) == [2,4,6,8,10])
    test(lists.evenMembers([3,4,5,6]) == [4,6])
    test(lists.evenMembers([10,11,12,14]) == [10,12,14])

    mylist = [1,2,3,4]
    lists.changeList(mylist)
    test(mylist == [1,6,2,12]) # Test 1
    mylist = [4,5,6,7]
    lists.changeList(mylist)
    test(mylist == [12,3,18,4]) # Test 2

    test(lists.isReverse([1,2,3,4],[4,3,2,1]) == True)
    test(lists.isReverse([1,2,3,4],[2,3,2,1]) == False)
    test(lists.isReverse([1,2,3,4],[3,2,1,0]) == False)
    test(lists.isReverse([4,5,6,7],[7,6,5,4]) == True)
    test(lists.isReverse([9,8,7,6],[6,7,8,9]) == True)

if __name__ == '__main__':
    main()
