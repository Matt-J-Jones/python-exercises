ALPHA = "abcdefghijklmnopqrstuvwxyz"
ALPHA_REV = ALPHA[::-1]

def encode(plain_text):
    encoded_text = ""
    for letter in plain_text:    
        if letter.lower() in ALPHA:
            encoded_text = encoded_text + ALPHA_REV[ALPHA.index(letter.lower())]
        elif letter not in " .,!?":
            encoded_text = encoded_text + letter
    return " ".join([encoded_text[i:i+5] for i in range(0, len(encoded_text), 5)])

def decode(ciphered_text):
    decoded_text = ""
    for letter in ciphered_text:
        if letter in ALPHA_REV:
            decoded_text = decoded_text + ALPHA[ALPHA_REV.index(letter)]
        else:
            decoded_text = decoded_text + letter
    return decoded_text.replace(" ", "")
