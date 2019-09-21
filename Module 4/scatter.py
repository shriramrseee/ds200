import csv

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import datetime

data = []

with open("PCA_CDB_3331_F_Census.csv") as f:
    r = csv.reader(f)
    for i in r:
        data.append(i)

xval = []
yval = []

for i in data[1:]:
    xval.append(int(i[11]))
    yval.append(int(i[12]))

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 4))
axes.scatter(xval, yval, zorder=3)
axes.set_title('Coimbatore District - Household per Town vs Population', fontsize=10)
plt.xlabel('No. of Households')
plt.ylabel('Population Count')
plt.grid(which='both', zorder=0)
plt.minorticks_on()
plt.show()