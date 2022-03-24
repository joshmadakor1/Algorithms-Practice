'''
    Dijkstra's Algorithm:
    Write a function that takes in an adjacency list and a starting index.
    Use Dijkstra's algorithm to find the shortest path to each vertex
    in the adjacency list and return the shortest distance to each node
    as an array (list). If a node is unreachable, it will have a distance
    of -1. Example:

    Input:  [[[1,7]],[[2,6],[3,20],[4,3]],[[3,14]],[[4,2]],[],[]]
    Output: [0, 7, 13, 27, 10, -1]

    Time:  
    Space: 
    
    Last Practiced: 2022-03-24 08:24:58
'''
def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)
    minDistanceFromStart = [float('inf')] * numberOfVertices
    minDistanceFromStart[start] = 0
    visited = set()

    while len(visited) < numberOfVertices:
        currentVertex, currentVertextDistanceFromStart = getNextNearestUnvisitedVertex(minDistanceFromStart, visited)
        if currentVertextDistanceFromStart == float('inf'): break # next nearest node is not reachable
        visited.add(currentVertex)
        for edge in edges[currentVertex]:
            neighborVertex, distanceFromCurrentVertextToNeighbor = edge
            if neighborVertex in visited: continue

            newDistanceFromStartToNeighbor = currentVertextDistanceFromStart + distanceFromCurrentVertextToNeighbor
            currentDistanceFromStartToNeighbor = minDistanceFromStart[neighborVertex]

            if newDistanceFromStartToNeighbor < currentDistanceFromStartToNeighbor:
                minDistanceFromStart[neighborVertex] = newDistanceFromStartToNeighbor
    return list(map(lambda x: -1 if x == float('inf') else x, minDistanceFromStart))

def getNextNearestUnvisitedVertex(minDistanceFromStart, visited):
    candidateVertex = None
    distanceFromStart = float('inf')
    
    for vertex, distance in enumerate(minDistanceFromStart):
        if vertex in visited: continue
        if distance <= distanceFromStart:
            candidateVertex = vertex
            distanceFromStart = distance

    return candidateVertex, distanceFromStart


distances = [[[1,7]],[[2,6],[3,20],[4,3]],[[3,14]],[[4,2]],[],[]]
start = 0

print(dijkstrasAlgorithm(start, distances))