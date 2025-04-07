'''
name=open("/Users/saikiranreddy/training/LearnGIt/hi.txt")
content_file=name.read()
print(content_file)
name.close()
'''


'''name=open("/Users/saikiranreddy/training/LearnGIt/hi.txt","a")
name_file=name.write("\n python is a famous language")
print(name_file)
name.close


def addition(x,y):
    return x+y
print(addition(5,3))

add=lambda x,y:x+y
print(add(5,3))

square=lambda x:x*x
print(square(5))'


#map
number=[1,2,3,4,5]
squared=list(map(lambda x:x**2,number))


print(squared)

#filter
num=[1,2,3,4,5,6,7,8,9,10]

odd_number=list(filter(lambda x:x%2!=0,num))
even_number=list(filter(lambda x:x%2==0,num))
print(odd_number)
print(even_number)'
'''


# Reduce function

from functools import reduce

numbers=[1,2,3,4,5]
sum_numbers=reduce(lambda x,y:x+y,numbers)
print(sum_numbers)


def sum_numbers(lst):
    result=0
    for num in lst:
        result+=num
    return result
print(sum_numbers([1,2,3,4,5]))

#lambda inside functions

def multiply(n):
    return lambda x:x*n

mul=multiply(3)

print(mul(5))



