#!/usr/bin/env python3
# Michael Gates
# 26 November 2017
# Example of object/classes


class Employee:
    
    
    
    def __init__(self, fullName, yearOfHire, monthOfHire, dayOfHire):
        self._fullName = fullName
        self._yearOfHire = yearOfHire
        self._monthOfHire = monthOfHire
        self._dayOfHire = dayOfHire

    def printName(self):
        print(self._fullName)
        
    def setName(self, name):
        self._fullName = name
        
    """
    in the format “yyyymmdd”. 
    This method will parse the string, convert each number to an int, 
    and then set the corresponding instance variables to the correct values
    (year of hire, month of hire, and day of hire)
    """
    def setStartdateString(self, rawDate):
        year = int(rawDate[0:4])
        month = int(rawDate[4:6])
        day = int(rawDate[6:8])
        
        self._yearOfHire = year
        self._monthOfHire = month
        self._dayOfHire = day
    


def main():
    
    # EMPLOYEE A
    empA = Employee("Michael Gates", 2017, 11, 27)
    empA.printName()
    dateStrA = str(empA._monthOfHire) + "/" + str(empA._dayOfHire) + "/" + str(empA._yearOfHire)
    print("Start date: " + dateStrA)
    # CHANGE NAME
    empA.setName("Mitchel Bates")
    # CHANGE START DATE
    empA.setStartdateString("20181221")
    empA.printName()
    dateStrA = str(empA._monthOfHire) + "/" + str(empA._dayOfHire) + "/" + str(empA._yearOfHire)
    print("Start date: " + dateStrA)
    
    print()
    
    # EMPLOYEE B
    empB = Employee("Richard Nameson", 1994, 4, 3)
    empB.printName()
    dateStrB = str(empB._monthOfHire) + "/" + str(empB._dayOfHire) + "/" + str(empB._yearOfHire)
    print("Start date: " + dateStrB)
    # CHANGE NAME
    empB.setName("Richie Sameson")
    empB.printName()
    # CHANGE START DATE
    empB.setStartdateString("19910509")
    dateStrB = str(empB._monthOfHire) + "/" + str(empB._dayOfHire) + "/" + str(empB._yearOfHire)
    print("Start date: " + dateStrB)
    
    

if __name__ == "__main__":
    main() 
