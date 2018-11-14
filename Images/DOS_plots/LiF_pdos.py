# coding: utf-8
hole_data = pd.read_csv("LiF_hole_sc.dos1ev", delim_whitespace=True, skiprows=3, names = ['E','tot', 'P'])
data = pd.read_csv('LiF.dos1ev', delim_whitespace=True, skiprows=3, names = ['E','tot', 'Li', 'P', 'F'])
#data.describe()
#plt.plot(data['E'],data['tot'], linewidth = 2.5)
#plt.plot(data['E'],data['F'], linewidth = 2.5)
plt.plot(hole_data['E'],hole_data['P'], linewidth = 2.5)
plt.plot(data['E'],data['P'], linewidth = 2.5)
plt.axvline(x=0, color= 'k', linewidth = 2.5) #Fermi energy
plt.title("P-DOS of Li2O")
plt.xlim([-5,20])
plt.xlabel("Energy (eV)")
plt.ylabel("DOS (States/eV cell)")

plt.show()
