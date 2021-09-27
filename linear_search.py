#linear search

def linear(n,x):
    element=[]
    for i in range(1,n):
        element.append(i)
    count=0
    flag=0
    for i in element:
        count+=1
        if(i==x):
            print("the number found at "+str(i))
            flag=1
            break
    if(flag==0):
        print("the number not found")
        print("the number of iteration is "+str(count))


linear(10,4)






