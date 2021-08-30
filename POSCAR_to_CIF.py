from pymatgen.io.vasp import Poscar
from pymatgen.io.cif import CifWriter

# Read a POSCAR and write to a CIF.
poscar = Poscar.from_file('POSCAR')
w = CifWriter(poscar.structure)
w.write_file('Collinear_1x1x1_PBE.cif')


