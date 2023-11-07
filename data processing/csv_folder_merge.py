#merge CSV files in one directry, while ignoring the headers in all but the first file (so that the resulting merged file only has one header)

import os
import pandas as pd

# Directory containing CSV files
directory = "/path/to/your/directory"

# Output CSV file
output_file = "merged_output.csv"

# Initialize an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Iterate through the files in the directory
for i, filename in enumerate(os.listdir(directory)):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        # Read the CSV file into a DataFrame
        data = pd.read_csv(file_path)
        # Ignore headers for all but the first file
        if i == 0:
            merged_data = data
        else:
            merged_data = merged_data.append(data, ignore_index=True)

# Write the merged data to the output CSV file
merged_data.to_csv(output_file, index=False)

print(f"Merged data saved to {output_file}")
