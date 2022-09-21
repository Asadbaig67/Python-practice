row=int(input("Enter number of rows: "))
col=int(input("Enter number of columns: "))

l=[]
L=[]

for i in range(0,row):
    for j in range(0,col):
        l.append(i*j)
    L.append(l)
    l=[]
print(L)