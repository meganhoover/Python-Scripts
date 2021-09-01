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
print(elements_list, num_per_elements_list)

directory_path = '/home/mel2/Python_Noncollinear_DOS/'
directory = os.listdir(directory_path)

# Because only the U atoms have f orbitals, and the first set of atoms are U
# I deleted all the other f_*csv files associated with the O atoms.
for elem in elements_list:
    if elem.startswith('U'):
        print(elem, num_per_elements_list[0])
        for i in range(int(num_per_elements_list[0])+1,int(NATOMS)+1):
            if os.path.exists('/home/mel2/Python_Noncollinear_DOS/f_orbital_atom_%d.csv' % i):
                os.remove('/home/mel2/Python_Noncollinear_DOS/f_orbital_atom_%d.csv' % i)
            else:
                print("Can not delete the file as it doesn't exists")
    else:
        print('Does not start with U')

        
# Let's rename the files to reflect to elements it's associated with
# This renames the Uf files
Uf_filenames = glob.glob('f_orbital_atom*.csv')
for file in Uf_filenames:
    split_filename = file.split('_') #[f, orbital, atom, #.csv]
    print(split_filename)
    new_filename = 'f_U{}'.format(split_filename[3])
    os.rename(file, new_filename)
