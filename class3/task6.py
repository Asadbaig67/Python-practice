list=[]
even=0
odd=0

ex=int(input("Enter -1 to stop entering data: "))

while ex!=-1:
    ex=int(input("Enter -1 to stop entering data: "))
    list.append(ex)

for item in list:
    if(item%2==0):
        even+=1
    else:
        odd+=1

print("The number of even values is ",even," and number of odd values is ",odd)        