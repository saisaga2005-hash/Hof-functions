'''class Inventory:
    total_items=0
    def __init__(self,stock):
        self.stock=dict({})
    def add(self,k,v):
        self.stock[k]=v
        Inventory.total_items+=1
    def remove(self,k):
        self.stock.pop(k)
        Inventory.total_items-=1
    @classmethod
    def change(cls,new):
        cls.threshold=new
    @staticmethod
    def verify(v):
        return Inventory.threshold k=v
I1=Inventory()
I2=Inventory()

#10
class Member:
    BMI_limit=4
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
    def calculate(self):
        cal=self.height/self.weight
        if cal>=self.BMI_limit:
            print("unfit")
        else:
            print("fit")
    @classmethod
    def update(cls,new):
        cls.BMI_limit=new
    @staticmethod


class Student:
     total_students=0
     def __init__(self,name,marks):
         self.name=name
         self.marks=marks
         Student.total_students+=1
     def is_passed(self):
         if (self.marks>=
        Student.passing_marks):
             return "pass"
         else:
             return "fail"
     @classmethod
     def curve_marks(cls,students,percent):
         for s in students:
             s.marks=s.marks+(s.marks*percent/100)
             if s.marks>100:
                 s.marks=100
     @staticmethod
     def grade(marks):
         if marks >=90:
             return 'A'
         elif marks>=75:
             return 'B'
         elif marks>=60:
             return 'C'
         elif marks>=40:
             return 'D'
         else:
             return 'F'
s1=Student("teja",60)
s2=Student("sri",30)
s3=Student("riya",80)
print(Student.total_students)
'''

#Q2. Design a class Product that:
#•	Maintains a base tax rate applicable to all products.
#•	Each product has a name and base price.
#•	Has a method to compute final price including tax.
#•	Can change tax rate for all products using one method.
#•	Includes a function to check whether a given price is valid or not (non-negative and realistic).
#Demonstrate:
#1.	Creating multiple products.
#2.	Changing the tax rate.
#3.	Showing updated prices and validity checks.

'''class Product:
    tax_rate=10
    def __init__(self,name,base_price):
        self.name=name
        self.base_price=base_price
    def final_price(self):
        return self.base_price+(self.base_price * Product.tax_rate/100)
    @classmethod
    def change_tax_rate(cls,new_tax):
        cls.tax_rate=new_tax
    @staticmethod
    def is_valid_price(price):
        return price >=0

p1=Product("teja",200)
p2=Product("sai",700)
print(p1.tax_rate)
print(p1.final_price())
Product.change_tax_rate(30)
print(p1.final_price())
'''
#3. Create an Employee class that:
##•	Keeps a minimum experience required for promotion (shared across all employees).
#•	Stores employee name, experience, and department.
#•	Has a method to check eligibility for promotion.
#•	Provides a function to update promotion criteria globally.
#•	Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
#Demonstrate:
#1.	Creating employees from different departments.
#2.	Changing promotion criteria.
#3.	Displaying eligibility results and department validation

class Employee:
    minimum_experience=2
    def __init__(self,name,experience,department):
        self.name=name
        self.experience=experience
        self.department=department
    def eligibility(self):
        return self.experience >=Employee.minimum_experience

    @classmethod
    def update(cls,new_exp):
        cls.minimum_experience=new_exp
    @staticmethod
    def valid_department(dept):
        valid_department=["HR","Tech","Admin"]
        return dept in valid_department
e1=Employee("vyshu",3,"bca")
e2=Employee("akhi",1,"eee")
print(Employee.minimum_experience)
print(e1.eligibility())
print(e2.eligibility())
Employee.update(4)
print(e1.eligibility())
print(e2.eligibility())
print(e1.valid_department(e1.department))

class Loan:
    interest_rate=200
    def __init__(self,borrower_name,principal):
        self.borrower_name=borrower_name
        self.principal=principal
    def total_amount(self):
        s=self.total_amount+self.interest_rate*Loan.interest_rate
    @classmethod
    def update(cls,new_rate):
        cls.update=new_rate
    @staticmethod
    def check_loan_eligibility(sal):
        return sal>0
l1=Loan("ramu",2000)
l2=Loan("akash",40000)
print(l1.borrower_name,l1.principal)
print(l2.borrower_name,l1.principal)
Loan.update(700)
print(l1.borrower_name,l1.update)
print(l2.borrower_name,l2.update)





















