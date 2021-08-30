import pandas as pd

# List all files in directory
directory_path = 'directory path'
directory = os.listdir(directory_path)

for filenames in directory:
    if filenames.endswith(".csv") and filenames.startswith("spd"):
        spd_orbitals_csv = os.path.join(directory_path,filenames)
        df_spd = pd.DataFrame(pd.read_csv(spd_orbitals_csv))

# add empty E0 to f_orbital*.csv files
# Copy values from spd_csv E0 column to f_csv E0 colomn
for filenames in directory:
    if filenames.endswith(".csv") and filenames.startswith("f"):
        f_orbitals_csv = os.path.join(directory_path,filenames)
        df_f = pd.DataFrame(pd.read_csv(f_orbitals_csv))
        df_f["E0"] = ""
        df_f['E0'] = df_spd['E0'].values
        # Rearrange columns, move E0 from the end to the beginning
        cols = df_f.columns.tolist()
        cols = cols[-1:] + cols[:-1]
        df_f = df_f[cols]
        df_f.to_csv(f_orbitals_csv, index=False)

# Add a sum totals columns for the s, p, d, and f orbitals for each U atom
for filenames in directory:
    if filenames.endswith("f.csv") and filenames.startswith("U"):
        f_orbitals_csv = os.path.join(directory_path,filenames)
        df = pd.DataFrame(pd.read_csv(f_orbitals_csv))
        df['f-total'] = df['fy3x2-total'] + df['fxyz-total'] + df['fyz2-total'] + df['fz3-total'] + df['fxz2-total'] + df['fzx2-total'] + df['fx3-total']
        df.to_csv(f_orbitals_csv, index=False)
    elif filenames.endswith("spd.csv") and filenames.startswith("U"):
        spd_orbitals_csv = os.path.join(directory_path,filenames)
        df2 = pd.DataFrame(pd.read_csv(spd_orbitals_csv))
        df2['s_orbital'] = df2['s-total']
        df2['p_orbitals'] = df2['py-total'] + df2['pz-total'] + df2['px-total']
        df2['d_orbitals'] = df2['dxy-total'] + df2['dyz-total'] + df2['dz2-total'] + df2['dxz-total'] + df2['dx2-y2-total']
        df2.to_csv(spd_orbitals_csv, index=False)

# Add a sum totals columns for the s, p, d, and f orbitals for each O atom
for filenames in directory:
    if filenames.endswith("spd.csv") and filenames.startswith("O"):
        spd_orbitals_csv = os.path.join(directory_path,filenames)
        df = pd.DataFrame(pd.read_csv(spd_orbitals_csv))
        df['s_orbital'] = df['s-total']
        df['p_orbitals'] = df['py-total'] + df['pz-total'] + df['px-total']
        df['d_orbitals'] = df['dxy-total'] + df['dyz-total'] + df['dz2-total'] + df['dxz-total'] + df['dx2-y2-total']
        df.to_csv(spd_orbitals_csv, index=False)
