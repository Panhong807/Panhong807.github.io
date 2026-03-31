# This code is designed to find the longest open reading frame (ORF) in a given RNA sequence. An ORF is a sequence of codons that starts with a start codon (AUG) and ends with a stop codon (UAA, UAG, or UGA). The code iterates through the RNA sequence, identifies potential ORFs, and keeps track of the longest one found.
import re # Import the regular expression module to work with patterns in strings
seq='AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
start_codon='AUG'  # Define the start codon
stop_codons=['UAA', 'UAG', 'UGA']  # Define the stop codons
longest_orf=''  # Initialize an empty string to store the longest ORF
max_length=0   # Initialize a variable to keep track of the maximum length of the ORF
for i in range(len(seq)): # Loop through each position in the sequence
    if seq[i:i+3] == start_codon:  # Check if the current position has the start codon
        for j in range(i+3, len(seq), 3):  # Loop through the sequence in steps of 3 (codon length)
            codon = seq[j:j+3]  # Get the current codon
            if codon in stop_codons:  # Check if the current codon is a stop codon
                orf_length = j + 3 - i  # Calculate the length of the ORF
                if orf_length > max_length:  # Check if this ORF is longer than the previously found longest ORF
                    longest_orf = seq[i:j+3]  # Update the longest ORF
                    max_length = orf_length  # Update the maximum length
                break  # Stop searching for this ORF once a stop codon is found
print("Longest ORF:", longest_orf)  # Print the longest ORF found
print("Length:", max_length)  # Print the length of the longest ORF found