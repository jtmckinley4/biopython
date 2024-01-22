#!/usr/bin/env python

# Import necessary modules from BioPython
from Bio import SeqIO
from Bio.Seq import Seq

# Function to calculate reverse complement and write to a new file
def reverse_complement_fasta(input_filename, output_filename):
    # Open the input FASTA file in read mode
    with open(input_filename, 'r') as input_file:
        # Use SeqIO to parse the FASTA file and iterate over each sequence
        for record in SeqIO.parse(input_file, 'fasta'):
            # Get the sequence as a Bio.Seq object
            sequence = Seq(str(record.seq))
            
            # Calculate the reverse complement
            reverse_complement = sequence.reverse_complement()
            
            # Print the header and reverse complement sequence
            print(f"> {record.id}\n{reverse_complement}\n")
            
            # Write the results to the output file
            with open(output_filename, 'a') as output_file:
                output_file.write(f"> {record.id}\n{reverse_complement}\n")

if __name__ == "__main__":
    # Get the input and output file names from the command line arguments
    import sys
    if len(sys.argv) != 3:
        print("Usage: python script.py input.fasta output.fasta")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Call the function with the provided input and output file names
    reverse_complement_fasta(input_filename, output_filename)

