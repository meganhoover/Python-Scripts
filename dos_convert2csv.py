import pandas as pd

# List all files in directory
directory_path = '/home/mel2/Python_Noncollinear_DOS/'
directory = os.listdir(directory_path)

# Convert f_*.txt and spd_*.txt files into *.csv files
for filenames in directory:
    # if file starts with 'f' and ends with '.txt', put it in f_orbitals 
    if filenames.endswith(".txt") and filenames.startswith("f"):
        f_orbitals = os.path.join(directory_path,filenames)
        base1 = os.path.basename(f_orbitals)
        #print(f_orbitals," ",base1)
        file1 = pd.read_csv(f_orbitals, sep=" ", engine='python', header=None)
        # remove the '.txt' from f_orbital file names & concatenate '.csv'
        file1.to_csv(os.path.splitext(base1)[0] + ".csv", index=False)
    # if file starts with 'spd' and ends with '.txt', put it in spd_orbitals
    elif filenames.endswith(".txt") and filenames.startswith("spd"):
        spd_orbitals = os.path.join(directory_path,filenames)
        base2 = os.path.basename(spd_orbitals)
        #print(spd_orbitals," ",base2)
        file2 = pd.read_csv(spd_orbitals, sep=" ", engine='python', header=None)
        # remove the '.txt' from spd_orbital file names & concatenate '.csv' 
        file2.to_csv(os.path.splitext(base2)[0] + ".csv", index=False)

# remove all empty columns
for filenames in directory:
    if filenames.endswith(".csv"):
        csv_files = os.path.join(directory_path,filenames)
        #print(csv_files)
        df = pd.DataFrame(pd.read_csv(csv_files))
        # remove all the empty columns
        df.replace("", inplace=True)
        df.dropna(how='all', axis=1, inplace=True)
        df.to_csv(csv_files, index=False)

spd_names = ['E0','s-total','s-mx','s-my','s-mz','py-total','py-mx','py-my','py-mz','pz-total','pz-mx','pz-my','pz-mz','px-total','px-mx','px-my','px-mz','dxy-total','dxy-mx','dxy-my','dxy-mz','dyz-total','dyz-mx','dyz-my','dyz-mz','dz2-total','dz2-mx','dz2-my','dz2-mz','dxz-total','dxz-mx','dxz-my','dxz-mz','dx2-y2-total','dx2-y2-mx','dx2-y2-my','dx2-y2-mz']
f_names = ['fy3x2-total','fy3x2-mx','fy3x2-my','fy3x2-mz','fxyz-total','fxyz-mx','fxyz-my','fxyz-mz','fyz2-total','fyz2-mx','fyz2-my','fyz2-mz','fz3-total','fz3-mx','fz3-my','fz3-mz','fxz2-total','fxz2-mx','fxz2-my','fxz2-mz','fzx2-total','fzx2-mx','fzx2-my','fzx2-mz','fx3-total','fx3-mx','fx3-my','fx3-mz']

# add headers to csv files via pandas
for filenames in directory:
    # if file starts with 'spd' and ends with '.csv', put it in spd_orbitals_csv
    if filenames.endswith(".csv") and filenames.startswith("spd"):
        spd_orbitals_csv = os.path.join(directory_path,filenames)
        df1 = pd.read_csv(spd_orbitals_csv)
        df1.to_csv(spd_orbitals_csv, header=spd_names, index=False)
    # if file starts with 'f' and ends with '.csv', put it in f_orbitals
    elif filenames.endswith(".csv") and filenames.startswith("f"):
        f_orbitals_csv = os.path.join(directory_path,filenames)
        df2 = pd.read_csv(f_orbitals_csv)
        df2.to_csv(f_orbitals_csv, header=f_names, index=False)


