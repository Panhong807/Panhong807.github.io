# This script reads a FASTA file containing cDNA sequences of Saccharomyces cerevisiae, identifies the longest open reading frame (ORF) for each gene, and determines the stop codon used in that ORF. The results are written to a new FASTA file with the gene name and the stop codon used.
infile = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
outfile = open("stop_genes.fa", "w")
seq = ""
gene_name = ""
for line in infile:
    line = line.strip()
    if line.startswith(">"):
        if seq != "":
            longest_length = 0
            best_stop = ""
            for i in range(len(seq) - 2):
                if seq[i:i+3] == "ATG":
                    j = i
                    length = 0
                    while j < len(seq) - 2:
                        codon = seq[j:j+3]
                        length += 3
                        if codon == "TAA" or codon == "TAG" or codon == "TGA":
                            if length > longest_length:
                                longest_length = length
                                best_stop = codon
                            break
                        j += 3
            if best_stop != "":
                outfile.write(">" + gene_name + ";" + best_stop + "\n")
                outfile.write(seq + "\n")
        gene_name = line.split()[0][1:]
        seq = ""
    else:
        seq += line
if seq != "":
    longest_length = 0
    best_stop = ""
    for i in range(len(seq) - 2):
        if seq[i:i+3] == "ATG":
            j = i
            length = 0
            while j < len(seq) - 2:
                codon = seq[j:j+3]
                length += 3

                if codon == "TAA" or codon == "TAG" or codon == "TGA":
                    if length > longest_length:
                        longest_length = length
                        best_stop = codon
                    break
                j += 3
    if best_stop != "":
        outfile.write(">" + gene_name + ";" + best_stop + "\n")
        outfile.write(seq + "\n")
infile.close()
outfile.close()

print("stop_genes.fa created")