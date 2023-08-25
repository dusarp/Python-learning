import os
import numpy as np

# set the sample folder and output folder paths
sample_folder = r'C:\Users\arpi\Desktop\proba' # modify
output_folder = os.path.join(sample_folder, 'mean')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# get a list of all the TXT files in the sample folder
files = [f for f in os.listdir(sample_folder) if f.endswith('.txt')]

# process each TXT file
for file in files:
    # read in the spectrum from the TXT file
    data = np.loadtxt(os.path.join(sample_folder, file))
    x = data[:, 0]
    y = data[:, 1:]

    # calculate the mean spectrum
    mean_y = np.mean(y, axis=1)
    mean_spectrum = np.column_stack((x, mean_y))

    # write the mean spectrum to a new TXT file in the output folder
    output_file = os.path.join(output_folder, file)
    np.savetxt(output_file, mean_spectrum, delimiter='\t')
