for i in range(1,6):
    for j in range(0,i):
        print("*",end="")
    print(end="\n")

for i in range(1,6):
    for j in range(1,6-i):
        print("*",end="")
    print(end="\n")

#method 2

for i in range(1,6):
    print("*"*i)
while(i>0):
    print("*"*i)
    i=i-1