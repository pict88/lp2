# Build graph from user input
'''graph = {}
n = int(input("Enter number of edges: "))

for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)
'''
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()
start_node = input("Enter starting node: ")

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(neighbour)

print("DFS Traversal:")
dfs(start_node)

queue=[start_node]
visited_bfs=set([start_node])
def bfs_recursive(queue, visited):
    if not queue:
        return
    node = queue.pop(0)
    print(node, end=" ")
    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)
    bfs_recursive(queue, visited) 

print("\n")
bfs_recursive([start_node], set([start_node]))

'''
def bfs(start):
    visited_bfs = set([start])
    queue = [start]
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited_bfs:
                visited_bfs.add(neighbour)
                queue.append(neighbour)

start_node = input("Enter starting node: ")
print("DFS Traversal:")
dfs(start_node)

print("\n\nBFS Traversal:")
bfs(start_node)
'''