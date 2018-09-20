#!/usr/bin/env python3
# Michael Gates
# 9 November 2017
# Lab10 - Blackout Math


"""
Checks if the sequence (one side of an equation) is evaluable
"""
def isValidSequence(seq):
    try:
        eval(seq)
        return True
    except:
        return False

"""
Computes all of the possible variations of a puzzle
"""
def getValidVariations(puz):
    
    pairs = [
        (i, j) 
        for i in range(len(puz))
        for j in range(i, len(puz))
    ]
    
    variations = [
        ''.join([
            c for idx, c in enumerate(puz) 
            if idx != i and idx != j
        ])
        for i, j in pairs
    ]
    
    # valid with no changes
    if(checkExpression(puz)):
        variations.append(puz)
    
    return [v for v in variations if checkExpression(v)]



# Creates an empty puzzle list, open the puzzles.txt file and
# take each line (one puzzle) and add it to our list of puzzles
# that we need to solve
def getPuzzleList():
    puzzles = []
    f = open('puzzles.txt', 'r')
    for line in f:
        puzzles.append(line.strip())
    return puzzles



    
"""
Checks if both sides (sequences) of an equation evaluable
"""
def checkExpression(exp):
    sides = exp.split("=")
    if(len(sides) < 2):
        return False
    for s in sides:
        if not isValidSequence(s):
            return False
    return eval(sides[0]) == eval(sides[1])



"""
Returns all possible solutions for a puzzle
"""
def getPuzzleSolutions(p):
    
    solutions = []
    variations = getValidVariations(p)
    
    for v in variations:
        if checkExpression(v) and not v in solutions:
            solutions.append(v)
    
    return solutions                    



def main():
        
    puzzles = getPuzzleList()
    
    for p in puzzles:   
        solutions = getPuzzleSolutions(p)
        """ UNCOMMENT TO PRINT ALTERNATE SOLUTIONS WHERE APPLICABLE
        if(len(solutions) > 0):
            for i in range(0, len(solutions)):
                print(str(i+1) + ") " + p + " -> " + solutions[i])
        else:
            print("NO SOLUTION >> " + p)
        """
        if(len(solutions) > 0):
            print(solutions[0])


if __name__ == "__main__":
    main() 
