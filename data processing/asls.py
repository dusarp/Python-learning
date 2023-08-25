import os

# Define the sample folder path and navigate to it
sample_folder = r'D:\Arpad\analyzed\Raman\Calibrated\20221214\despike\'  #ezt kell modositani
os.chdir(sample_folder)

# Create an output folder and navigate to it
output_folder = os.path.join(sample_folder, 'asls')
os.makedirs(output_folder, exist_ok=True)
os.chdir(output_folder)

# Get a list of all the TXT files in the sample folder
files = [f for f in os.listdir(sample_folder) if f.endswith('.txt')]

# Loop through each TXT file in the sample folder
for file in files:
    # Load the data from the TXT file, x: wavenumbers, y1...yN Raman signal (tabular)
    data = np.loadtxt(os.path.join(sample_folder, file))
    x = data[:, 0]
    y = data[:, 1:]

    # Loop through each column in y
    spektrum_norm2 = []
    for i in range(y.shape[1]):
        y1 = y[:, i]
        spektrum_norm = asLS_baseline_v1(y1)
        spektrum_norm2.append(y1 - spektrum_norm)

    # Combine the x and normalized y values into a single array
    spektrum_norm3 = np.column_stack((x, np.array(spektrum_norm2)))

    # Save the normalized data to a new TXT file in the output folder
    np.savetxt(os.path.join(output_folder, file), spektrum_norm3, delimiter='\t')