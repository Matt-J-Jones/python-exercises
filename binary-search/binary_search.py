def find(search_list, value):
    if value not in search_list:
        raise ValueError("value not in array")

    search_list.sort()
    left, right = 0, len(search_list)-1

    while left <= right:

        middle = (left + right) // 2
    
        if search_list[middle] == value:
            return middle
        
        if search_list[middle] < value:
            left = middle + 1
        elif search_list[middle] > value:
            right = middle - 1
