def score(x, y):
    distance_from_centre = (x**2 + y**2)**0.5
    if 0 <= distance_from_centre <= 1:
        return 10
    if 1 < distance_from_centre <= 5:
        return 5
    if 5 < distance_from_centre <= 10:
        return 1
    return 0
