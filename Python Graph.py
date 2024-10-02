# This Python program is for ploting a graph form data and finding the fitting patameters
# One can input the data manually or by selecting a data file from  google drive

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
import array as arr
from scipy import stats


# Choice of Data Input Manual or Data file

choice = input("Enter your data entry type (Manual / Data File) : ")

if choice == 'Manual':

  # x axis values
  x = []
  n = int(input("Enter total number of data points : "))
  print("Enter X values:")
  for i in range(0, n):
      ele = float(input())
      # adding the element
      x.append(ele)

  # corresponding y axis values
  y = []
  print("Enter Y values:")
  for i in range(0, n):
      ele = float(input())
      # adding the element
      y.append(ele)

  # Show the user input
  print("Your inputs are")
  print("x=",x, "&","Y=",y)

else: # Read form data fie
  #print("Chose Your Data File")

  #file_path = 'drive/MyDrive/Colab Notebooks/data2.txt' # Specify the data file path
  file_path = input("Chose Your Data File in Drive")
  # Read the data from the file
  x = []
  y = []
  yerr =[]


  with open(file_path, 'r') as file:
        for line in file:
            xf, yf,yerrf = map(float, line.strip().split())  # Assuming two columns: x and y and Y error
            x.append(xf)
            y.append(yf)
            yerr.append(yerrf)
  # Show the user input
  print("Your inputs are")
  print("x=",x, "&","Y=",y)




# Error Value
#yerr = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]


# Axis Labeling
xaxis_label= input("Enter x-axis label:") 
#plt.xlabel('Temperature Difference ($^o$C)',fontsize=14, color='black')
plt.xlabel(xaxis_label,fontsize=14, color='black')

yaxis_label= input("Enter y-axis label:")
#plt.ylabel('Thermo EMF (mV)',fontsize=14, color='black')
plt.ylabel(yaxis_label,fontsize=14, color='black')

# Axis Range seting ([Xmin, Xmax, Ymin, Ymax])

x_min = float(input("Enter x-minima value:"))
x_max = float(input("Enter x-maxima value:"))

y_min = float(input("Enter y-minima value:"))
y_max = float(input("Enter y-maxima value:"))

#plt.axis([25, 90, 0, 1.3])
plt.axis([x_min, x_max, y_min, y_max])


# Axis ticks control
#plt.xticks(rotation=00, fontsize=12, fontweight='medium')
plt.yticks(rotation=00, fontsize=12, fontweight='medium')
# plt.xticks(np.arange(min(x), max(x)+1, 1.0))
#plt.xticks(np.arange(30, 90+1, 10.0), rotation=00, fontsize=12, fontweight='medium')
plt.xticks(np.arange(x_min, x_max+1, 1.0), rotation=00, fontsize=12, fontweight='medium')

# Plot Title
plot_title= input("Enter the title of the plot (Figure caption):")
plt.title(plot_title, fontsize=14, color='black')



# Grid Seting
plt.grid(False)

# plotting the points
#plt.scatter(x, y, s=100, color='red', label="Data", alpha=0.7, marker='o')
#plt.plot(x, y , linewidth=2.0, color='black', linestyle = '-')
#plt.errorbar(x, y, yerr, linewidth=2, capsize=6 )

# function to show the plot

#plt.show()

#  User defined function plot (Linear regression)
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

#plt.scatter(x, y)
plt.scatter(x, y, s=100, color='red', label="Data", alpha=0.7, marker='o')
#plt.errorbar(x, y, yerr, linewidth=2, capsize=6 )
plt.plot(x, mymodel, color='green',linewidth=3)
plt.show()

print("Fitting Parameters")
print("The slope of the curve is =", slope)
print("The intercept of the curve is =", intercept)
print("the coefficient of correlation is =", r)


#slope_value= str(slope)
# Text Adding
#plt.text(40, 1.2, r'Slope =  $\mu V /\,\, ^oC$' )
#plt.text(1,15, r'slope_value')
