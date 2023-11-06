def is_paired(input_string):
    cleaned_string = ""
    for char in input_string:
        if char in "{([])}":
            cleaned_string = cleaned_string + char
    string_to_return = cleaned_string
    for count in range(len(cleaned_string)):
        string_to_return = remove_pairs(string_to_return)
    if len(string_to_return) == 0:
        return True
    return False

def remove_pairs(string):
    return_string = string.replace("[]", "")
    return_string = return_string.replace("{}", "")
    return_string = return_string.replace("()", "")
    return return_string