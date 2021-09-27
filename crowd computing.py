#importing to use mean function
from statistics import mean
#importing to use trimmed value function
from scipy import stats
estimates=[56,87,56,65,34,12,0,98,7,89,54,1,4,6,8,2,90,900,67,567,345,23,213,32,997,89,765]
estimates.sort()
print(estimates)
print(mean(estimates))



#calculating trimmed value
tv=int(0.1*len(estimates))
estimates=estimates[tv:]  #slicing
estimates=estimates[:len(estimates)-tv]
print(estimates)
print(mean(estimates))




#trimmed value using fuction
print("trimmed value using fuction")
values=[56,87,56,65,34,12,0,98,7,89,54,1,4,6,8,2,90,900,67,567,345,23,213,32,997,89,765]
values.sort()
#calculating trimmed value
m=stats.trim_mean(values,0.1)
print(m)

import statistics
import matplotlib.pyplot as plt
plt.plot(estimates)
y=[]
for i in range(len(estimates)):
    y.append(5)
plt.plot(estimates,y,'r--')
plt.plot([statistics.mean(estimates)],[5],'ro')
plt.plot([statistics.median(estimates)],[5],'g^')
