import re

# Split the file 'DOSCAR_datafile' into separate files for each atom
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Collect all lines, without loading whole file into memory
lines = []
with open('/home/mel2/Python_Noncollinear_DOS/DOSCAR_datafile') as main_file:
    for line in main_file:
        lines.append(line)

# Write each group of lines to separate files
for i, group in enumerate(chunks(lines, n=int(b+1)), start=1):
    with open('/home/mel2/Python_Noncollinear_DOS/DOSCAR_datafile_%d.txt' % i, mode="w") as outfile:
        for line in group:
            # change all whitespace in each line to only space
            outfile.write(re.sub('[\t ]+',' ',line))
