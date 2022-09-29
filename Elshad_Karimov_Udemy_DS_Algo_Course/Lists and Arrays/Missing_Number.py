# One of the most frequently asked question is
# Finding the missing number in the array/list in a program of data from 1 to 100 ?


def missing_no(lis1, total_elements1):
    total_sum_1 = total_elements1*(total_elements1+1)/2
    sum_of_list = sum(lis1)
    missing_value = total_sum_1 - sum_of_list
    return missing_value


lis = [1, 2, 3, 4, 5, 6, 7, 9, 10]
total_elements = 10
print("Missing element in the sequence of list is ", str(missing_no(lis, total_elements)))
