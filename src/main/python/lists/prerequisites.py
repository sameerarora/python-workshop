def ordering(prereqs):
    result = []
    visited = set()
    for p in prereqs:
        if p[1] in visited and p[0] not in visited:
            result += [p[0]]
            visited.add(p[0])
        if p[0] in visited and p[1] not in visited:
            i = result.index(p[0])
            result.insert(i, p[1])
            visited.add(p[1])
        if p[0] not in visited and p[1] not in visited:
            result += [p[1], p[0]]
            visited.add(p[0])
            visited.add(p[1])
        if p[0] in visited and p[1] in visited:
            if result.index(p[1]) > result.index(p[0]):
                result.remove(p[1])
                result.insert(result.index(p[0]), p[1])

    return result


print(ordering([[1, 0], [0,1], [0, 2], [0, 5], [3, 2], [3, 1], [5, 6], [2, 6]]))
