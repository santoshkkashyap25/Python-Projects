#collatz conjecture
'''
 Input= n
 if n is even then n=n/2
 else n=3n+1
'''

def checknum(num):
    count=1
    while(num!=1):
        if(num%2==0):
            num=int(num/2)
            count+=1
        else:
            num=(num*3)+1
            count+=1
    print(num,count)

checknum(256)















