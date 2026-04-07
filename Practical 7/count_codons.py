# This script reads a FASTA file containing cDNA sequences of Saccharomyces cerevisiae, identifies the longest open reading frame (ORF) for each gene, and determines the stop codon used in that ORF. The results are written to a new FASTA file with the gene name and the stop codon used.
import matplotlib.pyplot as plt
stop = input("Enter stop codon (TAA, TAG, TGA): ")
stop = stop.upper()
file = open("stop_genes.fa", "r")
seq = ""
codon_count = {}
for line in file:
    line = line.strip()
    if line.startswith(">"):
        if seq != "":
            longest_orf = ""
            for i in range(len(seq) - 2):
                if seq[i:i+3] == "ATG":
                    current_orf = ""
                    for j in range(i, len(seq)-2, 3):
                        codon = seq[j:j+3]
                        current_orf = current_orf + codon
                        if codon == stop:
                            if len(current_orf) > len(longest_orf):
                                longest_orf = current_orf
                            break
            if longest_orf != "":
                coding = longest_orf[:-3]
                for i in range(0, len(coding), 3):
                    codon = coding[i:i+3]
                    if codon in codon_count:
                        codon_count[codon] = codon_count[codon] + 1
                    else:
                        codon_count[codon] = 1
        seq = ""
    else:
        seq = seq + line
if seq != "":
    longest_orf = ""

    for i in range(len(seq) - 2):
        if seq[i:i+3] == "ATG":

            current_orf = ""

            for j in range(i, len(seq)-2, 3):
                codon = seq[j:j+3]
                current_orf = current_orf + codon

                if codon == stop:
                    if len(current_orf) > len(longest_orf):
                        longest_orf = current_orf
                    break
    if longest_orf != "":
        coding = longest_orf[:-3]
        for i in range(0, len(coding), 3):
            codon = coding[i:i+3]
            if codon in codon_count:
                codon_count[codon] = codon_count[codon] + 1
            else:
                codon_count[codon] = 1
file.close()
labels = []
sizes = []
for codon in codon_count:
    if codon_count[codon] > 0:
        labels.append(codon)
        sizes.append(codon_count[codon])
plt.figure()
plt.pie(sizes, labels=labels)
plt.title("Codon usage for " + stop)
plt.savefig("codon_usage_" + stop + ".png")
plt.close()
print("Pie chart saved")