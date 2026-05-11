# This script asks the user for a stop codon, reads the original yeast cDNA FASTA file,
# finds the longest ORF ending in that stop codon for each gene, counts the in-frame codons
# upstream of that stop codon, and saves a pie chart of codon usage.
import matplotlib.pyplot as plt
stop = input("Enter stop codon (TAA, TAG, TGA): ")
stop = stop.upper()

if stop not in ["TAA", "TAG", "TGA"]:
    print("Error: stop codon must be TAA, TAG, or TGA")
    exit()

file = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
seq = ""
codon_count = {}


def count_codons_for_sequence(seq, stop, codon_count):
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


for line in file:
    line = line.strip()
    if line.startswith(">"):
        if seq != "":
            count_codons_for_sequence(seq, stop, codon_count)
        seq = ""
    else:
        seq = seq + line
if seq != "":
    count_codons_for_sequence(seq, stop, codon_count)
file.close()
labels = []
sizes = []
for codon in codon_count:
    if codon_count[codon] > 0:
        labels.append(codon)
        sizes.append(codon_count[codon])
plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Codon usage for " + stop)
plt.xlabel("Codons")
plt.savefig("codon_usage_" + stop + ".png")
plt.close()
print("Pie chart saved")
