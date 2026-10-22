# Write a function that determines a valid package installation order by resolving dependencies. Use topological sorting to ensure dependencies are installed before the packages that require them.

# The function should:
# - Take a dictionary where keys are package names and values are lists of dependencies
# - Return packages in installation order (dependencies first)
# - Return empty list if no valid order exists (circular dependencies)
# - Handle empty input and isolated dependency chains
# - Ignore references to packages not in the input dictionary

# Algorithm requirements:
# - Use topological sorting (e.g., Kahn's algorithm)
# - Process packages with no remaining dependencies first
# - Ensure deterministic output when multiple valid orders exist

# Edge cases to handle:
# - Empty input: return empty list
# - Packages with no dependencies: include in output first
# - Multiple independent chains: process all chains
# - Circular dependencies: return empty list
# - Non-existent dependencies: ignore missing packages
# - Self-dependencies: return empty list

# Notes:
# - For deterministic output, process packages alphabetically when choices exist
# - A package cannot be installed until all its dependencies are installed
# - If any circular dependency exists, no valid installation order is possible

import heapq

# Algorithm explanation
# 1. build indegree and reverse adjacency
#   1. iterate over every package and its dependency list
#   2. deduplicate the dependencies with set(deps)
#   3. skip dependencies not present in packages
#   4. increment indegree[pkg] once per distinct existing dependency
#   5. append pkg to dependents[dep] (edge dep -> pkg)
# 2. add all packages with indegree 0 to a heap, keeping alphabetical order
#    (the heap yields the lexicographically smallest valid order)
# 3. for every package popped, decrement each dependent's indegree
#    and push the dependent into the heap when its indegree reaches 0
# 4. detect a cycle (including self-dependency) if the result length
#    doesn't match the number of packages

import heapq

def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    indegree = {pkg: 0 for pkg in packages}
    dependents = {pkg: [] for pkg in packages}

    # loop over all packages and its dependencies
    # for each dependency for the package increment number of indegree
    # and for each dependency 

    for pkg, deps in packages.items():
        for dep in set(deps):
            if dep in packages:
                indegree[pkg] += 1
                dependents[dep].append(pkg)

    heap = [
        pkg for pkg in packages
        if indegree[pkg] == 0
    ]
    heapq.heapify(heap)

    result = []
    while heap:
        pkg = heapq.heappop(heap)
        result.append(pkg)
        for dependent in dependents[pkg]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                heapq.heappush(heap, dependent)

    if len(result) != len(packages):
        return []
    return result


print(package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []})  , 'Expected: ["driver", "database", "app"]')
# print(package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]})  , 'Expected: ["A", "B", "C"]')
# print(package_dependency_resolver({})  ,'Expected: []')
# print(package_dependency_resolver({"X": ["Y"], "Y": ["X"]})  , 'Expected: []')
# print(package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]})  , 'Expected: ["api", "web", "backend", "frontend"]')
