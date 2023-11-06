def is_pangram(sentence):
    if sentence == '':
        return False
    alphabet = [*"abcdefghijklmnopqrstuvwxyz"]
    checked_sentence = [*sentence.lower()]
    if len([i for i in alphabet if i not in checked_sentence]) == 0:
        return True
    return False
    
    
