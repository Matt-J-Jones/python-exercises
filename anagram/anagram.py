def find_anagrams(word, candidates):
    return_list = []

    word_key = sorted(word.lower())
    for item in candidates:
        word_to_check = sorted(item.lower())
        if word_to_check == word_key and word.lower() != item.lower():
            return_list.append(item)

    return return_list
