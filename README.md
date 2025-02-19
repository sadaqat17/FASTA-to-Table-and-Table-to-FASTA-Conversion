**Sequence Format Conversion Scripts:**

This repository contains Python scripts to convert biological sequence data between FASTA and CSV formats.

**Features:**

**FASTA to CSV:** Converts a FASTA file into a CSV file containing accession IDs and sequences.

**CSV to FASTA:** Converts a CSV file containing accession IDs and sequences back into FASTA format.

**Prerequisites:**

Before running these scripts, ensure you have Python installed and the necessary dependencies:

-Python 3.x (preferably 3.6+)

-Biopython library

**To install the required library**

pip install biopython

**Clone repository:**

git clone https://github.com/sadaqat17/FASTA-to-Table-and-Table-to-FASTA-Conversion.git

**Scripts**

**1. FASTA to CSV Conversion**

Description: Converts a FASTA file into a CSV table. The CSV will contain two columns:

**Accession:** Sequence ID (or header)

**Sequence:** The sequence string

**Usage:**

python Fasta_to_table_convert.py -i input.fasta -o output.csv


**Arguments:**

-i or --input: Path to the input FASTA file.

-o or --output: Path where the output CSV file will be saved.

**2. CSV to FASTA Conversion**

Description: Converts a CSV or Table file into a FASTA table. 

**Usage:** 

python Table_to_fasta_convert.py -i input.csv -o output.fasta

**Arguments:**

-i or --input: Path to the input CSV file.

-o or --output: Path where the output FASTA file will be saved.

**Notes:**

-Ensure that your FASTA file uses the correct format, with each sequence beginning with a > followed by the accession ID and the sequence on the next line(s).

-The CSV file for the CSV to FASTA conversion should have two columns: the first column should be the accession and the second column should be the sequence string.
