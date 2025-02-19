# Importing necessary libraries
from Bio import SeqIO  # SeqIO is used to handle sequence data, though it's not used directly here
import csv  # CSV module to handle reading CSV files
import argparse  # argparse to handle command-line arguments

# Setting up the argument parser to handle user input for CSV file and output FASTA file
parser = argparse.ArgumentParser(description="Convert CSV table to FASTA")  
parser.add_argument("-i", "--input", required=True, help="Input CSV file")  # Input CSV file argument
parser.add_argument("-o", "--output", required=True, help="Output FASTA file")  # Output FASTA file argument
args = parser.parse_args()  # Parse the command-line arguments

# Assign input and output file paths from parsed arguments
input_file = args.input
output_file = args.output

# Opening the input CSV file for reading
with open(input_file, "r") as csvfile:
    reader = csv.reader(csvfile)  # Create a CSV reader object to iterate through rows
    # Opening the output FASTA file for writing
    with open(output_file, "w") as fasta_out:
        # Looping through each row in the CSV file
        for row in reader:
            if row:  # Check if the row is not empty
                accession = row[0]  # The first column is assumed to be the accession ID
                sequence = row[1]  # The second column is assumed to be the sequence itself
                if accession and sequence:  # Ensure both accession and sequence are non-empty
                    # Write the FASTA formatted sequence to the output file
                    fasta_out.write(f">{accession}\n{sequence}\n")
                else:
                    # If either accession or sequence is missing, skip this entry and print a warning
                    print(f"Skipping malformed entry: {row}")
    
# Once the conversion is complete, notify the user and show the output file location
print(f"Conversion to FASTA complete! Output saved to {output_file}")
