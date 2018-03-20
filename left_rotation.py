"""Left rotation"""

array = [1,2,3,4,5]
def left_rotation(array, no_of_cycles):
    return array[no_of_cycles:] + array[:no_of_cycles]

print(left_rotation(array, 4))