# This code stores gene expression levels in a dictionary, adds MYC data,
# prints the updated dictionary, looks up a selected gene, calculates the
# average expression level, and displays a labelled bar chart.
import matplotlib.pyplot as plt

gene_expression = {
    'TP53': 12.4,
    'EGFR': 15.1,
    'BRCA1': 8.2,
    'PTEN': 5.3,
    'ESR1': 10.7,
}

gene_expression['MYC'] = 11.6
print("Gene expression dictionary:", gene_expression)

genes = list(gene_expression.keys())
expression_levels = list(gene_expression.values())

plt.figure(figsize=(8, 5))
plt.bar(genes, expression_levels, color='skyblue')
plt.xlabel('Genes')
plt.ylabel('Expression Levels')
plt.title('Gene Expression Levels')
plt.show()

gene_of_interest = 'BRCA1'
if gene_of_interest in gene_expression:
    print(f"Expression level of {gene_of_interest}: {gene_expression[gene_of_interest]}")
else:
    print(f"{gene_of_interest} not found in the gene expression dictionary.")

average_expression = sum(expression_levels) / len(expression_levels)
print(f"Average expression level across all genes: {average_expression:.2f}")
