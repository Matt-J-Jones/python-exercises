def is_isogram(string):
    cleaned_string = string.lower()
    if cleaned_string == "":
        return True
    letter_list = [*cleaned_string]
    letter_set = []
    for letter in letter_list:
        if letter.isalpha():
            letter_set.append(letter)
    if len(set(letter_set)) == len(letter_set):
        return True
    return False