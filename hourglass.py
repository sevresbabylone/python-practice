"""2d Array: Maximum Hourglass value"""

def get_largest_hourglass(square, x_length, y_length):
    hourglass_array = []
    """Returns largest of all 3 x 3 hourglasses within a larger x_length by y_length 2d array"""
    for column_index in range(x_length - 2):
        # Loop through all columns except for last 2
        for row_index in range(y_length - 2):
            # Loop through all rows except for last 2
            hourglass = []
            # Get all 3 rows of an 3 x 3 square
            for mini_row_index in range(3):
                hourglass_row = arr[row_index + mini_row_index][column_index:column_index+3]
                hourglass.extend(hourglass_row)
            # Make it an hourglass    
            hourglass.pop(5)
            hourglass.pop(3)
            hourglass_array.append(hourglass)
    return max([sum(hourglass) for hourglass in hourglass_array])

arr = [[1, 1,  1,  0,  0, 0],
       [0, 1,  0,  0,  0, 0],
       [1, 1,  1,  0,  0, 0],
       [0, 9,  2, -4, -4, 0],
       [0, 0,  0, -2,  0, 0],
       [0, 0, -1, -2, -4, 0]]

print(get_largest_hourglass(arr, len(arr[0]), len(arr)))