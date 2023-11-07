def is_valid(isbn):
    isbn_to_test = [*isbn.replace("-", "")]
    if len(isbn_to_test) == 10:
        multiplier = 10
        result = 0
        if isbn_to_test[-1] == "X":
            isbn_to_test[-1] = 10
        for item in isbn_to_test:
            if str(item).isalpha():
                return False
            result = result + (int(item) * multiplier)
            multiplier -= 1
        if (result % 11) == 0:
            return True
    return False
