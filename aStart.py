import heapq

def read_input(filename="input.txt"):
    with open(filename, "r") as f:
        R, C = map(int, f.readline().split())
        grid = [list(map(int, f.readline().split())) for _ in range(R)]
        sr, sc = map(int, f.readline().split())
        tr, tc = map(int, f.readline().split())
    return R, C, grid, (sr, sc), (tr, tc)

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(R, C, grid, start, target):
    pq = []
    heapq.heappush(pq, (0, start))
    g_cost = {start: 0}
    parent = {start: None}

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while pq:
        f, current = heapq.heappop(pq)

        if current == target:
            # Reconstruct Path
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1], g_cost[target]

        for d in directions:
            nr, nc = current[0] + d[0], current[1] + d[1]

            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                new_cost = g_cost[current] + 1
                neighbor = (nr, nc)

                if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_cost
                    f_cost = new_cost + manhattan(neighbor, target)
                    heapq.heappush(pq, (f_cost, neighbor))
                    parent[neighbor] = current

    return None, None

# Main Execution
if __name__ == "__main__":
    R, C, grid, start, target = read_input()
    path, cost = a_star(R, C, grid, start, target)

    if path:
        print(f"Path found with cost {cost} using A*")
        print("Shortest Path:", path)
    else:
        print("Path not found using A*")
