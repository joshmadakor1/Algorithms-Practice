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
    
    Last Practiced: 2022-03-14 07:56:51 
'''
from calendar import c


def dijkstrasAlgorithm(startIndex, edges):
    numberOfVerticies = len(edges)
    minDistanceFromStartToAllVerticies = [float('inf')] * numberOfVerticies
    minDistanceFromStartToAllVerticies[startIndex] = 0
    visitedVerticies = set()

    while thereAreStillVerticiesToVisit(numberOfVerticies, len(visitedVerticies)):
        currentVertexBeingVisited, distanceFromStartToCurrentVertexBeingVisited = getVertexWithMinDistanceFromStartThatHasntBeenVisitedYet(minDistanceFromStartToAllVerticies, visitedVerticies)
        if distanceFromStartToCurrentVertexBeingVisited == float('inf'):
            break # First time to discover unreachable node; algorithm finished
        visitedVerticies.add(currentVertexBeingVisited)

        for edge in edges[currentVertexBeingVisited]:
            currentVertexNeighbor, distanceFromCurrentVertexToCurrentVertexNeighbor = edge
            
            if currentVertexNeighbor is visitedVerticies:
                continue

            newDistanceFromStartToCurrentVertexNeighbor = distanceFromStartToCurrentVertexBeingVisited + distanceFromCurrentVertexToCurrentVertexNeighbor
            currentDistanceFromStartToCurrentVertexNeighbor = minDistanceFromStartToAllVerticies[currentVertexNeighbor]

            if newDistanceFromStartToCurrentVertexNeighbor < currentDistanceFromStartToCurrentVertexNeighbor:
                minDistanceFromStartToAllVerticies[currentVertexNeighbor] = newDistanceFromStartToCurrentVertexNeighbor

    return list(map(lambda x: -1 if x == float('inf') else x, minDistanceFromStartToAllVerticies))


def thereAreStillVerticiesToVisit(numberOfVerticies, numberOfVisitedVerticies):
    return numberOfVisitedVerticies < numberOfVerticies

def getVertexWithMinDistanceFromStartThatHasntBeenVisitedYet(minDistanceFromStartToAllVerticies, visitedVerticies):
    currentVertex = -1
    currentDistanceFromStart = float('inf')

    for vertex, distance in enumerate(minDistanceFromStartToAllVerticies):
        if vertex in visitedVerticies:
            continue
        if distance <= currentDistanceFromStart:
            currentVertex = vertex
            currentDistanceFromStart = distance

    return currentVertex, currentDistanceFromStart
distances = [[[1,7]],[[2,6],[3,20],[4,3]],[[3,14]],[[4,2]],[],[]]
start = 0

print(dijkstrasAlgorithm(start, distances))