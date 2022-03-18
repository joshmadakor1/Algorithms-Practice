from math import dist


def dijkstrasAlgorithm(startVertex, edges):
    numberOfVerticies = len(edges)
    minDistanceFromStartToOtherVerticies = [float('inf')] * numberOfVerticies
    minDistanceFromStartToOtherVerticies[startVertex] = 0
    visitedVerticies = set()

    while thereAreStillOtherVerticiesToVisit(numberOfVerticies, len(visitedVerticies)):
        currentVertex, currentVertexDistanceFromStart = getVertexWithSmallestDistanceFromStartThatHasntBeenVisitedYet(minDistanceFromStartToOtherVerticies, visitedVerticies)
        if currentVertexDistanceFromStart == float('inf'):
            break # Next nearest node is unreachable
        visitedVerticies.add(currentVertex)

        for edge in edges[currentVertex]:
            currentVertexNeighbor, distanceFromCurrentVertextToCurrentVertexNeighbor = edge
            if currentVertexNeighbor in visitedVerticies: continue

            newDistanceFromStartToCurrentVertexNeighbor = currentVertexDistanceFromStart + distanceFromCurrentVertextToCurrentVertexNeighbor
            currentDistanceFromStartToCurrentVertexNeighbor = minDistanceFromStartToOtherVerticies[currentVertexNeighbor]
            if newDistanceFromStartToCurrentVertexNeighbor < currentDistanceFromStartToCurrentVertexNeighbor:
                minDistanceFromStartToOtherVerticies[currentVertexNeighbor] = newDistanceFromStartToCurrentVertexNeighbor
    return list(map(lambda x: -1 if x == float('inf') else x, minDistanceFromStartToOtherVerticies))

def thereAreStillOtherVerticiesToVisit(numberOfTotalVerticies, numberOfVisitedVerticies):
    return numberOfVisitedVerticies < numberOfTotalVerticies

def getVertexWithSmallestDistanceFromStartThatHasntBeenVisitedYet(minDistanceFromStartToOtherVerticies, visited):
    minDistance = float('inf')
    vertex = -1
    for candidateVertex, distance in enumerate(minDistanceFromStartToOtherVerticies):
        if candidateVertex in visited: continue
        if distance <= minDistance:
            vertex = candidateVertex
            minDistance = distance
    return [vertex, minDistance]