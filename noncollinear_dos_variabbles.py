# What is the atom order?
with open("directory path/POSCAR", 'r') as reader:
    POSCAR_data = reader.readlines()

# Extract line 6 and 7 in POSCAR
elements_str = POSCAR_data[5]
num_per_elements_str = POSCAR_data[6]

# Convert the string into a list
elements_list = elements_str.split()
num_per_elements_list = num_per_elements_str.split()

# Variables of interest
First_Element = elements_list[0]
Num_First_Element = num_per_elements_list[0]
Second_Element = elements_list[1]
Num_Second_Element = num_per_elements_list[1]

# Extract NEDOS, E_max, E_min, and FERMI values from the DOSCAR file
with open("directory path/DOSCAR", 'r') as reader:
    DOSCAR_data = reader.readlines()

# Extract line 1 and 6 in DOSCAR
linesix_str = DOSCAR_data[5]
lineone_str = DOSCAR_data[0]

# Convert the string into a list
linesix_list = linesix_str.split()
lineone_list = lineone_str.split()
print(linesix_list)

# Variables of interest
E_max = linesix_list[0]
E_min = linesix_list[1]
NEDOS = linesix_list[2]
FERMI = linesix_list[3]
NATOMS = lineone_list[0]

# Write variables to text file DOSCAR_variables
details = {'E_max' : E_max, 
           'E_min' : E_min, 
           'NEDOS' : NEDOS, 
           'FERMI' : FERMI, 
           'NATOMS' : NATOMS}

with open("/home/mel2/Python_Noncollinear_DOS/DOSCAR_variables",'w') as file:
    for key, value in details.items():
        file.write('%s: %s\n' % (key, value))

print("E_max = ",E_max)
print("E_min = ",E_min)
print("NEDOS = ",NEDOS)
print("FERMI = ",FERMI)
print("NATOMS = ",NATOMS)
print("There are", Num_First_Element,First_Element,"atoms and", Num_Second_Element,Second_Element,"atoms in this calculation.")
print("The total number of atoms in this calculations is",NATOMS)

# Find the total number of lines in the DOSCAR file
num_lines = 0
with open('DOSCAR', 'r') as reader:
    for line in reader:
        num_lines = num_lines + 1

# Record keeping
a = int(NEDOS)+7-1 # -1 bc python starts at 0
b = 2*int(NEDOS)
lines_to_read = [a,num_lines]
print("Start reading the data at python line number index",a)
print("Each atom encompasses",b,"lines.")
print("The total number of lines in the original DOSCAR file are", num_lines)

# Ignore some lines and write everything else to a datafile
with open("directory path/DOSCAR",'r') as infile:
    lines = infile.readlines()
    with open("directory path/DOSCAR_datafile", 'w') as outfile:
        outfile.writelines(lines[1006:])

# Find the total number of lines in the file 'DOSCAR_datafile'
datafile_num_lines = 0
with open('DOSCAR_datafile', 'r') as reader:
    for line in reader:
        datafile_num_lines = datafile_num_lines + 1

print("The total number of lines in the file 'DOSCAR_datafile' are", datafile_num_lines)
