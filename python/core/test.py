'''d={"apple":100,"banana":40,"cherry":150}
filtered_keys=filter(lambda key:d[key]>50,d)
result=list(filtered_keys)
print(result)'''


l=['P','Y','T','H','O','N']
def fun(a,b):
    return a+b
l1=reduce((fun,l))
print(l1)





