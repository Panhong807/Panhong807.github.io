# This script defines a function to calculate the total mass of a protein based on its amino acid sequence.
# It uses a dictionary to store the mass of each amino acid and returns a clear error message if an invalid
# amino acid is found.
def protein_mass(sequence):
    """
    Input: sequence (string) - amino acid sequence
    Returns: total mass of protein (float, amu)

    Returns an error message if an invalid amino acid is found
    """
    aa_mass = {
        'A': 71.04, 'R': 156.10, 'N': 114.04, 'D': 115.03,
        'C': 103.01, 'E': 129.04, 'Q': 128.06, 'G': 57.02,
        'H': 137.06, 'I': 113.08, 'L': 113.08, 'K': 128.09,
        'M': 131.04, 'F': 147.07, 'P': 97.05, 'S': 87.03,
        'T': 101.05, 'W': 186.08, 'Y': 163.06, 'V': 99.07
    }
    total_mass = 0
    for aa in sequence:
        if aa not in aa_mass:
            return f"Error: invalid amino acid '{aa}'"
        total_mass += aa_mass[aa]
    return total_mass
seq = "ACDE"
print("Protein mass:", protein_mass(seq))
