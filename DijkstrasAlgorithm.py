# AlgoExpert's implementation
def dijkstrasAlgorithm(start, edges):
    numberOfVerticies = len(edges)
    minDistances = [float("inf")] * numberOfVerticies
    minDistances[start] = 0
    visited = set()

    while len(visited) < numberOfVerticies:
        vertex, currentMinDistance = getVertexWithMinDistance(minDistances, visited)
        if currentMinDistance == float("inf"):
            break
        visited.add(vertex)

        for edge in edges[vertex]:
            destination, distanceToDestination = edge
        
            if destination in visited:
                continue
            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistances[destination]
            if newPathDistance < currentDestinationDistance:
                minDistances[destination] = newPathDistance
    
    return list(map(lambda x: -1 if x == float("inf") else x, minDistances))

def getVertexWithMinDistance(distances, visited):
    currentMinDistance = float("inf")
    vertex = -1

    for vertexIdx, distance in enumerate(distances):
        if vertexIdx in visited:
            continue
        if distance <= currentMinDistance:
            vertex = vertexIdx
            currentMinDistance = distance
    
    return vertex, currentMinDistance

distances = [
  [
    [1, 7]
  ],
  [
    [2, 6],
    [3, 20],
    [4, 3]
  ],
  [
    [3, 14]
  ],
  [
    [4, 2]
  ],
  [],
  []
]

start = 0

dijkstrasAlgorithm(start, distances)