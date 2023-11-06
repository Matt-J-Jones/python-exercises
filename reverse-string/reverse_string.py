def reverse(text):
    arr = []
    for letter in text:
        arr.append(letter)
    arr.reverse()
    return "".join(arr)
