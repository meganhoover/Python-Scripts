import pandas as pd
import os

# List all files in directory
directory_path = '/home/mel2/Python_Noncollinear_DOS/'
directory = os.listdir(directory_path)

# Add a sum totals columns for the s, p, d, and f orbitals for each U atom
for filenames in directory:
    if filenames.startswith("f_U") and filenames.endswith(".csv"):
        f_orbitals_csv = os.path.join(directory_path,filenames)
        df = pd.DataFrame(pd.read_csv(f_orbitals_csv))
        df['f-total'] = df['fy3x2-total'] + df['fxyz-total'] + df['fyz2-total'] + df['fz3-total'] + df['fxz2-total'] + df['fzx2-total'] + df['fx3-total']
        df.to_csv(f_orbitals_csv, index=False)
    elif filenames.startswith("spd_U") and filenames.endswith(".csv"):
        spd_orbitals_csv = os.path.join(directory_path,filenames)
        df2 = pd.DataFrame(pd.read_csv(spd_orbitals_csv))
        df2['s_orbital'] = df2['s-total']
        df2['p_orbitals'] = df2['py-total'] + df2['pz-total'] + df2['px-total']
        df2['d_orbitals'] = df2['dxy-total'] + df2['dyz-total'] + df2['dz2-total'] + df2['dxz-total'] + df2['dx2-y2-total']
        df2.to_csv(spd_orbitals_csv, index=False)

# Add a sum totals columns for the s, p, d, and f orbitals for each O atom
for filenames2 in directory:
    if filenames2.startswith("spd_O") and filenames2.endswith(".csv"):
        spd_orbitals_csv2 = os.path.join(directory_path,filenames2)
        df3 = pd.DataFrame(pd.read_csv(spd_orbitals_csv2))
        df3['s_orbital'] = df3['s-total']
        df3['p_orbitals'] = df3['py-total'] + df3['pz-total'] + df3['px-total']
        df3['d_orbitals'] = df3['dxy-total'] + df3['dyz-total'] + df3['dz2-total'] + df3['dxz-total'] + df3['dx2-y2-total']
        df3.to_csv(spd_orbitals_csv2, index=False)
