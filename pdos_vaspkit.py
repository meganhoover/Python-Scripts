import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

with open('PDOS_SUM_U_f.dat') as infile, open('PDOS_SUM_U_f.csv', 'w') as outfile:
    csv_writer = csv.writer(outfile)
    for line in infile:
        csv_writer.writerow(line.split())

with open('PDOS_SUM_U_d.dat') as infile, open('PDOS_SUM_U_d.csv', 'w') as outfile:
    csv_writer = csv.writer(outfile)
    for line in infile:
        csv_writer.writerow(line.split())

with open('PDOS_SUM_U_p.dat') as infile, open('PDOS_SUM_U_p.csv', 'w') as outfile:
    csv_writer = csv.writer(outfile)
    for line in infile:
        csv_writer.writerow(line.split())

with open('PDOS_SUM_O_p.dat') as infile, open('PDOS_SUM_O_p.csv', 'w') as outfile:
    csv_writer = csv.writer(outfile)
    for line in infile:
        csv_writer.writerow(line.split())

with open('PDOS_SUM_Si_p.dat') as infile, open('PDOS_SUM_Si_p.csv', 'w') as outfile:
    csv_writer = csv.writer(outfile)
    for line in infile:
        csv_writer.writerow(line.split())

"""Plot the TDOS of Pristine bulk USiO4 structure
    calculated using collinear spin and the PBE functional"""

# Read csv file and convert to DataFrame
PDOS_U_f = pd.read_csv("PDOS_SUM_U_f.csv")
df1 = pd.DataFrame(PDOS_U_f)

PDOS_U_d = pd.read_csv("PDOS_SUM_U_d.csv")
df2 = pd.DataFrame(PDOS_U_d)

PDOS_O_p = pd.read_csv("PDOS_SUM_O_p.csv")
df3 = pd.DataFrame(PDOS_O_p)

PDOS_Si_p = pd.read_csv("PDOS_SUM_Si_p.csv")
df4 = pd.DataFrame(PDOS_Si_p)

PDOS_U_p = pd.read_csv("PDOS_SUM_U_p.csv")
df5 = pd.DataFrame(PDOS_U_p)

# remove special character
df1.columns = df1.columns.str.replace('[#,@,&]', '')
df2.columns = df2.columns.str.replace('[#,@,&]', '')
df3.columns = df3.columns.str.replace('[#,@,&]', '')
df4.columns = df4.columns.str.replace('[#,@,&]', '')
df5.columns = df5.columns.str.replace('[#,@,&]', '')

# create a dictionary
# key = old name
# value = new name
dict = {'PDOS-UP': 'UP',
        'PDOS-DOWN': 'DOWN'}

# call rename () method
df1.rename(columns=dict,
          inplace=True)

df2.rename(columns=dict,
          inplace=True)

df3.rename(columns=dict,
          inplace=True)

df4.rename(columns=dict,
          inplace=True)

df5.rename(columns=dict,
          inplace=True)

# What will be plotted
x = df1.Energy
y = df1.UP
z = df2.UP
w = df3.UP
v = df4.UP
a = df5.UP

# plot
fig, ax = plt.subplots()
plt.vlines(0, 0, 30, color='k', linestyle=':')
plt.plot(x, y, color='b', linewidth=1.0, label='U 5f')
plt.plot(x, z, color='lime', linewidth=1.0, label='U 6d')
plt.plot(x, a, color='c', linewidth=1.0, label='U 6p')
plt.plot(x, w, color='r', linewidth=1.0, label='O 2p')
plt.plot(x, v, color='m', linewidth=1.0, label='Si 3p')
plt.xlabel('Energy (eV)')
plt.ylabel('Density of States (states/eV)')
plt.xlim([-8, 8])
plt.ylim([-2, 30])
ax.yaxis.set_minor_locator(AutoMinorLocator())
plt.grid(False)
plt.legend(loc='upper left')
ax.text(-7.8, 19, 'Indirect Band Gap = 3.207 eV', fontsize=8)
plt.savefig("PDOS_USiO4.pdf",dpi=1000, bbox_inches="tight")
