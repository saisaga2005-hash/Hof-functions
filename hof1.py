'''Given two lists:
a = [1, 2, 3, 4] b = [10, 20, 30, 40]
Use map() with a lambda to create a new list containing the sum of corresponding
elements.
What happens if the lists are of unequal length'''

'''a=[1,2,3,4]
b=[10,20,30,40]
result=list(map(lambda x,y:x+y,a,b))
print(result)
#if lists are unequal length
a=[1,2,3]
b=[10,20,30,40]
result=list(map(lambda x,y:x+y,a,b))
print(result)'''


#'2 Given a list:
#nums=[12,15,7,18,20,21,25]
#use filter() and lambda to keep numbers that are divisible by 3 or divisible by 5 but not divisible by
#not both
'''nums=[12,15,7,18,20,21,25]
result=list(filter(lambda x:(x%3==0) ^ (x%5==0) ,nums))
print(result)
'''

 #Given a list:
#nums = [1, 2, 3, 4]
#Use reduce() with a lambda to compute the sum, but start with an initial value
#of 10.
#Explain how the initial value affects the reduction process

'''from functools import reduce
nums=[1,2,3,4]
result=reduce(lambda a,b:a+b,nums,10)
print(result)'''

 #Consider the code below:
#nums = [[1, 2], [3, 4], [5, 6]] result = list(map(lambda x: x.append(10), nums))
#print("Result:", result) print("Nums:", nums)
#Questions
#• What will be the output of result?
#• What will be the output of nums?
#• Why does map() behave this way with list.append()?
#• How can you modify the lambda so that nums is not changed

'''Result: [None, None, None]
Nums: [[1, 2, 10], [3, 4, 10], [5, 6, 10]]
nums = [[1, 2], [3, 4], [5, 6]]
result = list(map(lambda x: x + [10], nums))  # create a new list
print("Result:", result)
print("Nums:", nums)'''

 #Use map() with a lambda to add 5 to every element of the following nested
#list [[1, 2], [3, 4], [5, 6]]

'''li=[[1,2],[3,4],[5,6]]
result=list(map(lambda inner:list(map(lambda x:x+5,inner)),li))
print(result)'''

 #Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use
#filter() to keep only the keys whose values are greater than 50.

'''d={"apple":100,"banana":40,"cherry":150}
result=list(filter(lambda k:d[k]>50,d))
print(result)'''


#Use functools.reduce() with a lambda to find the largest number from a given list Dynamically.

'''from functools import reduce
nums=[10,35,7,50,25]
largest=reduce(lambda a,b:a if a>b else b, nums)
print("Largest:", largest)'''


#What happens if the lambda passed to reduce() accepts only one parameter or three parameters? Explain the output or error.
#from functools import reduce

'''nums=[3,6,9]
res=reduce(lambda a: a,nums)
print(res)
 #three parameters
num=[6,9,7]
res=reduce(lambda a,b,c:a if a>b else b,nums)
print(res)'''

#Use map() on a string to convert each character into its ASCII value (using ord()). Print the result list.

'''s="Python"
result=list(map(ord,s))
print(result)'''

#Use filter() to remove all vowels from a string and print the final string.
# with lambda
'''s="Hello World"
res="".join(filter(lambda x:x.lower() not in "aeiou",s))
print(res)'''

#without lambda
'''def remove_vowel(x):
    return x.lower() not in "aeiou"
text=input("Enter a string: ")
result="".join(filter(remove_vowel,text))
print(result)'''

 #Use reduce() to concatenate a list of characters into a single string.
#Example input: ['P', 'y', 't', 'h', 'o', 'n']

'''from functools import reduce
inp=['P', 'y', 't', 'h', 'o', 'n']
res=reduce(lambda x,y:x+y,inp)
print(res)'''


 #Given a list of integers, use map() with id() to print the memory address
#of each element.
#Example: [10, 350, 10, 350, 20] — explain why some addresses repeat.

'''li=[10,350,10,350,20]
res=list(map(lambda x:id(x),li))
print(res)'''

 #Explain the difference between:
#map(str, [1, 2, 3])
#map(lambda x: str(x), [1, 2, 3])
#Which one is faster and why?

'''numbers = [1, 2, 3]
result = list(map(str, numbers))
print(result)   #faster

numbers = ['1', '2', '3']
result = list(map(lambda x: str(x), numbers))
print(result)'''   #slightly slow because lambda function calling str()


#10.  Given a list of numbers:
#[5, 10, 15, 20, 25, 30]
#Perform the following in a single pipeline:
#• Use map() to square each number
#• Use filter() to keep only numbers divisible by 5
#• Use reduce() to calculate the sum of remaining numbers

'''from functools import reduce
li=[5,10,15,20,25,30]
res=reduce(lambda x,y:x+y,filter(lambda x:x%5==0,map(lambda x:x*x,li)))
print(res)'''

from functools import reduce
li=[1,2,3,4,5,6]
res=reduce(lambda x,y:x+y,filter(lambda x:x%2==0,map(lambda x:x**2,li)))
print(res)

from functools import reduce
li=[2,3,4,5,6,7]
result=reduce(lambda x,y:x*y,filter(lambda x:x%4==0,map(lambda x:x**3,li)))
print(result)


from functools import reduce
li="Functional Programming"
result=reduce(lambda x,y:x+1,map(lambda x:x.upper(),filter(lambda x:x.lower() not in "aeiou",li)),0)
print(result)


li=[1,2,3]
res="".join(list(map(lambda x:x[str],li)))
print(res)