

def fun2():
    i=0;
    sum=0;
    while i<10:
        sum+=i
        print("Current number ",i,"Previous number ",end=" ")
        if i!=0:
            print(i-1,end=" ")
        else:
            print(i,end=" ")
        print(" Sum : ",sum)
        i+=1


fun2()