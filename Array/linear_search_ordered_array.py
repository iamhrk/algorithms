def linear_search(array, search_value):
    for index, element in enumerate(array):
        if element == search_value:
            return index
        elif element > search_value:
            break

    return None


print(linear_search([3,5,18,22],22))
