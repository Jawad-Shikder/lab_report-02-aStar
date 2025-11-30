# A* Search Algorithm – Shortest Path in a 2D Grid

This project implements the **A\*** (A-Star) pathfinding algorithm to find the shortest route in a 2D maze.  
The program reads maze data from **input.txt**, then computes the shortest path using **Manhattan distance** as the heuristic.

## 🚀 Features
- Reads maze and coordinates from `input.txt`
- Implements **A\*** search with priority queue
- Uses **Manhattan Distance** for heuristic calculation
- Allows movement in four directions (Up, Down, Left, Right)
- Outputs:
  - Path found / Path not found
  - Total path cost
  - The complete shortest path

### Example Input

```4 4
0 0 0 0
1 1 0 1
0 0 0 0
0 1 1 0
0 0
3 3
```
### Example Output

```Path found with cost 6 using A*
Shortest Path: [(0,0), (0,1), (0,2), (1,2), (2,2), (2,3), (3,3)]
```

