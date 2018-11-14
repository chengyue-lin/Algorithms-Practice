"""
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""

def search(graph, node1, node2):

    if node1 == node2:
        return True

    state = {node: "unvisited" for node in graph.keys()}

    state[node1] = "visiting"

    q = list()
    q.append(node1)
    while len(q):
        u = q.pop(0)
        for node in graph[u]:
            if node == node2:
                return True
            if state[node] == "unvisited":
                q.append(node)
                state[node] = "visiting"
        state[u] = "visited"
    return False

if __name__ == "__main__":
    graph = dict()
    """
    size = int(raw_input("Enter number of nodes in the graph: "))
    print("Enter the directed graph: ")

    for _ in xrange(size):
        key = raw_input("Enter node names: ")
        value = raw_input("Enter the adjacent nodes separated by space: ").split()
        graph[key] = value

    node1 = raw_input("Enter node 1: ")
    node2 = raw_input("Enter node 2: ")
    
    print search(graph, node1, node2)
    """
    print search({'0': ['1', '4', '5'], '1': ['4', '3'], '2': ['1'], '3': ['2', '4'], '4': [], '5': []}, '1', '2')
