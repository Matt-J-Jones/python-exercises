def square_of_sum(number):
    total = 0
    for num in range (number + 1):
        total += num
    return total ** 2


def sum_of_squares(number):
    total = 0
    for num in range (number + 1):
        total += num ** 2
    return total


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
