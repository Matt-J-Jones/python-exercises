def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    value = number
    step_count = 0
    while value != 1:
        step_count += 1
        if (value % 2) == 0:
            value /= 2
        else:
            value = value * 3 + 1
    return step_count