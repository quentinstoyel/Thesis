# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('Li2CO3.dos1ev', delim_whitespace=True, skiprows=3, names = ['E','tot','Li','C','O1','O2'])
data.describe()
data['O1'] = data['O1']+data['O2']
for i in np.arange(4):
    plt.plot(data['E'],data[data.keys()[i+1]])
plt.axvline(x=0) #Fermi energy
plt.title("DOS of Li2CO3")
plt.xlim([-5,15])
plt.xlabel("Energy (eV)")
plt.ylabel("DOS (States/eV cell")

plt.show()
