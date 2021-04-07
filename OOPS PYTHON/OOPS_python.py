#What is OOPS - Coding of objects that are used in your project numerous times so we code it one time by creating class and use it in different parts of project

class Employee:    #Class is a template that contains info that You can use in different context without making it everytime
#These are class variables  
    sal_increment = 2
    no_of_empl = 0
    def __init__(self, fname, lname, salary): #THIS __init__  is CONSTRUCTOR #This instance is for every employee, basic essential info that every employee should have

#These are instance variables 
        self.fname = fname
        self.lname = lname
        self.salary = int(salary) 
        Employee.no_of_empl += 1
        self.sal_increment = 5 #It will be taken before the class Employee by the incrment(), Comment this out to use sal_increment=2
  
    def increment(self):    #THIS IS ANOTHER METHOD 
        self.salary = int(self.salary * self.sal_increment) #Here "self.sal_increment" is present in the instance which is the first place this function will search for "sal_incrment" if its not in it it will go for main class Employee and search. 
        # So if you comment OUT "self.sal_increment" in increment() it will still work coz 
        # its present in class Employee():

#THIS IS DRIVER CODE 
print(Employee.no_of_empl)
ankit = Employee('Ankit', 'Jha', '1200000')  #OBJECTS  
billi = Employee('Billi', 'Jackson', '1200000') #OBJECTS


print(Employee.__dict__)#TO display directory of class
print("All information of Employee:",ankit.__dict__)   #To display whole directory of employee name Ankit
print("Name of Employee:",ankit.fname)
print("Number of Employees:",Employee.no_of_empl)
print("Old salary:",ankit.salary)
ankit.increment()
print("New salary:",ankit.salary)


 