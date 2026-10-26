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

def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    indegree = {pkg: 0 for pkg in packages}
    dependents = {pkg: [] for pkg in packages}
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
        for dep in dependents[pkg]:
            indegree[dep] -= 1
            if indegree[dep] == 0:
                heapq.heappush(heap, dep)
    if len(result) != len(packages):
        return []
    return result

print(package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []})  , 'Expected: ["driver", "database", "app"]')
print(package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]})  , 'Expected: ["A", "B", "C"]')
print(package_dependency_resolver({})  ,'Expected: []')
print(package_dependency_resolver({"X": ["Y"], "Y": ["X"]})  , 'Expected: []')
print(package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]})  , 'Expected: ["api", "web", "backend", "frontend"]')
