'''
    Cycle In Graph:
    Given an adjacency list (2d array), write a function that returns
    whether or not a cycle can be found in the graph

    Time:  O(V+E), where V = Verticies, and E = Edges
    Space: O(2V) -> O(V), where V = Verticies in the auxiliary data structures

    Last Practice: 2022-03-15 08:31:02
'''
def cycleInGraph(edges):
    vertexHasBeenVisited = [False] * len(edges)
    vertexIsInStack = [False] * len(edges)
    for vertex in range(len(edges)):
        if vertexHasBeenVisited[vertex]: continue
        if vertexIsInCycle(vertex, edges, vertexHasBeenVisited, vertexIsInStack): return True
    return False

def vertexIsInCycle(vertex, edges, vertexHasBeenVisited, vertexIsInStack):
    vertexHasBeenVisited[vertex] = True
    vertexIsInStack[vertex] = True
    neighbors = edges[vertex]
    for neighbor in neighbors:
        if vertexHasBeenVisited[neighbor] and vertexIsInStack[neighbor]: return True
        if vertexIsInCycle(neighbor, edges, vertexHasBeenVisited, vertexIsInStack): return True
    vertexIsInStack[vertex] = False
    return False

edges = [ [1, 3], [2, 3, 4],[0],[],[2, 5],[]]

assert cycleInGraph(edges) == True, "Error. Expected output: True"