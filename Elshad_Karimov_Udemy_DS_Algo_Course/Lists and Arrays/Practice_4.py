# Test the elements whether they exist in the array

import numpy as np

my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])


def find_number(my_array_1, number_1):
    for i in range(len(my_array_1)):
        if my_array_1[i] == number_1:
            print("Matching element ", number_1, " exists inside the entered array ")
            return True
    return False


print("Target exists inside the array entered : ", find_number(my_array, 100))
