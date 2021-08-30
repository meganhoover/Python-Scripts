import numpy as np
import matplotlib as mpl
mpl.use('Agg') #silent mode
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

#hsp=np.loadtxt(open("KLABELS", encoding='utf8'), dtype=np.string_,skiprows=1,usecols = (0,1))
df_u=np.loadtxt("REFORMATTED_BAND_UP.dat",dtype=np.float64)
df_d=np.loadtxt("REFORMATTED_BAND_DW.dat",dtype=np.float64)

for index in range(len(group_labels)):
    if group_labels[index]=="GAMMA":
        group_labels[index]=u"Γ"

#except:
    #print("failed to open KLABELS containing High symmetry point!")

fig,ax = plt.subplots()
ax.plot(df_u[:,0],df_u[:,1:],linewidth=1.0,color='blue')
ax.plot(df_d[:,0],df_d[:,1:],linewidth=1.0,color='blue')
font = {'color'  : 'black',
        'weight' : 'normal',
        'size'   : 13,
        }

# y-axis
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.tick_params(axis='y', which='major', direction='inout', labelsize=10, right=True, labelright=False)
ax.tick_params(axis='y', which='minor', direction='inout', right=True)
ax.set_ylabel(r'${E}$-$E_{f}$ (eV)',fontdict=font)
ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

# x-axis
ax.set_xticks(x)
ax.set_xticklabels(group_labels, rotation=0,fontsize=10)
#ax.set_xlabel(r'$\mathbf{k}$-points',fontsize=13)

# fermi line and vertical lines at high-symmetry points
ax.axhline(y=0, xmin=0, xmax=1,linestyle= '--',linewidth=0.5,color='0.5')
for i in x[1:-1]:
        ax.axvline(x=i, ymin=0, ymax=1,linestyle= '--',linewidth=0.5,color='0.5')

# set x,y limits manually
ax.set_xlim((x[0], x[-1]))
plt.ylim((-7, 2.5))

# plot figure
fig = plt.gcf()
fig.set_size_inches(6,6)
plt.savefig('bandGYXZGL_PeggPath.png',dpi=1000)
