Sequence Format Conversion Scripts
This repository contains Python scripts to convert biological sequence data between FASTA and CSV formats.

FASTA to CSV: Converts a FASTA file into a CSV file containing accession IDs and sequences.
CSV to FASTA: Converts a CSV file containing accession IDs and sequences back into FASTA format.
Prerequisites
Before running these scripts, ensure you have Python installed and the necessary dependencies.

Python 3.x (preferably 3.6+)
Biopython library (for working with biological sequence data)
To install the required library, run:

bash
Copy
Edit
pip install biopython
Scripts
1. FASTA to CSV Conversion
Description:
Converts a FASTA file into a CSV table. The CSV contains two columns:

Accession: Sequence ID (or header)
Sequence: The sequence string
Usage:
bash
Copy
Edit
python Fasta_to_table_convert.py -i input.fasta -o output.csv
Arguments:
-i or --input: Path to the input FASTA file.
-o or --output: Path where the output CSV file will be saved.
Example:
bash
Copy
Edit
python Fasta_to_table_convert.py -i input.fasta -o output.csv
If the input file input.fasta is as follows:

fasta
Copy
Edit
>seq1
ATGCGTAC
>seq2
GGCTAGTC
>seq3
TACGATCG
The output output.csv will be:

csv
Copy
Edit
Accession,Sequence
seq1,ATGCGTAC
seq2,GGCTAGTC
seq3,TACGATCG
2. CSV to FASTA Conversion
Description:
Converts a CSV file containing two columns (Accession and Sequence) into a FASTA file. The CSV should have:

Accession: Sequence ID
Sequence: The sequence string
Usage:
bash
Copy
Edit
python Table_to_fasta_convert.py -i input.csv -o output.fasta
Arguments:
-i or --input: Path to the input CSV file.
-o or --output: Path where the output FASTA file will be saved.
Example:
bash
Copy
Edit
python Table_to_fasta_convert.py -i input.csv -o output.fasta
If the input file input.csv looks like:

csv
Copy
Edit
Accession,Sequence
seq1,ATGCGTAC
seq2,GGCTAGTC
seq3,TACGATCG
The output output.fasta will be:

fasta
Copy
Edit
>seq1
ATGCGTAC
>seq2
GGCTAGTC
>seq3
TACGATCG
Notes:
Ensure that your FASTA file uses the correct format, with each sequence beginning with a > followed by the accession ID and the sequence on the next line(s).
The CSV file for the CSV to FASTA conversion should have two columns, where the first column is the accession and the second column is the sequence string.
