#iterative factorial

def factorial(n):
    product=1
    for i in range(1,n+1):
        product=product*i
    return product

n=int(input("Enter a positive number"))
if n<0:
    print("factorial not defined")
else:
    f=factorial(n)
    print('factorial of ',n ,'is ',f)