def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    hamming_value = 0
    for count, value in enumerate(strand_a):
        if value != strand_b[count]:
            hamming_value += 1
    return hamming_value
