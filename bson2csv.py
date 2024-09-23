
import os
import bson
import pandas as pd
import sys

def bson_to_csv(input_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".bson"):
            # Construct full file paths
            input_filepath = os.path.join(input_folder, filename)
            output_filename = filename.replace(".bson", ".csv")
            output_filepath = os.path.join(output_folder, output_filename)

            """ @author: vicervin
                Python3.5 
                Requires: pandas, pymongo (bson comes from this)
                input: bson file 
                output: csv file with same name
            """
            # Read BSON file
            with open(input_filepath, 'rb') as f:
                data = bson.decode_all(f.read())

            # Convert BSON data to DataFrame
            df = pd.DataFrame(data)

            # Save DataFrame to CSV
            try:
                df.to_csv(output_filepath, index=False, sep = ',')
                print("Data has been successfully converted")
            except:
                print("An exception occurred")

            

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    bson_to_csv(input_folder, output_folder)

