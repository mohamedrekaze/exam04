# Write a function that maps a constellation of stars onto a grid and returns the visual representation as a list of strings.
# The function should:
# - Take a list of star coordinates as tuples (row, col) and grid size as integer
# - Return a list of strings representing the grid
# - Stars are represented by '*' and empty spaces by '.'
# - Grid coordinates start from (0, 0) at top-left
# - Ignore coordinates outside the grid boundaries
# - Handle duplicate coordinates (star appears only once)

# def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
#     sphere = [["." for x in range(dim)] for x in range(dim)]
#     for star in stars:
#         x, y = star
#         if x > dim or y > dim:
#             continue
#         sphere[x][y] = "*"
#     return_list = ["".join(it) for it in sphere]
#     return return_list

def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    stars = set(stars)
    return [
        "".join("*" if (row, col) in stars else "." for col in range(dim))
        for row in range(dim)
    ]

print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3),   "Expected: ['*..', '.*.', '..*']")
print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3), "Expected: ['.*.', '***', '.*.']")
print(constellation_mapper([], 2),  "Expected: ['..', '..']")
print(constellation_mapper([(0, 0), (0, 0), (1, 1)], 2), "Expected: ['*.', '.*']")
print(constellation_mapper([(0, 0), (5, 5)], 3), "Expected: ['*..', '...', '...']")
print(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3), "Expected: ['...', '***', '...']")
