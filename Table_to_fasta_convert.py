# Import argparse module to allow parsing of command-line arguments
import argparse
# Import SeqRecord and Seq from Biopython to handle sequence records and sequences
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
# Import the csv module to read CSV files in Python
import csv

# Set up argument parsing
parser = argparse.ArgumentParser(description="Convert CSV table to FASTA format")
# Define the command-line argument for the input CSV file, which is required
parser.add_argument("-i", "--input", required=True, help="Input CSV file")
# Define the command-line argument for the output FASTA file, which is also required
parser.add_argument("-o", "--output", required=True, help="Output FASTA file")
# Parse the arguments from the command line
args = parser.parse_args()

# Input and output file paths are assigned based on the parsed arguments
input_table = args.input
output_fasta = args.output

# Open the input CSV file for reading
with open(input_table, "r") as csvfile:
    # Create a CSV reader object to read the file
    reader = csv.reader(csvfile)
    # Read the header row (skip it since we only need data rows)
    header = next(reader)
    
    # Open the output FASTA file in write mode
    with open(output_fasta, "w") as fasta_file:
        # Iterate through each row in the CSV
        for row in reader:
            # The first column should be the accession (ID), and the second column should be the sequence
            accession = row[0]
            sequence = row[1]
            
            # Create a SeqRecord object with the accession as the ID and the sequence
            seq_record = SeqRecord(Seq(sequence), id=accession, description="")
            
            # Write the SeqRecord object in FASTA format to the output file
            fasta_file.write(seq_record.format("fasta"))

# Print a success message indicating the output file location
print(f"CSV converted to FASTA successfully! Output saved to {output_fasta}")
