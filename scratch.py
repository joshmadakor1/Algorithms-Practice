def dijkstrasAlgorithm(start, edges):
    numberOfVerticies = len(edges)
    minDistances = [float('inf')] * numberOfVerticies
    minDistances[start] = 0
    visited = set()

    while thereAreStillUnvisitedVerticies(numberOfVerticies, visited):
        vertex, distance = getVertextWithSmallestDistanceThatHasntBeenVisitedYet(minDistances, visited)

        if distance == float('inf'): break

        visited.add(vertex)

        for edge in edges[vertex]:
            destinationVertex, destinationDistance = edge

            newDistanceoDestinationVertex = distance + destinationDistance
            currentDistanceToDestinationVertex = minDistances[destinationVertex]

            if newDistanceoDestinationVertex < currentDistanceToDestinationVertex:
                minDistances[destinationVertex] = newDistanceoDestinationVertex
        # End of While
    return list(map(lambda x: -1 if x == float('inf') else x, minDistances))

def getVertextWithSmallestDistanceThatHasntBeenVisitedYet(minDistances, visited):
    currentMinDistance = float('inf')
    currentVertex = -1

    for vertex, distance in enumerate(minDistances):
        if vertex in visited: continue
        if distance <= currentMinDistance:
            currentMinDistance = distance
            currentVertex = vertex
    return currentVertex, currentMinDistance

def thereAreStillUnvisitedVerticies(numberOfVerticies, visited):
    return len(visited) < numberOfVerticies

distances = [[[1,7]],[[2,6],[3,20],[4,3]],[[3,14]],[[4,2]],[],[]]
start = 0

print(dijkstrasAlgorithm(start, distances))