from wulffpack import (SingleCrystal,
                       Decahedron,
                       Icosahedron)
from ase.build import bulk
from ase.io import read
from ase.io import write

# Read the CIF file of the theoretical coffinite crystal structure
# Theoretical crystal structure taken from AMCSD
primitive_structure = read('USiO4_exp_forwulffpack.cif')

# Normalized surface energies, ref Coffinite_2019 excel document
# To normalize the SE divide each SE value by the lowest SE value
# silicate-terminated surface energies
surface_energies1 = {(0, 1, 1): 3.097,
                    (1, 0, 0): 1.,
                    (1, 1, 0): 1.591,
                    (2, 1, 1): 2.319}
# metal-terminated surface energies
surface_energies2 = {(0, 1, 1): 1.766,
                    (1, 0, 0): 1.,
                    (1, 1, 0): 1.591,
                    (2, 1, 1): 2.319}

particle1 = SingleCrystal(surface_energies1, primitive_structure)
particle2 = SingleCrystal(surface_energies2, primitive_structure)

# Check the ECS have the same volume
print('Volume (sanity check):')
for name, particle in zip(['silicate-terminated', 'metal-termianted'], [particle1, particle2]):
    volume = particle.volume
    print('{}: {:.2f}'.format(name, volume))
print()

# Print the surface area
print('Total surface area (excluding twin boundaries):')
for name, particle in zip(['silicate-terminated', 'metal-terminated'], [particle1, particle2]):
    area = particle.area
    print('{}: {:.2f}'.format(name, area))
print()

# Compare the large fraction area of the {100}
print('Fraction of {100} facets:')
for name, particle in zip(['silicate-terminated', 'metal-terminated'], [particle1, particle2]):
    fraction = particle.facet_fractions.get((1, 0, 0), 0.)
    print('{}: {:.4f}'.format(name, fraction))
print()

# Define colors (optional)
colors = {(0, 1, 1): '#C70039',
          (1, 0, 0): '#FFC30F',
          (1, 1, 0): '#A9A9A9',
          (2, 1, 1): '#FF5733'}

# Show with GUI:
particle1.view()
particle2.view()

# Save as file:
particle1.view(colors=colors, linewidth=0.3, alpha=0.9, save_as='coffinite_T1_wulff.png')
write('coffinite_T1_wulff.xyz', particle1.atoms)
particle2.view(colors=colors, linewidth=0.3, alpha=0.9, save_as='coffinite_T2_wulff.png')
write('coffinite_T2_wulff.xyz', particle2.atoms)


