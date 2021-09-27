#bubble sort 

def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range (0,n-i-1):
            if (a[j]>a[j+1]):
                tmp=a[j]
                a[j]=a[j+1]
                a[j+1]=tmp
                
                
a=[5,2,9,8,2,3,99,8,7,89,7,56,0,0,8,]
print(a)
bubble(a)
print(a)