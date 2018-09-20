#!/usr/bin/env python3
# Michael Gates
# 4 December 2017
# 

class Employee:
    
    def __init__(self, fullName, yearOfHire, monthOfHire, dayOfHire):
        self._fullName = fullName
        self._yearOfHire = yearOfHire
        self._monthOfHire = monthOfHire
        self._dayOfHire = dayOfHire

    def setName(self, name):
        self._fullName = name
        
    def getName(self):
        return self._fullName
        
    def printName(self):
        print(self._fullName)
        
        
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
    
    def __str__(self):
     return "[" + self._fullName + " " + str(self._monthOfHire) + "/" + str(self._dayOfHire) + str(self._yearOfHire) + "]"
    
    
class Supervisor(Employee):
    
    def __init__(self, name, startDate, department):
        year = int(startDate[0:4])
        month = int(startDate[4:6])
        day = int(startDate[6:8])
        Employee.__init__(self, name, year, month, day)
        
        self._department = department       
        self.employees = {}
        self.contact_info = {}
    
    def setName(self, name, department):
        self._fullName = name
        self._department = department
        
    def printName(self):
        print(self._fullName + ", " + self._department)
        
    def getDept(self):
        return self._department
        
    def addEmployees(self, emp):
        self.employees[emp.getName()] = emp
        
    def removeEmployee(self, name):
        if name in self.employees:
            del(self.employees[name])
        else:
            print("Error: Can't remove an employee that isn't hired")
        
    def isManager(self):
        return len(self.employees) > 0
    
    def printEmployeeNames(self):
        for e in self.employees.values():
            e.printName()
            
    def getContactInfo(self):
        return self.contact_info
    
    def setContactInfo(self, phone, fax, email):
        self.contact_info["phone"] = phone
        self.contact_info["fax"] = fax
        self.contact_info["email"] = email
    
    def getPhone(self):
        return self.contact_info["phone"] if "phone" in self.contact_info else ""
    
    def getFax(self):
        return self.contact_info["fax"] if "fax" in self.contact_info else ""
    
    def getEmail(self):
        return self.contact_info["email"] if "email" in self.contact_info else ""
    
if __name__ == "__main__":
    
    print("Creating 'Supervisor' object 'tyler'")
    s = Supervisor("Tyler Whitney", "12212017", "Computing Systems")
    s.printName()
    print("Is Manager? " + str(s.isManager()))
    #print("Service: " + s.getDept())
    print()
    
    print("Creating 'Employee' object 'one'")
    one = Employee("John Doe", 2, 14, 2014)
    one.printName()
    print()
    
    s.addEmployees(one)
    print("Added 'one' as an employee under 'tyler'")
    print("-- Employees under 'tyler' object")
    s.printEmployeeNames()
    print(" ----- ")
    print("Is 'tyler' Manager? " + str(s.isManager()))
    print()
    
    print("Creating 'Supervisor' object 'two' ")
    two = Supervisor("Eric Twofer", "04162002", "Marketing and Communicaitons")
    two.printName()
    print("Changing name of 'two' to a different name and department")
    two.setName("Eric J Twofer", "MarCom")
    two.printName()
    print()
    
    print("Setting contact info for object 'tyler'")
    s.setContactInfo("5642449", "5552400", "whit4763@plattsburgh.edu")
    print("-- Printing Contact Info from 'getContactInfo' method --")
    print(s.getContactInfo())
    
    print("-- Printing Contact Info from individual 'getPhone', 'getFax', 'getEmail' methods --")
    print("Phone: " + s.getPhone())
    print("Fax: " + s.getFax())
    print("Email: " + s.getPhone())
    print()
    
    
    print("Adding 'two' as an employee under 'tyler'")
    s.addEmployees(two)
    print("-- Employees under 'tyler' object --")
    s.printEmployeeNames()
    print(" ----- ")
