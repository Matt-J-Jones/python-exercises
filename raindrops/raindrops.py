def convert(number):
    x, y, z = (number % 3), (number % 5), (number % 7)
    return_string = ""
    if x == 0:
        return_string = return_string + 'Pling'
    if y == 0:
        return_string = return_string + 'Plang'
    if z == 0:
        return_string = return_string + 'Plong'
    if x != 0 and y != 0 and z != 0:
        return_string = str(number)
    return return_string
