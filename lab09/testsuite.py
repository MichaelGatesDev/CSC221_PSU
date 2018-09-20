#! /usr/bin/env python3

# Tyler Whitney
# 11/10/2016
# Test suite for lab09

import sys
import products

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
    names = ["Airheads", "Asparagus", "Donuts", "Drinks", "Glitter", "Hose", "Juice", "Kite", "Lamp", "Lipstick", "Lollipop", "Map", "Mints", "Onions", "Table", "Trampoline"]
    product = ["004345549", "009953344", "003343344", "00935783", "003993310", "004379385", "005583044", "003346645", "003394434", "004023571", "003342343", "004773327", "009943377", "004453234", "009934432", "004334045"]

    test(products.binarySearch(names, product, "Airheads") == "004345549")
    test(products.binarySearch(names, product, "Asparagus") == "009953344")
    test(products.binarySearch(names, product, "Donuts") == "003343344")
    test(products.binarySearch(names, product, "Drinks") == "00935783")
    test(products.binarySearch(names, product, "Glitter") == "003993310")
    test(products.binarySearch(names, product, "Hose") == "004379385")
    test(products.binarySearch(names, product, "Juice") == "005583044")
    test(products.binarySearch(names, product, "Kite") == "003346645")
    test(products.binarySearch(names, product, "Lamp") == "003394434")
    test(products.binarySearch(names, product, "Lipstick") == "004023571")
    test(products.binarySearch(names, product, "Lollipop") == "003342343")
    test(products.binarySearch(names, product, "Map") == "004773327")
    test(products.binarySearch(names, product, "Mints") == "009943377")
    test(products.binarySearch(names, product, "Onions") == "004453234")
    test(products.binarySearch(names, product, "Table") == "009934432")
    test(products.binarySearch(names, product, "Trampoline") == "004334045")
    test(products.binarySearch(names, product, "Aart") == "Not found" or products.binarySearch(names, product, "Aart") == "Not Found" or products.binarySearch(names, product, "Aart") == "not found")
    test(products.binarySearch(names, product, "Zebra") == "Not found" or products.binarySearch(names, product, "Zebra") == "Not Found" or products.binarySearch(names, product, "Zebra") == "not found")

if __name__ == '__main__':
    main()