# l=[[1,2],[3,4],[5,6]]
# k=list(map(lambda x:x.append(5), l))
# print(k)


# d={"apple":100, "banana":40, "cherry":150}
# print(d.keys())
# print(d.values)
# print(d.items())
# f=dict(filter(lambda x:x[1]>50,d.items()))
# print(f)


# k=input()
# print(k.split())
# print(type(k))



#
# k=list(map(int,input().split()))
# m=10**6
# for i  in k:
#     if m<i:
#         m=i
# from functools import reduce
# print(reduce(lambda x, y: x if  x>y else y,k))




# #4th question
# k= reduce(lambda x,y:x+y,[1,2,3])


'''class Profile:
    def __init__(self ,username):
        self.followers=0
        self. username=username
    def follow(self):
        print("someone followed you")
        self.followers+=1
    def update_username(self,nun):
        self.username=nun
        print("your follower count is 2")
P1=Profile("saitejasri")
P1.follow()
print(P1.followers)
P1.update_username("saitejasri")
print(P1.username)'''


'''class Person:
    total_phones=0
    def __init__(self, name,age,phone):
        self.name=name
        self.age=age
        self.phone=phone
        if phone:
            Person.total_phones+=1
p1=Person("Teja",19,True)
print(p1.total_phones)
p2=Person("mouni",12,False)
print(p2.total_phones)'''





'''class Building:
    no_of_rooms=10
    total_buildings=0
    def __init__(self ,name,wifi):
        self.bname=name
        self.wifi=wifi
        Building.total_buildings+=1
b1=Building("Main Building",True)
print(b1.total_buildings)
b2=Building("Python building",False)'''

'''def change_rooms(self,nor):
    Building.no_of_rooms=nor #using method

'''


'''class Movie:
    lauguage="telugu"
    def __init__(self,director,hero,tp):
        self.director=director
        self.hero=hero
        self.ticket_price=tp
    def collections(self,tickets):
        return self.ticket_price*tickets
    def Dub(self,new_lang):
        self.lang=new_lang
bahubali=Movie("SSR","PB",350)
bahubali.collections(10000000)
print(bahubali.ticket_price)
bahubali.Dub("Hindi")
Spirit=Movie("SRV","PB",500)
print(Spirit.ticket_price)
print(bahubali.lang)
'''

'''class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        return self.marks>40
Student1=Student("sai","60")
Student2=Student("tej","90")
if Student1.is_passed:
    print("Student.name has passed")
else:
    print("Student.name has failed")
'''


'''class Course:
    total_students=30
    def __init__(self,student_name):
        self.name= student_name
    @classmethod
    def show_total(cls,new):
            cls.total_students=new
    def enroll(total_students):
            self.+= total_students
    @staticmethod
    def is_eligible(self,age):
         if age >=18:
             return True
b1=Course("sai")
b2=Course("Teja")
print(b1.enroll(60))
print(Course. is_eligible())

class Student:
    def __init__(self, name,marks)
        self.name="teja"
        self.marks="60"
    def is_passed(self,):
        return self.marks
'''
'''class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        return self.marks>40
s1=Student("sai",70)
s2=Student("maro",30)
print(s1.is_passed())
if s1.is_passed():
    print(s1.name,"has passed")
else:
    print(s1.name,"has failed")
if s2.is_passed():
    print(s2.name,"has passed")
else:
    print(s2.name,"has failed")'''

'''class Employee:
    company_name="TechCorp"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
e1=Employee("teja")
e2=Employee("moka")
Employee.change_company("Innotech")
print(e1.company_name)
print(e2.company_name)'''

'''class MathOps:
    @staticmethod
    def is_even(num):
        return num%2==0
print(MathOps.is_even(8))#calling using class
m1=MathOps #creating object
print(m1.is_even(7))'''

'''class Car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=mileage
    def display_specs(self):
        print("Mileage:", self.mileage)
        print("Wheels:",Car.wheels)
    @classmethod
    def change_wheels(cls,new_wheels):
        cls.wheels=new_wheels
c1=Car(9)
Car.change_wheels(6)
c1.display_specs()'''

'''class Book:
    total_books=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        Book.total_books+=1
    @classmethod
    def from_string(cls,book_str):
        title,author=book_str.split("-")
        return cls(title, author)
    @staticmethod
    def is_valid_title(title):
        return len(title)>=3
b1=Book("python","Gudio")
b2=Book("Java","John")
print("Total books:",Book.total_books)
print(b2.is_valid_title("Java"))
print(b1.is_valid_title("Python"))
b3=Book.from_string("Python-Gudio")
print(b3.title, b3.author)
'''

'''class Employee:
    bonus_rate=0.1
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def final_salary(self):
        return self.base_salary + (self.base_salary * self.bonus_rate)
    @classmethod
    def update_bonus(cls,new_rate):
        cls.update_bonus=new_rate
    @staticmethod
    def is_valid_salary(sal):
        return sal>0
E1=Employee("teja",29000)
E2=Employee("bantu",50000)
Employee.update_bonus(0.9)
print(E1.final_salary())
'''

class Course:
    total_students=0
    def __init__(self,student_name):
        self.student_name=student_name
    def enroll(self):
        Course.total_students+=1
    @classmethod
    def show_total(cls):
        print(cls.total_students)
    @staticmethod
    def is_eligible(age):
        if age>=18:
            return True
        else:
            return False
c1=Course("teja")
c2=Course("srija")
c1.enroll()
c2.enroll()
Course.show_total()

'''class BankAccount:
    bank_name="SBI"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        self.deposit=amount
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    @staticmethod
    def validate_amount(amount):
        if amount>0:
            return True
        else:
            return False
b1=BankAccount("sai",2000)
b2=BankAccount("tej",3000)
BankAccount.change_bank_name("ABS")
'''


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        return self.marks>40
s1=Student("sai",70)
s2=Student("teja",50)
print(s1.is_passed())
if s1.is_passed:
    print(s1.name,"has passed")
else:
    print(s2.name,"has failed")
if s2.is_passed:
    print(s1.name,"has passed")
else:
    print(s2.name,"has failed")


#2
class Employee:
    company_name="Techcorp"
    def __init__(self,company_name):
        self.company_name=company_name
    @classmethod
    def change_company(cls,new_name):
        cls.change_company=new_name
e1=Employee("teja")
e2=Employee("moka")
Employee.change_company="cvcorp"
print(e1.change_company)
print(e2.change_company)







