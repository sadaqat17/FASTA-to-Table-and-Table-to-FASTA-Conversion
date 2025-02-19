#Instruction
#Before running this script install biopython(command: pip install biopython) into your environemnt
#after that run it as: python Fasta_to_table_convert -i input_file_path -o output_file_path(name and path)
#Suppose your input file name is "input.fasta" and it is in the same directory where script is present then run it as follow to make the output file name "output.csv" as:
#python Fasta_to_table_convert -i input.fasta -o output.csv
#*************End of instruction***************

# Import argparse module to allow parsing of command-line arguments
import argparse
# Import the SeqIO module from Biopython to handle sequence data in different formats such as FASTA, GenBank, etc.
from Bio import SeqIO
# Import the csv module to read and write to CSV files in Python
import csv

# Set up argument parsing
parser = argparse.ArgumentParser(description="Convert FASTA to CSV table format")
# Define the command-line argument for the input file, which is required
parser.add_argument("-i", "--input", required=True, help="Input FASTA file")
# Define the command-line argument for the output file, which is also required
parser.add_argument("-o", "--output", required=True, help="Output CSV file")
# Parse the arguments from the command line
args = parser.parse_args()

# Input and output file paths are assigned based on the parsed arguments
input_fasta = args.input
output_table = args.output

# Open the output CSV file in write mode
with open(output_table, "w", newline="") as csvfile:
    # Create a CSV writer object to write to the file
    writer = csv.writer(csvfile)
    # Write the header row with "Accession" and "Sequence" as column names
    writer.writerow(["Accession", "Sequence"])
    
    # Iterate over each record in the input FASTA file using SeqIO.parse
    # This function reads and parses each sequence record in the FASTA file
    for record in SeqIO.parse(input_fasta, "fasta"):
        # Write the accession (record.id) and the sequence (record.seq) to the CSV file
        # Convert the sequence to a string before writing
        writer.writerow([record.id, str(record.seq)])

# Print a success message to the user indicating the output file location
print(f"FASTA converted to CSV successfully! Output saved to {output_table}")
