# This script reads a FASTA file containing gene sequences, identifies any stop codons (TAA, TAG, TGA) present in the sequences, and writes the gene names along with the found stop codons and their sequences to an output FASTA file.
input_file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') #open the file
output_file=open('stop_genes.fa','w') #open the output file
gene_name='' #initialize the gene name variable
seq='' #initialize the sequence variable
for line in input_file: #loop through each line in the input file
    line=line.strip() #remove any leading or trailing whitespace
    if line.startswith('>'): #check if the line is a header (starts with '>')
        if seq!='': #if there is a sequence stored, write it to the output file
            found_stops=set() #initialize a set to store found stop codons
            for i in range(0, len(seq)-2, 3): #loop through the sequence in steps of 3 (codon length)
                codon=seq[i:i+3] #get the current codon
                if codon in ['TAA', 'TAG', 'TGA']: #check if the codon is a stop codon
                    found_stops.add(codon) #add the stop codon to the set of found stop codons
            if found_stops: #if any stop codons were found
                output_file.write(f">{gene_name}{''.join(found_stops)}\n") #write the gene name and found stop codons to the output file
                output_file.write(seq + '\n') #write the sequence to the output file
        gene_name=line.split()[0][1:] #update the gene name (remove the '>' character)
        seq='' #reset the sequence variable for the next gene
    else:
        seq+=line #append the current line to the sequence variable
if seq!='': #after the loop, check if there is a sequence stored for the last gene
    found_stops=set() #initialize a set to store found stop codons
    for i in range(0, len(seq)-2, 3): #loop through the sequence in steps of 3 (codon length)
        codon=seq[i:i+3] #get the current codon
        if codon in ['TAA', 'TAG', 'TGA']: #check if the codon is a stop codon
            found_stops.add(codon) #add the stop codon to the set of found stop codons
    if found_stops: #if any stop codons were found
        output_file.write(f">{gene_name}{''.join(found_stops)}\n") #write the gene name and found stop codons to the output file
        output_file.write(seq + '\n') #write the sequence to the output file
input_file.close() #close the input file
output_file.close() #close the output file