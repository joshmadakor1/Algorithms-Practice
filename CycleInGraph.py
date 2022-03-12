'''
    Cycle In Graph:
    Given an adjacency list (2d array), write a function that returns
    whether or not a cycle can be found in the graph

    Time:  O(V+E), where V = Verticies, and E = Edges
    Space: O(2V) -> O(V), where V = Verticies in the auxiliary data structures

    Last Practice: 2022-03-12 15:33:33
'''
def cycleInGraph(edges):
    visited = [False] * len(edges) # Keeps track of visited nodes globally
    stack = [False] * len(edges) # Keeps track of nodes visited during cycle checks

    # Step through each node, skipping visited notes, and check for cycles
    for node in range(len(edges)):
        if visited[node]:
            continue
        inCycle = nodeInCycle(node, edges, visited, stack)
        if inCycle:
            return True

    return False

# Helper function to check if any given node is in a cycle
def nodeInCycle(node, edges, visited, stack):
    visited[node] = True
    stack[node] = True
    neighbors = edges[node]

    for neighbor in neighbors:
        if not visited[neighbor]:
            isInCycle = nodeInCycle(neighbor, edges, visited, stack)
            if isInCycle:
                return True
        elif stack[neighbor]:
            return True

    stack[node] = False
    return False

edges = [ [1, 3], [2, 3, 4],[0],[],[2, 5],[]]

assert cycleInGraph(edges) == True, "Error. Expected output: True"