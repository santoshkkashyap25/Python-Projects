#lottery simulation

import matplotlib.pyplot as plt
import random

account=0
x=[]
y=[] 
for i in range(30):
    x.append(i+1)
    bet=random.randint(1,10)
    Lucky_draw=random.randint(1,10)
    print("Day ",(i+1))
    print("Your bet ",bet)
    print("Your lucky draw ",Lucky_draw)
    if bet==Lucky_draw:
        account=account+900-100
        print("Account",account)
    else:
        account=account-100
        print("Account",account)
    y.append(account)
print("Total Account",account)
plt.plot(x,y)
plt.show()

    

