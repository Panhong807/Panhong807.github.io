# This script defines a function to calculate the total mass of a protein based on its amino acid sequence. It uses a dictionary to store the mass of each amino acid and iterates through the sequence to sum up the total mass. If an invalid amino acid is found, it raises an error.
def protein_mass(sequence):
    """
    Input: sequence (string) - amino acid sequence
    Returns: total mass of protein (float, amu)

    Raises an error if invalid amino acid is found
    """
    aa_mass = {
        'A': 89.1, 'R': 174.2, 'N': 132.1, 'D': 133.1,
        'C': 121.2, 'E': 147.1, 'Q': 146.2, 'G': 75.1,
        'H': 155.2, 'I': 131.2, 'L': 131.2, 'K': 146.2,
        'M': 149.2, 'F': 165.2, 'P': 115.1, 'S': 105.1,
        'T': 119.1, 'W': 204.2, 'Y': 181.2, 'V': 117.1
    }
    total_mass = 0
    for aa in sequence:
        if aa not in aa_mass:
            raise ValueError(f"Invalid amino acid: {aa}")
        total_mass += aa_mass[aa]
    return total_mass
seq = "ACDE"
print("Protein mass:", protein_mass(seq))