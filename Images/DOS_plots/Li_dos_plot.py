# coding: utf-8
hole_data = pd.read_csv("Li_sc_hole.dos1ev", delim_whitespace=True, skiprows=3, names = ['E','tot','Li','S', 'P'])
data = pd.read_csv('Li.dos1ev', delim_whitespace=True, skiprows=3, names = ['E','tot','Li','S', 'P'])
data.describe()
#plt.plot(data['E'],data['tot'])
#plt.plot(data['E'],data['S'])
plt.plot(hole_data['E'],hole_data['P'])
plt.plot(data['E'],3*data['P'])
plt.axvline(x=0) #Fermi energy
plt.title("P-DOS of Li")
plt.xlim([-5,15])
plt.xlabel("Energy (eV)")
plt.ylabel("DOS (States/eV cell")

plt.show()
