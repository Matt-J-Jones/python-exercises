def append(list1, list2):
    return list1 + list2

def concat(lists):
    return_list = []
    for list in lists:
        return_list  = return_list + list
    return return_list

def filter(function, list):
    return_list = []
    for item in list:
        if function(item):
            return_list.append(item)
    return return_list

def length(list):
    return len(list)

def map(function, list):
    return_list = []
    for item in list:
        return_list.append(function(item))
    return return_list

def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial

def foldr(function, list, initial):
    list.reverse()
    for item in list:
        initial = function(initial, item)
    return initial

def reverse(list):
    return_list = []
    if len(list) > 0 :
        for index, item in enumerate(list):
            return_list.append(list[len(list)-1-index])
    return return_list
