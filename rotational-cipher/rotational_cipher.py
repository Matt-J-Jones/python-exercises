ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def rotate(text, key):
    encoded_text = ""
    new_alphabet = ALPHABET[key:len(ALPHABET)] + ALPHABET[0:key]
    for char in text:
        if char.isalpha():
            new_letter = new_alphabet[check_char_index(char)]
            if char.isupper():
                encoded_text = encoded_text + new_letter.upper()
            else:
                encoded_text = encoded_text + new_letter
        else:
            encoded_text = encoded_text + char
    return encoded_text

def check_char_index(char):
    return ALPHABET.rfind(char.lower())
