def response(hey_bob):
    cleaned_text = hey_bob.strip()
    if cleaned_text == "":
        return "Fine. Be that way!"
    if cleaned_text.isupper():
        if cleaned_text[-1] == '?':
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if cleaned_text[-1] == '?':
        return "Sure."
    return "Whatever."
