import csv

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import datetime

data = []

with open("fpt3302_Chennai-2001.csv") as f:
    r = csv.reader(f)
    for i in r:
        data.append(i)

yval1 = [0, 0, 0]
yval2 = [0, 0, 0]

for i in data[6:]:
    yval1[0] += int(i[10]) - int(i[13]) - int(i[16])
    yval1[1] += int(i[13])
    yval1[2] += int(i[16])
    yval2[0] += int(i[11]) - int(i[14]) - int(i[17])
    yval2[1] += int(i[14])
    yval2[2] += int(i[17])

xval = [1, 3, 5]
xval3 = [1.5, 3.5, 5.5]
xticks = ['Others', 'Scheduled Caste', 'Scheduled Tribe']
xval2 = [2, 4, 6]

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 4))
axes.bar(xval2, yval2, zorder=3)
axes.bar(xval, yval1, zorder=3)
plt.yscale("log")
axes.set_ylim(ymin=100)
axes.set_title('Chennai - Population Distribution - 2001', fontsize=10)
axes.legend(['Male', 'Female'])
plt.xlabel('Population Type')
plt.ylabel('Count (log scale)')
plt.xticks(xval3, xticks)
plt.grid(which='both', zorder=0)
plt.minorticks_on()
plt.show()
