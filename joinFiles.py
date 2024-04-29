import csv
import glob
import os

# Glob pattern to match all CSV files in the directory
joined_files = os.path.join("./temp", "*.csv")

# A list of all joined files is returned
joined_list = glob.glob(joined_files)

# Open the final CSV file for writing
with open('outputs/pataky-test-29-4-24.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # Iterate over each joined file
    for file_path in joined_list:
        # Open the joined file
        with open(file_path, 'r', newline='', encoding='utf-8') as joined_file:
            # Read the joined file line by line and write its contents to the final CSV file
            for line in joined_file:
                writer.writerow(line.strip().split(','))  # Write each line to the final CSV file
