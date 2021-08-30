import pymatgen as mg
from pymatgen.io.vasp.outputs import BSVasprun, Vasprun
from pymatgen import Spin
from pymatgen.electronic_structure.plotter import BSPlotter, BSDOSPlotter, DosPlotter

import matplotlib as mpl
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter

group_labels=[]
x=[]

with open("KLABELS",'r') as reader:
    lines=reader.readlines()[1:]
for i in lines:
    s=i.encode('utf-8')#.decode('latin-1')
    if len(s.split())==2 and not s.decode('utf-8','ignore').startswith("*"):
        group_labels.append(s.decode('utf-8','ignore').split()[0])
        x.append(float(s.split()[1]))

for index in range(len(group_labels)):
    if group_labels[index]=="GAMMA":
        group_labels[index]=u"Γ"

# Extracting bands
run = BSVasprun("vasprun.xml", parse_projected_eigen=True)
bs = run.get_band_structure("KPOINTS")

print("number of bands", bs.nb_bands)
print("number of kpoints", len(bs.kpoints))

bsplot = BSPlotter(bs)
plt = bsplot.get_plot(zero_to_efermi=True)

# Plotting BS
font = {'color'  : 'black',
        'weight' : 'normal',
        'size'   : 13,
        }

print(bs.efermi)

# add some features
ax = plt.gca()

# title
#ax.set_title("Band structure for the collinear 12-atom uranium dioxide cell with PBE", fontsize=14)

# x-axis
xlim = ax.get_xlim()
ax.hlines(0, xlim[0], xlim[1], linestyles="dashed", color="black")
ax.set_xticks(x)
ax.set_xticklabels(group_labels, rotation=0,fontsize=10)

# supress x-axis title
#ax.set_xlabel(r'$\mathbf{k}$-points',fontdict=font)
ax1 = plt.axes()
x_axis = ax1.xaxis
x_axis.set_label_text('foo')
x_axis.label.set_visible(False)

# y-axis
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.tick_params(axis='y', which='major', direction='inout', labelsize=10, right=True, labelright=False)
ax.tick_params(axis='y', which='minor', direction='inout', right=True)
ax.set_ylabel(r'${E}$-$E_{f}$ (eV)',fontdict=font)
ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

# lines
#for i in x[1:-1]:
#        ax.axvline(x=i, ymin=0, ymax=1,linestyle= '--',linewidth=0.5,color='0.5')

# add legend
#ax.plot((), (), "b-", label="spin up")
#ax.plot((), (), "r--", label="spin down")
ax.get_legend().remove()

# set x,y limits manually
ax.set_xlim((x[0], x[-1]))
plt.ylim((-8, 7))

# save figure
plt.savefig('BS_USiO4.pdf',dpi=1000, bbox_inches="tight")
