'''
The script extracts the orbital magnetic moments from the OUTCAR file
and prints them to a file named OrbitalData.
The orbital magnetic moments share the same order as the POSCAR or CONTCAR ions.
To use this script:
    python readOrbital.py
The OUTCAR file must be present in the same dictionary.
The respective columns in the OrbitalData file give 
the orbital magnetic moments in the x, y, and z dimensions.
The final column is the total orbital magnetic moment calculated 
by pythagorean theorem.
Author: Megan Hoover, adapted from James T. Pegg
'''

import os
from math import sqrt

xData = []
yData = []
zData = []

with open('OUTCAR', 'r+') as f:
    for n, line in enumerate(f):
        if ' orbital moment (x)' in line:
            xmTitle = n
            xmStart = n + 4
        if ' orbital moment (y)' in line:
            ymTitle = n
            ymStart = n + 4
        if ' orbital moment (z)' in line:
            zmTitle = n
            zmStart = n + 4
        if 'Spin-Orbit-Coupling matrix elements' in line:
            SOCline = n

with open('OUTCAR', 'r+') as f:
    for n, line in enumerate(f):
        if ('---' in line) and (n >= xmStart) and (n < ymTitle):
            xmEnd = n - 1
        if ('---' in line) and (n >= ymStart) and (n < zmTitle):
            ymEnd = n - 1
        if ('---' in line) and (n >= zmStart) and (n < SOCline):
            zmEnd = n - 1

with open('OUTCAR', 'r+') as f:
    for n, line in enumerate(f):
        if (n >= xmStart) and (n <= xmEnd):
            xData.append(line.split()[4])
        if (n >= ymStart) and (n <= ymEnd):
            yData.append(line.split()[4])
        if (n >= zmStart) and (n <= zmEnd):
            zData.append(line.split()[4])

with open('OrbitalData#', 'a+') as f:
    f.write('{}\n'.format('Orbital Data'))
    f.write('{}\n'.format('%s %15s %15s %15s'% ('x-axis', 'y-axis', 'z-axis', 'Total')))
    f.write('{}\n'.format('%s %15s %15s %15s'% ('----------', '----------', '----------', '----------')))
    for i in range(0, len(xData)):
        total = round(sqrt(float(xData[i])**2 + float(yData[i])**2 + float(zData[i])**2), 3)
        f.write('{}\n'.format('%s %15s %15s %15s'% (xData[i], yData[i], zData[i], total)))
