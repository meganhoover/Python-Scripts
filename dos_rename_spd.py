import os
import glob

with open("/home/mel2/Python_Noncollinear_DOS/POSCAR", 'r') as reader:
    POSCAR_data = reader.readlines()

# Extract line 6 and 7 in POSCAR
elements_str = POSCAR_data[5]
num_per_elements_str = POSCAR_data[6]

# Convert the string into a list
elements_list = elements_str.split()
num_per_elements_list = num_per_elements_str.split()

directory_path = '/home/mel2/Python_Noncollinear_DOS/'
directory = os.listdir(directory_path)

# Let's rename the files to reflect to elements it's associated with
# This renames the spd files
spd_filenames = glob.glob('spd_orbital_atom*.csv')
for file in spd_filenames:
    split_filename = file.split('_') #[f, orbital, atom, #.csv]
    print(split_filename)
    new_filename = 'spd_{}'.format(split_filename[3])
    os.rename(file, new_filename)

for i in range(int(num_per_elements_list[0])+1,int(NATOMS)+1):
    if os.path.exists('/home/mel2/Python_Noncollinear_DOS/spd_%d.csv' % i):
        os.rename('/home/mel2/Python_Noncollinear_DOS/spd_%d.csv' % i, os.path.join(directory_path, 'spd_O%d' % i + '.csv'))

for j in range(0,int(num_per_elements_list[0])+1):
    if os.path.exists('/home/mel2/Python_Noncollinear_DOS/spd_%d.csv' % j):
        os.rename('/home/mel2/Python_Noncollinear_DOS/spd_%d.csv' % j, os.path.join(directory_path, 'spd_U%d' % j + '.csv'))
