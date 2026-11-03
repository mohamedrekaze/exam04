# Write a function that finds the maximum element in each sliding window of size k in an array. Return a list of maximums for each window position.
# The function should:
# - Slide a window of size k through the array
# - Find the maximum element in each window position
# - Return a list of maximum values
# - Handle edge cases (empty array, k <= 0, k > array length)
# - Return empty list for invalid inputs

def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if not len(nums) or not k:
        return []
    res = []
    for x in range(len(nums)):
        sub = nums[x:x+k]
        if len(sub) < k:
            break
        res.append(max(sub))
    return res

print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7])
print(sliding_window_maximum([1, 2, 3, 4, 5], 2) == [2, 3, 4, 5])
print(sliding_window_maximum([5, 4, 3, 2, 1], 1) == [5, 4, 3, 2, 1])
print(sliding_window_maximum([1, 2, 3], 3) == [3])
print(sliding_window_maximum([1, 2, 3], 4) == [])
print(sliding_window_maximum([], 2) == [])
print(sliding_window_maximum([1, 2, 3], 0) == [])
