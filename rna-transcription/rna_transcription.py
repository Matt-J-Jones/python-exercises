def to_rna(dna_strand):
    dna_dict = {
        '' : '',
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    rna_return = ""
    for char in dna_strand:
        rna_return = rna_return + dna_dict[char]
    return rna_return