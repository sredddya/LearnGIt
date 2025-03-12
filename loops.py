''''
user_input1=int(input("enter the num1: "))
user_input2=int(input("enter the num2: "))
user_choice=input("1.Addition\n2.subtraction\n3.multiplication\n4.Division\n:")

if user_choice=="1":
    add_num=user_input1+user_input2
    print(add_num)
elif user_choice=="2":
    sub_num=user_input1-user_input2
    print(sub_num)
elif user_choice:
    mul_num=user_input1*user_input2
    print(mul_num)
elif user_choice:
    div_num=user_input1/user_input2
    print(div_num)
else:
    print("out of scope condition is given")
'''

'''
user_input=(int(input("enter the num")))

if user_input>0:
    print("positive Number")
elif user_input==0:
    print("enter number is 0")
else:
    print("Negative Number")'
'''
'''
import random
user_input=input("do want to play the game:")
if user_input=="yes":
    print("user selected yes")
    dice_input=input("Enter the number of faces you want to select:\n6 face\n8 face\n:")
    if dice_input=="6":
        print("Generate a random number between 1-6")
        number_6faces=random.randrange(1,6)
        print(number_6faces)
    elif dice_input=="8":
        print("Generate a random number between 1-8")
        number_8faces=random.randrange(1,8)
        print(number_8faces)
else:
    print("Thank You! come again when you wish to play")
    
'''


user_input=input("Are you a citizen of india Yes/No:\n:")
if user_input=="yes":
    print("user selected yes")
    age=int(input("enter your age: "))
    if age>=18:
        print("eligible to vote")
    elif age<18:
        print("age limit is not up to the mark")
else:
    print("Not eligible to vote")