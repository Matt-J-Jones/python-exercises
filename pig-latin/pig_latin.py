def translate(text):
    final_text = []
    for word in text.split():
        final_text.append(return_words(word))
    return " ".join(final_text)

def return_words(word):
    vowels = ["a", "e", "i", "o", "u", "xr", "yt"]
    const_sounds = ["ch", "sch", "thr", "th"]
    if "y" in word and word[0] != "y":
        index = word.rfind("y")
        count = 0
        for letter in word[0:index]:
            if letter not in "aeiou":
                count += 1
        if count == index:
            return word[index:len(word)]+word[0:index]+"ay"
    for vowel in vowels:
        if word[0:len(vowel)] == vowel:
            return word + "ay"
    for const in const_sounds:
        if word[0:len(const)] == const:
            return word[len(const): len(word)] + word[0:len(const)] + "ay"
    if word[0] == 'q' and word[1] == 'u':
        return word[2:len(word)] + word[0:2] + "ay"
    if word[1] == 'q':
        return word[3:len(word)] + word[0:3] + "ay"
    return word[1:len(word)]+word[0] + "ay"
