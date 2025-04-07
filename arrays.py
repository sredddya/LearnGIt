
import array
numbers=array.array('i',[43,23,56,76,67])
print(numbers)
print(type(numbers))


for num in numbers:
    print(num)

for indexing, num in enumerate(numbers):
    print(f"Index {indexing}:{num}")

'''
def add (a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    print(c)
    print(d)
    print(e)
    print(f)
add (8,3)'''