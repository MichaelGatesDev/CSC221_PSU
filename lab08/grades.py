#! /usr/bin/env python3

# Michael Gates
# 30 October 2017
# Test suite implementations for lab08

GRADE_TRANSLATIONS = {
	"A": (100, 95),
	"B": (94.99, 85),
	"C": (84.99, 75),
	"D": (74.99, 65),
	"F": (64.99, 0),
}
"""
Returns the letter grade 'equivelant' of a number
"""
def getLetter(numGrade):
	result = "?" # unknown
	for key in GRADE_TRANSLATIONS:
		gRange = GRADE_TRANSLATIONS[key]
		gMax = gRange[0]
		gMin = gRange[1]
		if(numGrade >= gMin and numGrade <= gMax):
			result = key
	return result

grades = [
    ("Calculus", [100, 95, 90, 92, 100, 100]),
    ("EarthScience", [100, 50, 55, 0, 35, 85]),
    ("PhysicalEd", [100, 100, 100, 95, 98, 92]),
    ("CompSci", [100, 100, 100, 100, 92, 90]),
    ("Accounting", [90, 90, 90, 92, 85, 100])
]



"""
Returns the mean average of a list of numbers
"""
def listAverage(l, numOfDecs):
	# If provided type is not a list
	if(not type(l) is list):
		return -1
	result = 0
	for item in l:
		result = result + item
	result = result / len(l)
	return round(result, numOfDecs)


"""
Takes a dictionary and returns a modified version of the dictionary where the 'value' is a sum of the previously-provided number array

e.g. passing in {"hi", [1,2,3]} will return {"hi", 6}
"""
def gradesAverage(grades, numOfDecs):
	result = {}
	for item in grades:
		name = item[0]
		valuesList = item[1]
		average = listAverage(valuesList, numOfDecs)
		result[name] = average
	return result
	
	
def printPrettyGrades(dic):	
	for key in dic:
		value = dic[key]
		letter = getLetter(value)
		line = ""
		print("{0:<16} {1:<5} {2:>3}".format(key, value, letter))

def main():
	printPrettyGrades(gradesAverage(grades, 2))

if __name__ == '__main__':
	main()

