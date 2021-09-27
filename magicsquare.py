
def magicsquare(n):
    magic_square=[]
    for i in range(n):
        l=[]
        for j in range (n):
            l.append(0)
        magic_square.append(l)


    i=n//2
    j=n-1
    num=n*n
    count=1
    while(count<=num):
        if(i==-1 and j==n):
            j=n-2
            i=0
        else:
            if(j==n):
                j=0
            if(i<0):
                i=n-1
        if(magic_square [i][j]!=0):
            j=j-2
            i=i+1
            continue
        else:
            magic_square[i][j]=count
            count=count+1
        j=j+1
        i=i-1
        
    for i in range(n):
        for j in range(n):
            print(magic_square[i][j],end=" ")
        print()
    print("the sum of row/column/diagonal is :"+str(n*(n**2+1)/2))

        
magicsquare(3)
    
        
        
        
        
        
        
        
        
        
        
        
