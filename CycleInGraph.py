'''
    Cycle In Graph:
    Given an adjacency list (2d array), write a function that returns
    whether or not a cycle can be found in the graph

    Time:  O(V+E), where V = Verticies, and E = Edges
    Space: O(2V) -> O(V), where V = Verticies in the auxiliary data structures

    Last Practice: 2022-03-22 06:18:54
'''
def cycleInGraph(edges):
    visited = [False] * len(edges)
    inStack = [False] * len(edges)
    for vertex in range(len(edges)):
        if visited[vertex]: continue
        if isInCycle(vertex, edges, visited, inStack):
            return True
    return False

def isInCycle(vertex, edges, visited, inStack):
    visited[vertex] = True
    inStack[vertex] = True
    neighbors = edges[vertex]
    for neighbor in neighbors:
        if visited[neighbor] and inStack[neighbor]:
            return True # Cycle was found
        if isInCycle(neighbor, edges, visited, inStack):
            return True
    inStack[vertex] = False
    return False




edges = [ [1, 3], [2, 3, 4],[0],[],[2, 5],[]]

assert cycleInGraph(edges) == True, "Error. Expected output: True"