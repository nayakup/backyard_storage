def linear_search(array, value):
    """
    returns the index position of the value from array.
    If value is not found, return None
    """
    array_length = len(array)
    for i in range(0, array_length):
        if(value == array[i]):
            return i
    return None


my_array = [1, 3, 5, 7, 9]
print(linear_search(my_array, 8))
print(linear_search(my_array, 7))
