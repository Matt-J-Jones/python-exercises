EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(time_elapsed):
    """Calculate the bake time remaining.

    :param time_elapsed: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - time_elapsed

def preparation_time_in_minutes(layers):
    """Calculate the preparation time.

    :param layers: int - the number of layers.
    :return: int - preparation time, derived from 'PREPARATION_TIME';

    Function that takes the number of layers and returns a preparation time based
    on the 'PREPARATION_TIME', assuming 2 minutes per layer
    """
    return PREPARATION_TIME * layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the overall elapsed time.

    :param number_of_layers: int - the number of layers.
    :param elapsed_bake_time: int - the time elapsed.

    :return: int - preparation time

    Function that takes the number of layers and the time elapsed, returns total time elapsed
    by first working out total preperation time, and adding time alreay elapsed.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
