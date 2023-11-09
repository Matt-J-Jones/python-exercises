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

TOLERANCE_DICT = {
    'grey' : ' ±0.05%',
    'violet' : ' ±0.1%',
    'blue' : ' ±0.25%',
    'green' : ' ±0.5%',
    'brown' : ' ±1%',
    'red' : ' ±2%',
    'gold' : ' ±5%',
    'silver' : ' ±10%'
}

def resistor_label(colors):
    if colors == ['black']:
        return "0 ohms"

    values = ""
    tolerances = ""
    zeroes = ""

    for band in colors[0:-2]:
        values = values + str(COLORS_DICT[band])
    zeroes = "0" * COLORS_DICT[colors[-2]]
    tolerances = TOLERANCE_DICT[colors[-1]]

    return format_values(values + zeroes) + get_prefix(values+zeroes) + tolerances

def get_prefix(number_string):
    ohms_prefix = [' ohms', ' kiloohms', ' megaohms', ' gigaohms']
    count = 0
    values = number_string
    while '000' in values:
        count += 1
        values = values.replace('000', '')
    if len(values) > 3:
        count += 1
    return ohms_prefix[count]

def format_values(values):
    dec_point_posn = 0
    if len(values) > 3:
        dec_point_posn = len(values)%3
        formatted_values = values[0:dec_point_posn] + '.' + values[dec_point_posn:len(values)]
        formatted_values = formatted_values.replace('0', '')
        if formatted_values[-1] == '.':
            formatted_values = formatted_values.replace('.','')
        return formatted_values
    return values
