import csv

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import datetime

data = []

with open("Per_Capita_Income_at_Current_Prices.csv") as f:
    r = csv.reader(f)
    for i in r:
        data.append(i)

print data[1]

yval = [[] for i in range(2004, 2013)]

for i in data[1:]:
    for j in range(2004, 2013):
        try:
            yval[j-2004].append(int(i[j-2004+2]))
        except Exception as e:
            break


xval = [str(i) for i in range(2004, 2013)]

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 4))
axes.boxplot(yval, zorder=3)
axes.set_title('Per Capita Income - Madhya Pradesh - Districtwise - 2004 - 2012', fontsize=10)
plt.xlabel('Year')
plt.ylabel('Per Capita Income (Rupees)')
axes.set_xticklabels(xval)
plt.grid(which='both', zorder=0)
plt.minorticks_on()
plt.show()