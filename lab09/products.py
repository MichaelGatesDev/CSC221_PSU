#!/usr/bin/env python3
# Michael Gates
# 6 November 2017
# Binary Search

# Function to read the names and serials into lists
def getLists():
    infile  = open("products.txt",'r')
    line =  infile.readline()

    names = []
    numbers = []

    while line  != "":
        line = line.strip()
        name, number = line.split(',')
        names = names + [name]
        numbers = numbers + [number]
        line = infile.readline()

    infile.close()
    return names, numbers

# Function to find the name and return the associated phone number
# You must complete this function!
def binarySearch(names, serials, name):
    # left  side of list
    left =  0
    # right side of the list
    right = len(names) - 1
    while(left <= right):
        # middle of list
        mid = (left + right) // 2
        if names[mid] == name:
            return serials[mid]
        elif names[mid] > name:
            right = mid - 1
        else:
            left = mid + 1
    return "not found"

# Main Function
def main():
    # Get the lists (tuple)
    names,  serials = getLists()
    # Get the name  to search for
    theName = input("Enter  the product name to search for: ")

    # Find  the phone number for the given name
    serialNum = binarySearch(names, serials, theName)
    print("The  product number for ", theName, " is ", serialNum)

if __name__ == "__main__":
    main()