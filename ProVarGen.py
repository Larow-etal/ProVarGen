import random

# Define amino acid groups based on similar properties
amino_acid_groups = {
    'hydrophobic': ['A', 'V', 'I', 'L', 'M', 'F', 'W', 'P'],
    'polar': ['S', 'T', 'N', 'Q', 'Y', 'C'],
    'positive': ['K', 'R', 'H'],
    'negative': ['D', 'E'],
    'special': ['G']
}

# Function to substitute amino acids
def substitute_amino_acids(sequence):
    new_sequence = []
    for aa in sequence:
        for group in amino_acid_groups.values():
            if aa in group:
                new_sequence.append(random.choice(group))
                break
        else:
            new_sequence.append(aa)  # If amino acid not found in any group, keep it unchanged
    return ''.join(new_sequence)

# Function to generate multiple variants
def generate_variants(sequence, num_variants=8):
    variants = []
    for _ in range(num_variants):
        variants.append(substitute_amino_acids(sequence))
    return variants

# Example usage
if __name__ == "__main__":
    original_sequence = "QINQVRPKLPLLKILHAAGAQGEMFTVKEVMHYLGQYIMVKQLYDQQEQHMVYCGGDLLGELLGRQSFSVKDPSPLYDMLRKNLVTLAT"
    variants = generate_variants(original_sequence)
    print(f"Original sequence: {original_sequence}")
    for i, variant in enumerate(variants, 1):
        print(f"Variant {i}: {variant}")
