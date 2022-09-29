# Find the maximum product of 2 integers in the given array/list

import numpy as np
data_1 = np.array([1, 2, 3, 4, 5, 100, 6, 7, 8, 9, 10, 11, 7, 3, 2])


def find_max_value(data):
    pro = 1
    max_pro = 1
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            pro = data[i]*data[j]
            if pro > max_pro and data[i] != data[j]:
                max_pro = pro
                pro = 1
                values = [max_pro, data[i], data[j]]
            else:
                pro = 1
    return values


value_list = find_max_value(data_1)
print("The maximum product is : ", value_list[0])
print("Maximum value pair : ", value_list[1], ",", value_list[2])
