#if statement
age=25
print("hii")
if age>=18:
    print("welcome")
    print("eligible")
    print("issued")
print("thankyou")
print("bye")

#if-else:
'''if condition:
    statements
else:
    statements'''
num = 5
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#if-else-if
'''if condition:
    statements
elif condition:
    statements
else:
    statements'''
marks = 80
if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
else:
    print("C Grade")

#nested if
age = 20
citizen = True
if age >= 18:
    if citizen == True:
        print("Eligible to vote")
a,b,c=2,3,5
if a>b:
    if a>c:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b>c:
        print("b is greater")
    else:

        print("c is greater")