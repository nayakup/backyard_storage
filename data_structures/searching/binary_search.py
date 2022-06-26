def binary_search(array, value):
    """
    (input array should be sorted in ascending order)
    returns the index position of the value from array.
    If value is not found, return None

    Complexity: O(log n)
    """

    first = 0
    last = len(array)-1
    while (first <= last):
        mid = (first + last)//2
        if(value == array[mid]):
            return mid
        # If value is greater than the mid start from mid+1 to last
        elif(value > array[mid]):
            first = mid+1
        # If value is less than the mid start from first to mid-1
        else:
            last = mid-1
    return None


my_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
print(binary_search(my_array, 8))
print(binary_search(my_array, 19))

fruits = ['Apple', 'Banana', 'Grapes', 'Jackfruit', 'Kiwi',
          'Lemon', 'Mango', 'Orange', 'Pears', 'Rambutan']

print(binary_search(fruits, 'Mango'))
