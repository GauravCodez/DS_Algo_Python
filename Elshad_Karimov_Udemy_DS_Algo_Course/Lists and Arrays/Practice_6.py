# Program to find whether the elements in the list are repeated or not
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 18, 11, 1])


def check_if_repeated(list1):
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            if arr[i] == arr[j]:
                return True
    return False


print("Do duplicates exist in the provided array : ", check_if_repeated(arr))


