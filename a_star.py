# A* Algorithm for 2D Maze Problem

maze = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

# Heuristic function (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star():

    open_list = [start]
    visited = set()

    g = {start: 0}
    parent = {start: start}

    while open_list:

        current = open_list[0]

        # Find node with minimum f(n)
        for node in open_list:
            if g[node] + heuristic(node, goal) < g[current] + heuristic(current, goal):
                current = node

        # Goal reached
        if current == goal:

            path = []

            while parent[current] != current:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            print("Path Found:")
            for p in path:
                print(p)

            return

        open_list.remove(current)
        visited.add(current)

        x, y = current

        # Possible moves
        moves = [(0,1), (1,0), (0,-1), (-1,0)]

        for dx, dy in moves:

            nx, ny = x + dx, y + dy

            neighbor = (nx, ny)

            # Check boundaries and walls
            if 0 <= nx < 4 and 0 <= ny < 4 and maze[nx][ny] == 0:

                if neighbor not in visited:

                    g[neighbor] = g[current] + 1
                    parent[neighbor] = current

                    if neighbor not in open_list:
                        open_list.append(neighbor)

    print("No Path Found")

# Run A*
a_star()

import heapq

def astar(grid, start, goal):
    h = lambda a, b: abs(a[0]-b[0]) + abs(a[1]-b[1])
    pq = [(0, 0, start, [start])]
    seen = set()
    while pq:
        _, cost, pos, path = heapq.heappop(pq)
        if pos == goal:
            return path
        if pos in seen:
            continue
        seen.add(pos)
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            r, c = pos[0]+dr, pos[1]+dc
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0:
                heapq.heappush(pq, (cost+1+h((r,c),goal), cost+1, (r,c), path+[(r,c)]))
    return None

grid = [
    [0,0,0,1,0],
    [1,0,0,1,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [0,0,0,0,0]
]
path = astar(grid, (0,0), (4,4))
print("Path:", path)