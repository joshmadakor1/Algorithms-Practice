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
    
    Last Practiced: 2022-03-22 05:51:35
'''
def dijkstrasAlgorithm(start, edges):
    numberOfEdges = len(edges)
    minDistanceFromStart = [float('inf')] * numberOfEdges
    minDistanceFromStart[start] = 0
    visited = set()
    
    while len(visited) < numberOfEdges:
        currentVertex, distanceFromStartToCurrentVertex = getNextClosestUnvisitedNode(minDistanceFromStart, visited)
        visited.add(currentVertex)
        
        if distanceFromStartToCurrentVertex == float('inf'): break # Closest node is unreachable. Finish algorithm
        
        for edge in edges[currentVertex]:
            currentVertextNeighbor, distanceFromCurrentVertexToNeighbor = edge
            if currentVertextNeighbor in visited: continue
            
            newDistanceFromStartToNeighbor = distanceFromStartToCurrentVertex + distanceFromCurrentVertexToNeighbor
            currentDistanceFromStartToNeighbor = minDistanceFromStart[currentVertextNeighbor]
            
            if newDistanceFromStartToNeighbor < currentDistanceFromStartToNeighbor:
                minDistanceFromStart[currentVertextNeighbor] = newDistanceFromStartToNeighbor
                
    return list(map(lambda x: -1 if x == float('inf') else x, minDistanceFromStart))

def getNextClosestUnvisitedNode(minDistanceFromStart, visited):
    candidateVertex = None
    candidateDistance = float('inf')
    
    for vertex, distance in enumerate(minDistanceFromStart):
        if vertex in visited: continue
        if distance <= candidateDistance:
            candidateVertex = vertex
            candidateDistanxe = distance
            
    return candidateVertex, candidateDistance


distances = [[[1,7]],[[2,6],[3,20],[4,3]],[[3,14]],[[4,2]],[],[]]
start = 0

print(dijkstrasAlgorithm(start, distances))