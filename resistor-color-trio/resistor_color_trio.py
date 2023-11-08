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

def label(colors):
    # return  ohms_prefix(band_values(colors), COLORS_DICT[colors[2]])
    return convert_results(
        str(COLORS_DICT[colors[0]])
        + str(COLORS_DICT[colors[1]])
        + ("0"*COLORS_DICT[colors[2]]))

def convert_results(number_str):
    ohms_prefix = ['ohms', 'kiloohms', 'megaohms', 'gigaohms']
    count = 0
    for number in number_str:
        if number == '0':
            count += 1
    for x in range(int(count/3)):
        number_str = number_str.replace('000', '')
    return str(int(number_str)) + " " + ohms_prefix[int(count/3)]
