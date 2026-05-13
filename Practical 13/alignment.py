"""Simple non-gapped protein sequence comparison using BLOSUM62.

Pseudocode:
1. Read two protein sequences from FASTA files.
2. Read the BLOSUM62 scoring matrix.
3. For each aligned amino acid position:
   - add the BLOSUM62 substitution score to the total score
   - count the position as identical if both amino acids are the same
4. Print the sequences, total score, score per residue, and percent identity.
"""

from pathlib import Path


BLOSUM62 = """
   A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V
A  4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0
R -1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3
N -2  0  6  1 -3  0  0  0  1 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3
D -2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3
C  0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1
Q -1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2
E -1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2
G  0 -2  0 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3
H -2  0  1 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -2  2 -3
I -1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3
L -1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1
K -1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2
M -1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1
F -2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1
P -1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2
S  1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2
T  0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0
W -3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3
Y -2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1
V  0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4
"""


DEFAULT_COMPARISONS = [
    ("human_DLX5.fasta.txt", "mouse_DLX5.fasta.txt"),
    ("human_DLX5.fasta.txt", "Random Sequence.fasta"),
    ("mouse_DLX5.fasta.txt", "Random Sequence.fasta"),
]


def parse_blosum62(matrix_text):
    """Convert the text version of BLOSUM62 into a lookup dictionary."""
    lines = [line.split() for line in matrix_text.strip().splitlines()]
    amino_acids = lines[0]
    matrix = {}
    for row in lines[1:]:
        row_aa = row[0]
        for col_aa, score in zip(amino_acids, row[1:]):
            matrix[(row_aa, col_aa)] = int(score)
    return matrix


def read_fasta(path):
    """Read the first FASTA record from a file and return its name and sequence."""
    name = None
    chunks = []
    started = False

    with open(path, encoding="utf-8") as fasta_file:
        for line in fasta_file:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if started:
                    break
                started = True
                name = line[1:]
                continue
            if started:
                chunks.append(line.upper())

    if name is None:
        raise ValueError(f"No FASTA sequence found in {path}")

    return name, "".join(chunks)


def compare_sequences(seq1, seq2, matrix):
    """Compare two equal-length sequences with a non-gapped global alignment."""
    if len(seq1) != len(seq2):
        raise ValueError(
            "This practical uses non-gapped global alignments, so sequences must "
            f"have the same length ({len(seq1)} != {len(seq2)})."
        )

    total_score = 0
    identical = 0
    alignment_marks = []

    for aa1, aa2 in zip(seq1, seq2):
        # Look up the substitution score for this aligned amino acid pair.
        score = matrix[(aa1, aa2)]
        total_score += score

        # "|" marks identical residues; ":" marks conservative substitutions.
        if aa1 == aa2:
            identical += 1
            alignment_marks.append("|")
        elif score > 0:
            alignment_marks.append(":")
        else:
            alignment_marks.append(" ")

    length = len(seq1)
    return {
        "length": length,
        "score": total_score,
        "score_per_residue": total_score / length,
        "identical": identical,
        "percent_identity": identical / length * 100,
        "marks": "".join(alignment_marks),
    }


def print_wrapped_alignment(name1, seq1, name2, seq2, marks, width=70):
    print(name1)
    print(name2)
    for start in range(0, len(seq1), width):
        end = start + width
        print(seq1[start:end])
        print(marks[start:end])
        print(seq2[start:end])
        print()


def run_comparison(path1, path2, matrix):
    name1, seq1 = read_fasta(path1)
    name2, seq2 = read_fasta(path2)
    result = compare_sequences(seq1, seq2, matrix)

    print("=" * 78)
    print(f"Comparison: {Path(path1).name} vs {Path(path2).name}")
    print_wrapped_alignment(name1, seq1, name2, seq2, result["marks"])
    print(f"Length: {result['length']} amino acids")
    print(f"BLOSUM62 alignment score: {result['score']}")
    print(f"Score per residue: {result['score_per_residue']:.3f}")
    print(
        "Identical amino acids: "
        f"{result['identical']} / {result['length']} "
        f"({result['percent_identity']:.2f}%)"
    )
    print()
    return result


def main():
    base_dir = Path(__file__).resolve().parent
    matrix = parse_blosum62(BLOSUM62)

    print("Simple non-gapped global protein alignment using BLOSUM62")
    print("BLOSUM62 source: NCBI BLAST substitution matrix")
    print()

    for file1, file2 in DEFAULT_COMPARISONS:
        run_comparison(base_dir / file1, base_dir / file2, matrix)


if __name__ == "__main__":
    main()
