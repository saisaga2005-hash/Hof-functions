#break statements
for i in range(1, 6):
    if i == 4:
        break
    print(i)
#2
n=29
for i in range(2,n,4):
    print(i*2)
    if i%5==0:
        print(i)
        break
    print("hii")
print("bye")

#continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#pass statement
for i in range(1, 6):
    pass