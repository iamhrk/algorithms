def binary_search(array, search_value):
    upper_bound = len(array) - 1
    lower_bound = 0

    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound) // 2
        value_at_midpoint = array[midpoint]
        
        if search_value == value_at_midpoint:
            return midpoint
        elif search_value < value_at_midpoint:
            upper_bound = middlepoint - 1
        elif search_value > value_at_midpoint:
            lower_bound = midpoint + 1
    return None
                


print(binary_search([2,4,8,9,10,12,15],15))
