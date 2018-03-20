"""2d Array: Maximum Hourglass value"""

def get_all_hourglasses(square, x_length, y_length):
    hourglass_array = []
    # excluded_indexes = [3, 5]
    """Returns an array of all 3 x 3 hourglasses within a larger x_length by y_length 2d array"""
    for column_index in range(x_length - 2):
        # Loop through all columns except for last 2
        for row_index in range(y_length - 2):
            # Loop through all rows except for last 2
            hourglass = []
            for mini_row_index in range(3):
                hourglass_row = arr[row_index + mini_row_index][column_index:column_index+3]
                hourglass.extend(hourglass_row)

            hourglass.pop(5)
            hourglass.pop(3)
            hourglass_array.append(hourglass)
    return hourglass_array    

def get_largest_hourglass(hourglass_array):
    """Returns largest hourglass value in array of hourglasses"""
    sums = [sum(hourglass) for hourglass in hourglass_array]
    return max(sums)

arr = [[1, 1,  1,  0,  0, 0],
       [0, 1,  0,  0,  0, 0],
       [1, 1,  1,  0,  0, 0],
       [0, 9,  2, -4, -4, 0],
       [0, 0,  0, -2,  0, 0],
       [0, 0, -1, -2, -4, 0]]

new_array = get_all_hourglasses(arr, len(arr[0]), len(arr))
print(get_largest_hourglass(new_array))