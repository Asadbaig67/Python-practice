import random

num=random.randint(1,10)
val=int(input("Enter a number between 1 to 9 "))
while num!=val:
    val=int(input("Enter a number between 1 to 9 "))
print("Well guessed")