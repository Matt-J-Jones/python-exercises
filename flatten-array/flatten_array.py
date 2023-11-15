def flatten(iterable):
    return_array = []
    for item in iterable:
        if item is not None:
            if isinstance(item, int):
                return_array.append(item)
            if isinstance(item, list):
                sub_lists(return_array, item)
    return return_array

def sub_lists(return_array, list_to_flatten):
    for item in list_to_flatten:
        if isinstance(item, int):
            return_array.append(item)
        elif isinstance(item, list):
            sub_lists(return_array, item)
