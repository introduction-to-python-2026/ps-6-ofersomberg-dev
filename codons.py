def create_codon_dict(file_path):
    mapping_between_codons_and_amino_acids = {}
    with open(file_path, 'r') as f:
        for line in f:
            if not line.strip():
                continue
            cells = line.strip().split('\t') # Changed 'row' to 'line'
            if len(cells) < 3:
                continue
            codon = cells[0]
            amino_acid = cells[2]
            mapping_between_codons_and_amino_acids[codon] = amino_acid
    return mapping_between_codons_and_amino_acids


