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
    
    Last Practice: 2022-03-13 14:36:58
'''
def dijkstrasAlgorithm(start, edges):
    numberOfVerticies = len(edges)
    minDistances = [float('inf')] * numberOfVerticies
    minDistances[start] = 0
    visited = set()
    
    while thereAreStillUnvisitedVerticies(visited,numberOfVerticies):
        vertex, currentMinDistance = getVertexWithMinDistanceThatHasntBeenVisited(minDistances, visited)
        
        if currentMinDistance == float('inf'):
            break
            
        visited.add(vertex)
        
        for edge in edges[vertex]:
            destination, distanceToDestination = edge
            
            if destination in visited: continue
            
            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistances[destination]
            
            if newPathDistance < currentDestinationDistance:
                minDistances[destination] = newPathDistance
      # End of while
      
    return list(map(lambda x: -1 if x == float('inf') else x, minDistances))

def getVertexWithMinDistanceThatHasntBeenVisited(distances, visited):
    currentMinDistance = float('inf')
    vertex = -1
    
    for vertexId, distance in enumerate(distances):
        if vertexId in visited: continue
        if distance <= currentMinDistance:
            vertex = vertexId
            currentMinDistance = distance
            
    return vertex, currentMinDistance

def thereAreStillUnvisitedVerticies(visited,numberOfVerticies):
  return len(visited) < numberOfVerticies

distances = [[[1,7]],[[2,6],[3,20],[4,3]],[[3,14]],[[4,2]],[],[]]
start = 0

print(dijkstrasAlgorithm(start, distances))