def equilateral(sides):
    for side in sides:
        if side == 0:
            return False
    if sides[0] == sides[1] == sides[2]:
        return True
    return False

def isosceles(sides):
    sum_sides = sides[0] + sides[1] + sides[2]
    for side in sides:
        if side > (sum_sides/2):
            return False
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
        return True
    return False


def scalene(sides):
    sum_sides = sides[0] + sides[1] + sides[2]
    for side in sides:
        if side > (sum_sides/2):
            return False
    if sides[0] != sides[1] != sides[2] and sides[0] != sides[2]:
        return True
    return False
