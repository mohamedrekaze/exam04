# Given a string `s`, find the minimum number of cuts needed to partition it such that every resulting substring is a palindrome.
# A cut divides the string between two characters. With `c` cuts, the string is split into `c + 1` substrings. We want the minimum number of cuts `c` such that all parts are palindromes.
# Return this minimum number of cuts (an integer).
# Constraints:
# - An empty string or a string of length 1 is already a palindrome -> 0 cuts.
# - If the entire string is already a palindrome -> 0 cuts.
# - In the worst case (all characters are distinct), the result is len(s) - 1 cuts.


# def palindrome_partitioner(s: str) -> int:
#     if not s:
#         return 0
#     cuts = [i - 1 for i in range(len(s) + 1)]
#     for i in range(1, len(s) + 1):
#         for j in range(i):
#             if s[j:i] == s[j:i][::-1]:
#                 cuts[i] = min(cuts[i], cuts[j] + 1)
#     return cuts[-1]

def palindrome_partitioner(s: str) -> int:
    if s == s[::-1]:
        return 0
    return 1 + min(palindrome_partitioner(s[:i]) + palindrome_partitioner(s[i:]) for i in range(1, len(s)))

print(palindrome_partitioner("aab"),  "Expected: 1")
print(palindrome_partitioner("aba"),  "Expected: 0")
print(palindrome_partitioner("abc"),  "Expected: 2")
