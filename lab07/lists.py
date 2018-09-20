#! /usr/bin/env python3

# Michael Gates
# 23 October 2017
# Test suite implementations for lab07




# The parameter intList is supposed to be a list of integers.
# The function returns the product of the odd integers from intList, and leaves intList not​ ​modified​.
# For instance, given [1,2,3,4], the function returns 3. 
# The function performs no I/O.
def productOfOdd(intList):
	# if list is empty
	if(len(intList) <= 0):
		return 0
	
	last = 1
	for i in intList:
		if(i % 2 != 0):
			last = last * i
	return last

# The parameter intList is supposed to be a list of integers.
# The function returns the sum of the even integers from intList, and leaves intList not​ ​modified​.
# For instance, given [1,2,3,4], the function returns 6. 
# The function performs no I/O.
def sumOfEven(intList):
	# if list is empty
	if(len(intList) <= 0):
		return 0
	
	sumTotal = 0
	for i in intList:
		if(i % 2 == 0):
			sumTotal = sumTotal + i
	return sumTotal

#The parameter intList is supposed to be a list of integers.
# The function returns​ ​a​ ​new​ ​list​ containing the even integers from intList, in the same order, and
# leaves intList not modified.
# For instance, given [1,2,3,4,2,3,6], the function returns [2,4,2,6].
# The function performs no I/O.
def evenMembers(intList):
	evenList = []
	for i in intList:
		if(i % 2 == 0):
			evenList.append(i)
	return evenList


# The parameter intList is supposed to be a list of integers.
# The function modifies​ intList: 
# 	● For odd integers one (1) is added and then the result is divided by 2
# 	● Even integers are multiplied by 3.
# This function does not return anything. (void)
# For instance, the parameter [1,2,3,4]  should become [1,6,2,12].
# The function performs no I/O.
def changeList(intList):
	for index, value in enumerate(intList):
		if(value % 2 == 0):
			intList[index] = value*3
		else:
			intList[index] = round((value+1) / 2)
	
	
	

# The parameters intListOne and intListTwo are supposed to be lists of integers.
# The function will return​ ​true​ ​if​ intListTwo is the reversed version of intListOne.
# The function will return​ ​false​ ​if​ intListTwo is NOT the reversed version of intListOne.
# The function performs no I/O.
def isReverse(intListOne, intListTwo):
	return intListTwo == intListOne[::-1]


def main():
	pass

if __name__ == '__main__':
	main()
	
