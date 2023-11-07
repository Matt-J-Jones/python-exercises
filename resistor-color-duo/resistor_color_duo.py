COLORS_DICT = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9
}

def value(colors):
    result = ""
    for band in colors:
        result = result + str(COLORS_DICT[band])
    return int(result[0:2])
