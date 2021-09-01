# Find the total number of lines in the DOSCAR file
num_lines = 0
with open('DOSCAR', 'r') as reader:
    for line in reader:
        num_lines = num_lines + 1

# Record keeping
a = int(NEDOS)+7-1 # -1 bc python starts at 0
b = 2*int(NEDOS)
lines_to_read = [a,num_lines]
print("Start reading the data at python line number index",a)
print("Each atom encompasses",b,"lines.")
print("The total number of lines in the original DOSCAR file are", num_lines)

# Ignore some lines and write everything else to a datafile
with open("/home/mel2/Python_Noncollinear_DOS/DOSCAR",'r') as infile:
    lines = infile.readlines()
    with open("/home/mel2/Python_Noncollinear_DOS/DOSCAR_datafile", 'w') as outfile:
        outfile.writelines(lines[1006:])

# Find the total number of lines in the file 'DOSCAR_datafile'
datafile_num_lines = 0
with open('DOSCAR_datafile', 'r') as reader:
    for line in reader:
        datafile_num_lines = datafile_num_lines + 1

print("The total number of lines in the file 'DOSCAR_datafile' are", datafile_num_lines)
