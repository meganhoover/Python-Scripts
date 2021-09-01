#!/bin/sh
# This code has been written to calculate the density of states
# for noncollinear calculations in VASP. The current form is written
# for a 2 element crystal, i.e., UO2. If there are more elements in
# the crystal, the dos_variabbles.py and ?.py scripts need to be 
# edited.
#
# IF YOU ARE RUNNING COLLINEAR CALCULATIONS, THIS SCRIPT DOES 
# NOT WORK FOR YOU.
#
# The output files are: 
# 	TDOS 
# 	PDOS_{element}{orbital} (i.e., PDOS_Uf)
# 	PDOS_{element}{atom position} (i.e., PDOS_U1)
# 
# To use this script: 
# 	./pdos_noncollinear.sh
# 
# The DOSCAR and POSCAR files must be in the same dictionary. 
#
# The columns in the DOSCAR file are as follows: 
# 	Line A: E0
# 		s-total s-mx s-my s-mz
# 		py-total py-mx py-my py-mz
# 		pz-total pz-mx pz-my pz-mz
# 		px-total px-mx px-my px-mz
# 		dxy-total dxy-mx dxy-my dxy-mz
# 		dyz-total dyz-mx dyz-my dyz-mz
# 		dz2-total dz2-mx dz2-my dz2-mz
# 		dxz-total dxz-mx dxz-my dxz-mz
# 		dx2-y2-total dx2-y2-mx dx2-y2-my dx2-y2-mz 
# 	Line B: fy3x2-total fy3x2-mx fy3x2-my fy3x2-mz 
# 		fxyz-total fxyz-mx fxyz-my fxyz-mz 
# 		fyz2-total fyz2-mx fyz2-my fyz2-mz 
# 		fz3-total fz3-mx fz3-my fz3-mz 
# 		fxz2-total fxz2-mx fxz2-my fxz2-mz 
# 		fzx2-total fzx2-mx fzx2-my fzx2-mz 
# 		fx3-total fx3-mx fx3-my fx3-mz
#
# Author: Megan Hoover 
# Date: 8/27/2021 
# Institution: Clemson University

# Remove any old modules that maybe in path and load anaconda
module purge
module load anaconda3/2020.07-gcc

# Write the DOSCAR_datafile
python dos_datafile.py

# Separate the data from the DOSCAR file into *.txt files for each
# atom position, i.e., 'atom_#.txt', where # is associated with
# each atom in that position as written in the POSCAR file. If the 
# order in the POSCAR file is U (1-4) and O (5-12), then 
# 'atom_1.txt' corresponds to the U1 atom.
python dos_sepatoms2txt.py

# Remove the first row in each 'atom_#.txt' file
sed -i '1d' *.txt

# Split the data into 'f_orbital_atom_#.txt' and 'spd_orbital_atom_#.txt' files
python dos_sepspdf2txt.py

# Convert *.txt to *.csv
python dos_convert2csv.py

# Copy E0 from spd*.csv file to the beginning of the f*.csv files
# The spd*.csv files have 37 columns and the f*.csv files have 29 columns 
python dos_insrtE0.py

# Extract variables of interest from the POSCAR and DOSCAR files
# Write them to a file called 'DOSCAR_variables'
python dos_variabbles.py

# Delete the f*.csv files not associated with the U-atoms and rename the files
python dos_remove_rename_Uf.py

# Rename spd*.csv files
python dos_rename_spd.py

# Sum columns in each *.csv file to get the total density of states for each orbial
# i.e., s, p, d, and f totals
python dos_sumcolumns.py

# Sum the last column (f-total) in each f_U*.csv file, and write to a new file with
# 2 columns: E0 and f-total
# Sum the last column (d-total) in each spd_U*.csv file, and write to a new file with
# 2 columns: E0 and d-total
# Sum the second to last column (p-total) in each spd_U*.csv file, and write to a new 
# file with 2 columns: E0 and p-total
# Sum the second to last column (p-total) in each spd_O*.csv file, and write to a new
# file with 2 columns: E0 and p-total
# Sum the third to last column (s-total) in each spd_O*.csv file, and write to a new
# file with 2 columns: E0 and s-total
python dos_pdos_per_element.py

