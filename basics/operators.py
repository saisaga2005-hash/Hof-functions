#Arithmetic operators
'''| Operator | Meaning        | Example |
| -------- | -------------- | ------- |
| +        | Addition       | a + b   |
| -        | Subtraction    | a - b   |
| *        | Multiplication | a * b   |
| /        | Division       | a / b   |
| %        | Modulus        | a % b   |
| //       | Floor Division | a // b  |
| **       | Exponent       | a ** b  |'''
a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)


#relational operators
'''| Operator | Meaning               |
| -------- | --------------------- |
| >        | Greater than          |
| <        | Less than             |
| >=       | Greater than or equal |
| <=       | Less than or equal    |
| ==       | Equal to              |
| !=       | Not equal to          |
'''
a = 10
b = 20
print(a > b)
print(a < b)
print(a == b)
print(a != b)

#Logical operators
'''| Operator | Meaning                |
| -------- | ---------------------- |
| and      | Both conditions true   |
| or       | Any one condition true |
| not      | Reverse condition      |
'''
a = 10
b = 20
print(a > 5 and b > 10)
print(a > 15 or b > 10)
print(not(a > 5))

#Assignment operators
'''| Operator | Example |
| -------- | ------- |
| =        | a = 10  |
| +=       | a += 5  |
| -=       | a -= 5  |
| *=       | a *= 5  |
| /=       | a /= 5  |'''
a = 10
a += 5
print(a)
a -= 2
print(a)
a*=3
print(a)
a/=2
print(a)
a%=2
print(a)

#Bitwise operators
'''| Operator | Meaning     |
| -------- | ----------- |
| &        | AND         |
| |        | OR          |
| ^        | XOR         |
| ~        | NOT         |
| <<       | Left Shift  |
| >>       | Right Shift |'''

a = 5
b = 3
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)

#membership operators
'''| Operator | Meaning     |
| -------- | ----------- |
| in       | Present     |
| not in   | Not present |
'''
name = "Python"
print("P" in name)
print("z" not in name)

#identity operators
'''| Operator | Meaning          |
| -------- | ---------------- |
| is       | Same object      |
| is not   | Different object |'''
a = [1, 2]
b = a
c = [1, 2]
print(a is b)
print(a is c)
print(a is not c)

#combined operators
a = 15
b = 4
print("Arithmetic:", a + b)
print("Relational:", a > b)
print("Logical:", a > 10 and b < 5)
a += 5
print("Assignment:", a)
print("Membership:", "P" in "Python")