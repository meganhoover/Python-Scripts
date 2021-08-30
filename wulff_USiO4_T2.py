from wulffpack import (SingleCrystal,
                       Decahedron,
                       Icosahedron)
from ase.build import bulk
from ase.io import read
from ase.io import write

primitive_structure = read('USiO4_exp_forwulffpack.cif')
surface_energies = {(0, 1, 1): 1.766,
                    (1, 0, 0): 1.,
                    (1, 1, 0): 1.591,
                    (2, 1, 1): 2.319}
particle = SingleCrystal(surface_energies, primitive_structure)

# Define colors (optional)
colors = {(0, 1, 1): '#C70039',
          (1, 0, 0): '#FFC30F',
          (1, 1, 0): '#A9A9A9',
          (2, 1, 1): '#FF5733'}

# Show with GUI:
particle.view()

# Save as file:
particle.view(colors=colors, linewidth=0.3, alpha=0.9, save_as='coffinite_T2_wulff.png')
write('coffinite_T2_wulff.xyz', particle.atoms)
