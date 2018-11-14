# coding: utf-8
#hole_data = pd.read_csv("Li2O_guide_sc.dos1ev", delim_whitespace=True, skiprows=3, names = ['E','tot','Li','S', 'P'])
data = pd.read_csv('Li2O_guide.dos1ev', delim_whitespace=True, skiprows=3, names = ['E','tot', 'O', 'Li', 'P'])
data.describe()
plt.plot(data['E'],data['tot'])
plt.plot(data['E'],data['O'])
#plt.plot(hole_data['E'],hole_data['P'])
plt.plot(data['E'],data['Li'])
plt.axvline(x=0) #Fermi energy
plt.title("P-DOS of Li2O")
plt.xlim([-5,15])
plt.xlabel("Energy (eV)")
plt.ylabel("DOS (States/eV cell")

plt.show()
