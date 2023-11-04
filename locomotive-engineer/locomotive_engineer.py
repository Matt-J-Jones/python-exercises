"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    wagons = []
    for wagon in args:
        wagons.append(wagon)
    return wagons


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    input_data=([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15]), 
    move 2,5 to the end, input 3,17,6,15 after 1 in original list.
    output_data=[1, 3, 17, 6, 15, 7, 4, 12, 6, 3, 13, 2, 5]
    """
    move_to_end_1, move_to_end_2, first_item, *remaining = each_wagons_id
    fixed_list = *[first_item], *missing_wagons, *remaining, *[move_to_end_1, move_to_end_2]
    return get_list_of_wagons(*fixed_list)

def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    return {**route, "stops" : list(kwargs.values())}

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    extended_information = {**route, **more_route_information}
    return extended_information


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    # [*all_trains] = zip(*wagons_rows)
    # fix_depot_information = []
    # return fix_depot_information
    mixed_rows = []
    for row in wagons_rows:
        [*temp_row] = zip(*row)
        mixed_rows.append(temp_row)
    ordered_rows = []
    row_count = [0,1,2]
    for count in row_count:
        ordered_rows.append([
            (mixed_rows[0][0][count], mixed_rows[0][1][0]),
            (mixed_rows[1][0][count], mixed_rows[1][1][0]),
            (mixed_rows[2][0][count], mixed_rows[2][1][0])])
    return ordered_rows