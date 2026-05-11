# This script reads a FASTA file containing cDNA sequences of Saccharomyces cerevisiae,
# identifies genes that contain at least one in-frame stop codon in an ORF that starts with ATG,
# and writes them to stop_genes.fa with only the gene name and the stop codon types found.

STOP_CODONS = ["TAA", "TAG", "TGA"]


def find_stop_codons(seq):
    found_stops = set()

    for i in range(len(seq) - 2):
        if seq[i:i + 3] == "ATG":
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j + 3]
                if codon in STOP_CODONS:
                    found_stops.add(codon)
                    break

    return found_stops


infile = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
outfile = open("stop_genes.fa", "w")
seq = ""
gene_name = ""

for line in infile:
    line = line.strip()
    if line.startswith(">"):
        if seq != "":
            found_stops = find_stop_codons(seq)
            if found_stops:
                stop_text = ",".join(sorted(found_stops))
                outfile.write(">" + gene_name + ";" + stop_text + "\n")
                outfile.write(seq + "\n")
        gene_name = line.split()[0][1:]
        seq = ""
    else:
        seq += line

if seq != "":
    found_stops = find_stop_codons(seq)
    if found_stops:
        stop_text = ",".join(sorted(found_stops))
        outfile.write(">" + gene_name + ";" + stop_text + "\n")
        outfile.write(seq + "\n")

infile.close()
outfile.close()

print("stop_genes.fa created")
