def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print("Selection Sort:", selection_sort([64, 25, 12, 22, 11]))

def kruskal(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    mst = []
    edges.sort(key=lambda x: x[2])  # sort by weight

    for u, v, w in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            mst.append((u, v, w))
            parent[rv] = ru
    return mst

edges = [
    (0, 1, 10), (0, 2, 6), (0, 3, 5),
    (1, 3, 15), (2, 3, 4)
]

print("Kruskal's MST:", kruskal(4, edges))


# Job Scheduling using Greedy Method

jobs = [
    ('J1', 2, 100),
    ('J2', 1, 50),
    ('J3', 2, 10),
    ('J4', 1, 20)
]

# Sort jobs by profit (descending)
jobs.sort(key=lambda x: x[2], reverse=True)

# Find max deadline
max_deadline = max(job[1] for job in jobs)

slots = [False] * max_deadline
result = [''] * max_deadline
profit = 0

for job in jobs:
    name, deadline, gain = job
    # Try to schedule in latest available slot before deadline
    for j in range(min(deadline, max_deadline) - 1, -1, -1):
        if not slots[j]:
            slots[j] = True
            result[j] = name
            profit += gain
            break

print("Selected Jobs:", [job for job in result if job])
print("Total Profit:", profit)

# ---------------------------
# Prim's Minimal Spanning Tree
# ---------------------------
import heapq

def prims(n, graph):
    visited = [False] * n
    mst = []
    pq = [(0, 0, -1)]  # (weight, node, parent)

    while pq:
        w, u, parent = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        if parent != -1:
            mst.append((parent, u, w))
        for v, wt in graph[u]:
            if not visited[v]:
                heapq.heappush(pq, (wt, v, u))
    return mst

graph = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}
print("Prim's MST:", prims(4, graph))


# ---------------------------
# Dijkstra's Single-Source Shortest Path
# ---------------------------
def dijkstra(n, graph, src):
    dist = [float('inf')] * n
    dist[src] = 0
    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, wt in graph[u]:
            if dist[v] > dist[u] + wt:
                dist[v] = dist[u] + wt
                heapq.heappush(pq, (dist[v], v))
    return dist

graph2 = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
print("Dijkstra's Shortest Paths:", dijkstra(4, graph2, 0))
