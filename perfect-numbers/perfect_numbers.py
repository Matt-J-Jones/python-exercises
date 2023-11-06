def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    sum_factors = return_factors_total(number)
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    if number == sum_factors:
        return "perfect"
    if number < sum_factors:
        return "abundant"
    if number > sum_factors:
        return "deficient"

def return_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def return_factors_total(number):
    factors = []
    for x in range(1, number):
        if (number%x) == 0:
            factors.append(x)
    return return_sum(factors)
