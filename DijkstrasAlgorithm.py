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
    
    Last Practiced: 2022-03-14 07:42:15
'''
from calendar import c


def dijkstrasAlgorithm(start, edges):
    numberOfVerticies = len(edges)
    minDistanceFromStartToEachVertex = [float('inf')] * numberOfVerticies
    minDistanceFromStartToEachVertex[start] = 0
    visitedVerticies = set()

    while thereAreStillVerticiesToVisit(visitedVerticies, numberOfVerticies):
        currentVertexBeingVisited, distanceFromStartToCurrentVertexBeingVisited = getVertexWithMinDistanceFromStartThatHasntBeenVisitedYet(minDistanceFromStartToEachVertex, visitedVerticies)

        if distanceFromStartToCurrentVertexBeingVisited == float('inf'):
            break # The first discovered node where there is no path, algorithm is finished

        visitedVerticies.add(currentVertexBeingVisited)

        for edge in edges[currentVertexBeingVisited]:
            currentVertexNeighbor, distanceFromCurrentVertexToCurrentVertexNeighbor = edge

            if currentVertexNeighbor in visitedVerticies:
                continue

            newDistanceFromStartToCurrentVertexNeighbor = distanceFromStartToCurrentVertexBeingVisited + distanceFromCurrentVertexToCurrentVertexNeighbor
            currentDistanceFromStartToCurrentVertexNeighbor = minDistanceFromStartToEachVertex[currentVertexNeighbor]

            if newDistanceFromStartToCurrentVertexNeighbor < currentDistanceFromStartToCurrentVertexNeighbor:
                minDistanceFromStartToEachVertex[currentVertexNeighbor] = newDistanceFromStartToCurrentVertexNeighbor

    return list(map(lambda x: -1 if x == float('inf') else x, minDistanceFromStartToEachVertex))


def getVertexWithMinDistanceFromStartThatHasntBeenVisitedYet(minDistanceFromStartToEachVertex, visitedVerticies):
    currentVertex = -1
    currentDistanceFromStart = float('inf')

    for vertex, distance in enumerate(minDistanceFromStartToEachVertex):
        if vertex in visitedVerticies:
            continue
        if distance <= currentDistanceFromStart:
            currentVertex = vertex
            currentDistanceFromStart = distance
            
    return currentVertex, currentDistanceFromStart

def thereAreStillVerticiesToVisit(visitedVerticies, numberOfVerticies):
    return len(visitedVerticies) < numberOfVerticies

distances = [[[1,7]],[[2,6],[3,20],[4,3]],[[3,14]],[[4,2]],[],[]]
start = 0

print(dijkstrasAlgorithm(start, distances))