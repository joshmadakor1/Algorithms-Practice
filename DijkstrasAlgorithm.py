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
    
    Last Practiced: 2022-03-21 07:05:24
'''
def dijkstrasAlgorithm(start, edges):
    numberOfEdges = len(edges)
    minDistancesFromStart = [float('inf')] * numberOfEdges
    minDistancesFromStart[start] = 0
    visited = set()
    while len(visited) < numberOfEdges:
        currentVertex, distanceFromStartToCurrentVertex = getNearestUnvisitedVertex(minDistancesFromStart, visited)
        if distanceFromStartToCurrentVertex == float('inf'): break # next nearest vertex is unreachable
        visited.add(currentVertex)
        
        for edge in edges[currentVertex]:
            currentNeighbor, distanceFromCurrentVertexToNeighbor = edge
            if currentNeighbor in visited: continue
            
            newDistanceFromStartToCurrentNeighbor = distanceFromStartToCurrentVertex + distanceFromCurrentVertexToNeighbor
            currentDistanceFromStartToCurrentNeighbor = minDistancesFromStart[currentNeighbor]
            
            if newDistanceFromStartToCurrentNeighbor < currentDistanceFromStartToCurrentNeighbor:
                minDistancesFromStart[currentNeighbor] = newDistanceFromStartToCurrentNeighbor
    return list(map(lambda x: -1 if x == float('inf') else x, minDistancesFromStart))
def getNearestUnvisitedVertex(minDistancesFromStart, visited):
    candidateVertex = None
    candidateDistance = float('inf')
    for vertex, distance in enumerate(minDistancesFromStart):
        if vertex in visited: continue
        if distance <= candidateDistance:
            candidateVertex = vertex
            candidateDistance = distance
            
    return [candidateVertex, candidateDistance]


distances = [[[1,7]],[[2,6],[3,20],[4,3]],[[3,14]],[[4,2]],[],[]]
start = 0

print(dijkstrasAlgorithm(start, distances))