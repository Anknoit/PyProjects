#What is OOPS - Coding of objects that are used in your project numerous times so we code it one time by creating class and use it in different parts of project

class Employee:    #class is a template that contains info that You can use in different context without making it everytime
    sal_increment = 2
    no_of_empl = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = int(salary) 
        Employee.no_of_empl += 1
        self.sal_increment_init = 2
  
    def increment(self):
        self.salary = int(self.salary * Employee.sal_increment) #Here since we have only taken "sal_increm" it will first search in def__init__ which is known as "Instance" for sal_increment if it does not find any it will go to main clas Employee
        # self.salary = self.salary * self.sal_increment_init  #For checking purpose to know where it goes first

print(Employee.no_of_empl)
ankit =Employee('Ankit', 'Jha', '1200000')
billi =Employee('Billi', 'Jackson', '1200000')

print(Employee.__dict__)#TO display directory of class
print("All information of Employee:",ankit.__dict__)   #To display whole directory of employee name Ankit
print("Name of Employee:",ankit.fname)
print("Number of Employees:",Employee.no_of_empl)
print("Old salary:",ankit.salary)
ankit.increment()
print("New salary:",ankit.salary)


 