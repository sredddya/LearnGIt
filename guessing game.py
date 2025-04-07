'''
The task is this: the program will ask for the user's name and then it will say
something like: “Well John, I've thought of a number between 1 and 100 and you
have only eight tries to guess it. What number do you think it is?” On each try, the
player will say a number and the program can answer for different things.
 If the number the user said is less than 1 or greater than 100, it will tell them that
he/she has chosen a number that is out of play.
 If the number the user chose is less than the number the program thought of, it will tell
them that the answer is wrong, and that he/she chose a lower number than the secret
number.
 If the user chose a number greater than the secret number, it will let them know that it
was greater.
 And if the user got the secret number right, they will be informed that they have won,
and how many tries that has taken them.
 If the user has not guessed correctly in their first attempt, they will be asked again to
choose another number and so on until they win or until their eight attempts are done. '
'''
import random

guess=0
secret_num=random.randint(1,5)
attempts=0
user=input("Enter the name of the user: ")

print(f"{user} guess a number between 1 and 100 and you have only eight tries to guess i What number do you think it is?t")
while attempts < 8:
    estimation=int(input("Enter the number"))

    if estimation<=secret_num:
        print("The number selected is less than secret number") 
        break
    elif estimation >= secret_num:
        print("The number selected is more than secret number")
    else:
        print("not correct")

        