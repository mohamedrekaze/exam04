# Write a Python function that takes two lists (arrays) as parameters and determines
# if the second list is a rotation of the first list (left or right).
# A rotation means that the elements are shifted circularly. For example,
# shifting [1, 2, 3] to the right by one position results in [3, 1, 2].
# The function must return True if arr2 is a rotation of arr1, and False otherwise.
# If the arrays have different lengths, they cannot be rotations of each other.
# Two empty arrays are considered rotations of each other.

# Moulinette Rules & Constraints
# Forbidden built-ins / modules: collections.deque.rotate(). Use only permitted built-in functions to avoid getting 0 on exam day.

def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) == 0 and len(arr2) == 0:
        return True
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr2)):
        if arr1 == arr2[i:] + arr2[:i]:
            return True
    return False

print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]) == True)
print(array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]) == True)
print(array_rotation_detector([1, 2, 3], [3, 2, 1]) == False)
print(array_rotation_detector([1, 2], [1, 2, 3]) == False)
print(array_rotation_detector([], []) == True)
