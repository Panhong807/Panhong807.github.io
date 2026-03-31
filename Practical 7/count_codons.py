import matplotlib.pyplot as plt 
stop=input("Enter the stop codon sequence (TAA, TAG, TGA): ") # Prompt the user to enter a stop codon sequence
codon_counts = {} # Initialize an empty dictionary to store codon counts
file=open('stop_genes.fa', 'r') # Open the file containing gene sequences
seq='' # Initialize an empty string to store the current gene sequence
for line in file: # Loop through each line in the file
    line=line.strip() # Remove any leading or trailing whitespace
    if line.startswith('>'): # Check if the line is a header (starts with '>')
        seq = '' # Reset the sequence variable for the next gene
    else:
        seq+=line # Append the current line to the sequence variable
        if stop in seq: # Check if the specified stop codon is present in the sequence
            pos=seq.find(stop) # Find the position of the stop codon in the sequence
            codon=seq[pos:pos+3] # Extract the codon from the sequence
            for i in range(0, len(seq)-2, 3): # Loop through the sequence in steps of 3 (codon length)
                current_codon=seq[i:i+3] # Get the current codon
                if current_codon == codon: # Check if the current codon matches the specified stop codon
                    if codon in codon_counts: # If the codon is already in the dictionary, increment its count
                        codon_counts[codon] += 1
                    else: # If the codon is not in the dictionary, add it with a count of 1
                        codon_counts[codon] = 1
labels=list(codon_counts.keys()) # Get the list of codon labels from the dictionary keys
sizes=list(codon_counts.values()) # Get the list of codon counts from the dictionary values
plt.figure() # Create a new figure for the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%') # Create a pie chart with the codon counts and labels
plt.title(f"Distribution of {stop} Codons in stop_genes.fa") # Set the title of the pie chart
plt.axis('equal') # Ensure the pie chart is circular
plt.savefig("codon_pie.png") # Save the pie chart as a PNG file
plt.show() # Display the pie chart
plt.close() # Close the plot to free up memory
file.close() # Close the file after processing