import os

file_path = os.environ['USERPROFILE'] + "\\Downloads\\"
dataset_file = open(file_path + "rosalind_ini5.txt", 'r')
solution_file = open(file_path + "rosalind_ini5_solution.txt", 'w+')

odd = True

for line in dataset_file:
    if odd == True:
        odd = False
    else:
        odd = True
        solution_file.write(line)

dataset_file.close()
solution_file.close()
