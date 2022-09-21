print("Select any option")
print("1.Celcius")
print("2.Fahrenhiet")
choice=int(input())
temp=int(input("Enter tempature: "))
if choice==1:
    print(((temp*9/5)+32))
else:
    print(((temp-32)*5/9))