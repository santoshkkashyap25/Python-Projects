
#leap year or not

import random
year=random.randint(1993,2020)
print(year)
if(year%4==0 and year%100!=0 or year%400==0):
    print('Leap Year')
else:
    print('not a Leap Year')
    
