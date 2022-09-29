# Program for practice problem on permutation
# Find whether one string is the permutation of another

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False

    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False


list_a = ['a', 'b', 'c']
list_b = ['a', 'b', 'c']
print("Are both the lists permutation of each other : ", permutation(list_a, list_b))
