import pandas as pd

# List all files in directory
directory_path = '/home/mel2/Python_Noncollinear_DOS/'
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

