def dijkstrasAlgorithm(start, edges):
	numberOfEdges = len(edges)
	minDistanceFromStartToEdges = [float('inf')] * numberOfEdges
	minDistanceFromStartToEdges[start] = 0
	visited = set()
	
	while len(visited) < numberOfEdges:
		currentVertex, distanceFromStartToCurrentVertex = getNearestUnvisitedVertex(minDistanceFromStartToEdges, visited)
		if distanceFromStartToCurrentVertex == float('inf'): break # next nearest vertex is not reachable
		visited.add(currentVertex)
		for edge in edges[currentVertex]:
			neighborVertex, distanceFromCurrentVertexToNeighborVertex = edge
			if neighborVertex in visited: continue
			
			newDistanceFromStartToNeighborVertex = distanceFromStartToCurrentVertex + distanceFromCurrentVertexToNeighborVertex
			currentDistanceFromStartToNeighborVertex = minDistanceFromStartToEdges[neighborVertex]
			
			if newDistanceFromStartToNeighborVertex < currentDistanceFromStartToNeighborVertex:
				minDistanceFromStartToEdges[neighborVertex] = newDistanceFromStartToNeighborVertex
	
	return list(map(lambda x: -1 if x == float('inf') else x, minDistanceFromStartToEdges))
		
def getNearestUnvisitedVertex(minDistanceFromStartToEdges, visited):
	candidateVertex = None
	candidateVertexDistanceFromStart = float('inf')
	
	for vertex, distance in enumerate(minDistanceFromStartToEdges):
		if vertex in visited: continue
		if distance <= candidateVertexDistanceFromStart:
			candidateVertex = vertex
			candidateVertexDistanceFromStart = distance
			
	return [candidateVertexDistanceFromStart, distance]

distances = [[[1,7]],[[2,6],[3,20],[4,3]],[[3,14]],[[4,2]],[],[]]
start = 0

print(dijkstrasAlgorithm(start, distances))