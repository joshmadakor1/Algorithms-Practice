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
    
    Last Practiced: 2022-03-27 05:39:11
'''
def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)
    minDistancesFromStart = [float('inf')] * numberOfVertices
    minDistancesFromStart[start] = 0
    visited = set()
    
    while len(visited) < numberOfVertices:
        currentVertex, distanceFromStartToCurrentVertex = getNextClosestUnvisitedVertex(minDistancesFromStart, visited)
        if distanceFromStartToCurrentVertex == float('inf'): break # next closest is unreachable; algo finished
        visited.add(currentVertex)
        for edge in edges[currentVertex]:
            neighborVertex, neighborVertexDistanceFromCurrentVertex = edge
            if neighborVertex in visited: continue
            newDistanceFromStartToNeighborVertex = distanceFromStartToCurrentVertex + neighborVertexDistanceFromCurrentVertex
            currentDistanceFromStartToNeighborVertex = minDistancesFromStart[neighborVertex]
            if newDistanceFromStartToNeighborVertex < currentDistanceFromStartToNeighborVertex:
                minDistancesFromStart[neighborVertex] = newDistanceFromStartToNeighborVertex
                
    return list(map(lambda x: -1 if x == float('inf') else x, minDistancesFromStart))
        
def getNextClosestUnvisitedVertex(minDistancesFromStart, visited):
    candidateVertex = None
    candidateDistance = float('inf')
    for vertex, distance in enumerate(minDistancesFromStart):
        if vertex in visited: continue
        if distance <= candidateDistance:
            candidateVertex = vertex
            candidateDistance = distance
    return candidateVertex, candidateDistance


distances = [[[1,7]],[[2,6],[3,20],[4,3]],[[3,14]],[[4,2]],[],[]]
start = 0

print(dijkstrasAlgorithm(start, distances))