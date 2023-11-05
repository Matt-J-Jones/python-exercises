def is_armstrong_number(number):
    if number == 0:
        return True
    number_of_digits = len(str(number))
    square = []
    for count in range(number_of_digits):
        square.append(return_digit(number, count)**number_of_digits)
    total = 0
    for item in square:
        total += item
    if total == number:
        return True
    return False

def return_digit(number, digit):
    return int(str(number)[digit])
