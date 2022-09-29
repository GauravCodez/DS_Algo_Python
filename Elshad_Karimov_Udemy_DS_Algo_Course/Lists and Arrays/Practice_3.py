# Program : Write a program to find all pairs of integers whose sum is equal to the given number
# Example : [2, 6, 3, 9, 11]  ==>  Solution should be [6,3]
# Pairs should be distinct


def find_pairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target and nums[i] != nums[j]:
                print(nums[i], ",", nums[j])


list1 = [1, 2, 3, 2, 3, 4, 5, 6]
find_pairs(list1, 6)
