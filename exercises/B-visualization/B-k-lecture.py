
# import sys

# locate_python = sys.exec_prefix
# print(locate_python)

# # To launch this library on Jupyter
# # matplotlib inline
# Useful link to plot things inside Sublime Text 3
# https://github.com/sschuhmann/Helium/issues

# To install the library for the first time:
# python -m pip install matplotlib 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 20 ,30, 40, 50, 60 , 70 , 80, 90 , 100]

plt.plot(x,y,'b')
plt.show()

x = np.arange(0,11,1.)
y = 2*x+y

fig = plt.figure(figsize=(10,2)) # larghezza 10 pollici, altezza 2 pollici
