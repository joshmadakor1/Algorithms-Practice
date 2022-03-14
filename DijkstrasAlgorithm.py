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
    
    Last Practiced: 2022-03-14 11:39:18
'''
def dijkstrasAlgorithm(startVertex, edges):
    numberOfVerticies = len(edges)
    minDistanceFromStartToOtherVerticies = [float('inf')] * numberOfVerticies
    minDistanceFromStartToOtherVerticies[startVertex] = 0
    visitedVerticies = set()

    while thereAreStillOtherVerticiesToVisit(numberOfVerticies, len(visitedVerticies)):
        currentVertex, currentVertexDistanceFromStart = getVertexWithSmallestDistanceFromStartThatHasntBeenVisitedYet(minDistanceFromStartToOtherVerticies,visitedVerticies)
        if currentVertexDistanceFromStart == float('inf'):
            break # Next nearest node cannot be reached, finish.
        visitedVerticies.add(currentVertex)

        for edge in edges[currentVertex]:
            currentVertexNeighbor, distanceFromCurrentVertexToCurrentVertexNeighbor = edge
            if currentVertexNeighbor in visitedVerticies: continue

            distanceFromStartToCurrentVertexNeighbor = currentVertexDistanceFromStart + distanceFromCurrentVertexToCurrentVertexNeighbor
            currentDistanceFromStartToCurrentVertexNeighbor = minDistanceFromStartToOtherVerticies[currentVertexNeighbor]

            if distanceFromStartToCurrentVertexNeighbor < currentDistanceFromStartToCurrentVertexNeighbor:
                minDistanceFromStartToOtherVerticies[currentVertexNeighbor] = distanceFromStartToCurrentVertexNeighbor

    return list(map(lambda x: -1 if x == float('inf') else x, minDistanceFromStartToOtherVerticies))

def getVertexWithSmallestDistanceFromStartThatHasntBeenVisitedYet(minDistanceFromStartToOtherVerticies, visitedVerticies):
    nearestVertex = -1
    nearestVertexDistance = float('inf')
    for vertex, distance in enumerate(minDistanceFromStartToOtherVerticies):
        if vertex in visitedVerticies: continue
        if distance <= nearestVertexDistance:
            nearestVertex = vertex
            nearestVertexDistance = distance
    return nearestVertex, nearestVertexDistance

def thereAreStillOtherVerticiesToVisit(numberOfVerticiesTotal, numberOfVerticiesVisited):
    return numberOfVerticiesVisited < numberOfVerticiesTotal

distances = [[[1,7]],[[2,6],[3,20],[4,3]],[[3,14]],[[4,2]],[],[]]
start = 0

print(dijkstrasAlgorithm(start, distances))