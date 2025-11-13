# BFS and DFS Traversal in Python

def dfs(adjmatrix, start, visited, nodes):
    """Depth-First Search using adjacency matrix"""
    print(start, end=" ")
    visited[nodes.index(start)] = True
    for i, connected in enumerate(adjmatrix[nodes.index(start)]):
        if connected == 1 and not visited[i]:
            dfs(adjmatrix, nodes[i], visited, nodes)

def bfs(adjlist, start):
    """Breadth-First Search using adjacency list"""
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in adjlist[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def main():
    # Define graph nodes
    nodes = ["A", "B", "C", "D", "E"]

    # Adjacency matrix representation
    adjmatrix = [
        [0, 1, 1, 0, 0],  # A
        [1, 0, 0, 1, 1],  # B
        [1, 0, 0, 0, 1],  # C
        [0, 1, 0, 0, 0],  # D
        [0, 1, 1, 0, 0]   # E
    ]

    # Adjacency list representation
    adjlist = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "E"],
        "D": ["B"],
        "E": ["B", "C"]
    }

    # Menu for traversal choice
    print("Choose traversal method:")
    print("1. BFS")
    print("2. DFS")

    choice = int(input("Enter choice (1 or 2): "))
    startnode = "A"

    if choice == 1:
        print(f"\nBFS traversal starting from {startnode}: ", end="")
        bfs(adjlist, startnode)
    elif choice == 2:
        print(f"\nDFS traversal starting from {startnode}: ", end="")
        visited = [False] * len(nodes)
        dfs(adjmatrix, startnode, visited, nodes)
    else:
        print("⚠️ Invalid choice!")

if __name__ == "__main__":
    main()
