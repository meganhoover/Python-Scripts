import os

# List all files in directory
directory_path = '/home/mel2/Python_Noncollinear_DOS/'
directory = os.listdir(directory_path)

# Move all the odd lines into spd_DOSCAR_datafile_#.txt
# Move all the even lines into f_DOSCAR_datafile_#.txt
for filenames in directory:
    if filenames.endswith(".txt"):
        DOSCAR_data = os.path.join(directory_path,filenames)
        with open(DOSCAR_data) as openfile, open(directory_path + 'f_orbital_' + filenames, 'w') as f_outfile, open(directory_path + 'spd_' + filenames, 'w') as spd_outfile:
            for count, line in enumerate(openfile, start=1):
                # move even lines into f file
                if count % 2 == 0:
                    f_outfile.write(line)
                # move the odd lines into spd file
                elif count % 2 == 1:
                    spd_outfile.write(line)        
