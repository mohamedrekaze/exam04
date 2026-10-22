# Write a function that finds the intersection of multiple sorted lists.
# Return a new list containing elements that appear in ALL input lists, in sorted order.
# The function should:
# - Return elements that appear in ALL lists
# - Result should be sorted in ascending order
# - Remove duplicates from the result
# - Handle empty input or empty lists gracefully
# - If any list is empty, the intersection is empty

def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not len(lists):
        return []
    n_list = [set(it) for it in lists]
    common = set.intersection(*n_list)
    return sorted(list(common))

print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]),  " Expected: [2, 3]")
print(list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]),  " Expected: [4]")
print(list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]),  " Expected: [1, 2, 3]")
print(list_intersection_finder([[1, 2, 3], [4, 5, 6]]),  " Expected: []")
print(list_intersection_finder([]),  " Expected: []")
print(list_intersection_finder([[1, 2, 3], []]),  " Expected: []")
print(list_intersection_finder([[5]]),  " Expected: [5]")
