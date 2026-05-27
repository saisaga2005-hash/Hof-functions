#Arithmetic operators
a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)


#relational operators
a = 10
b = 20
print(a > b)
print(a < b)
print(a == b)
print(a != b)

#Logical operators
a = 10
b = 20
print(a > 5 and b > 10)
print(a > 15 or b > 10)
print(not(a > 5))

#Assignment operators
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
a = 5
b = 3
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)

#membership operators
name = "Python"
print("P" in name)
print("z" not in name)

#identity operators
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