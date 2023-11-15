def rows(letter):
    if letter == "A":
        return ["A"]
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_index = alphabet.index(letter)
    alpha_slice = alphabet[0:letter_index+1]
    diamond = []
    for index, value in enumerate(alpha_slice):
        diamond.append(get_row(value, index, letter_index + 1))

    return diamond + diamond[::-1][1:len(diamond)]

def get_row(letter, posn, width):
    empty_row = " " * width
    new_row = list(empty_row)
    # new_row[posn] = letter
    return_string = list(empty_row[0:-1]) + new_row
    midpoint = len(return_string)//2
    return_string[midpoint + posn] = letter
    return_string[midpoint - posn] = letter
    return "".join(return_string)
