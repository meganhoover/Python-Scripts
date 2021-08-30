import csv
import pandas as pd
import matplotlib.pyplot as plt

with open('TDOS.dat') as infile, open('TDOS.csv', 'w') as outfile:
    csv_writer = csv.writer(outfile)
    for line in infile:
        csv_writer.writerow(line.split())

with open('PDOS_U_UP.dat') as infile, open('PDOS_U.csv', 'w') as outfile:
    csv_writer = csv.writer(outfile)
    for line in infile:
        csv_writer.writerow(line.split())

with open('PDOS_O_UP.dat') as infile, open('PDOS_O.csv', 'w') as outfile:
    csv_writer = csv.writer(outfile)
    for line in infile:
        csv_writer.writerow(line.split())

with open('PDOS_Si_UP.dat') as infile, open('PDOS_Si.csv', 'w') as outfile:
    csv_writer = csv.writer(outfile)
    for line in infile:
        csv_writer.writerow(line.split())

"""Plot the TDOS of Pristine bulk USiO4 structure
    calculated using collinear spin and the PBE functional"""

# Read csv file and convert to DataFrame
TDOS = pd.read_csv("TDOS.csv")
df1 = pd.DataFrame(TDOS)

PDOS_U = pd.read_csv("PDOS_U.csv")
df2 = pd.DataFrame(PDOS_U)

PDOS_O = pd.read_csv("PDOS_O.csv")
df3 = pd.DataFrame(PDOS_O)

PDOS_Si = pd.read_csv("PDOS_Si.csv")
df4 = pd.DataFrame(PDOS_Si)

# remove special character
df1.columns = df1.columns.str.replace('[#,@,&]', '')
df2.columns = df2.columns.str.replace('[#,@,&]', '')
df3.columns = df3.columns.str.replace('[#,@,&]', '')
df4.columns = df4.columns.str.replace('[#,@,&]', '')

# create a dictionary
# key = old name
# value = new name
dict = {'tdos-UP': 'UP',
        'tdos-DOWN': 'DOWN'}

# call rename () method
df1.rename(columns=dict,
          inplace=True)

# Sum each row for the specific U orbitals
df2['f_orbitals'] = df2['fy3x2'] + df2['fxyz'] + df2['fyz2'] + df2['fz3'] + df2['fxz2'] + df2['fzx2'] + df2['fx3']
df2['d_orbitals'] = df2['dx2'] + df2['dxz'] + df2['dz2'] + df2['dyz'] + df2['dxy']
#df2['p_orbitals'] = df2['px'] + df2['py'] + df2['pz']

# Sum each row for the specific O orbitals
df3['p_orbitals'] = df3['px'] + df3['py'] + df3['pz']

# Sum each row for the specific Si orbitals
df4['p_orbitals'] = df4['px'] + df4['py'] + df4['pz']

x = df1.Energy
y = df1.UP
z = df2.f_orbitals
z1 = df2.d_orbitals
#z2 = df2.p_orbitals
w = df3.p_orbitals
v = df4.p_orbitals

# plot
fig, ax = plt.subplots()
plt.vlines(0, 0, 40, color='k', linestyle=':')
#plt.plot(x, y, color='k', linewidth=1.0, label='TDOS')
plt.plot(x, z, color='b', linewidth=1.0, label='U 5f')
plt.plot(x, z1, color='g', linewidth=1.0, label='U 6d')
#plt.plot(x, z2, color='b', linewidth=1.0, label='U (p)')
plt.plot(x, w, color='r', linewidth=1.0, label='O 2p')
plt.plot(x, v, color='m', linewidth=1.0, label='Si 3p')
plt.xlabel('Energy (eV)')
plt.ylabel('Density of States (states/eV)')
plt.xlim([-8, 7])
plt.ylim([0, 40])
plt.grid(False)
plt.legend()
ax.text(0.2, 38, 'Indirect Band Gap = 3.207 eV', fontsize=8)
plt.savefig("DOS_USiO4.pdf",dpi=1000, bbox_inches="tight")
