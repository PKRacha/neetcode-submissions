"""
1. CLARITY & REAL-WORLD SCENARIO
Clarity:
- Can we move diagonally? (No, only up, down, left, right).
- What if a cell cannot reach any treasure? (Keep as INF).
- Are treasure chests starting points? (Yes).

Real-world:
- Pathfinding in games to determine accessibility/proximity to resources.
- Network routing to find the nearest server or node from multiple available sources.

2. CORNER CASES
- Grid with no treasure chests.
- Grid completely filled with water (-1).
- Grid with only one treasure chest and no land.
- Grid where land is entirely surrounded by water.

3. BRUTEFORCE APPROACH
- For every land cell (INF), perform a BFS or DFS to find the shortest path to any treasure chest (0).
- Time: O((M * N)^2).

4. BEST APPROACH
- Multi-Source BFS: Add all treasure chest coordinates to a queue initially.
- Process the queue level by level. When moving from a treasure to a land cell, the distance is current_cell_dist + 1.
- This ensures each cell is visited only once.

5. LOGIC WALKTHROUGH
grid = [[INF, -1, 0, INF], [INF, INF, INF, -1]]
[Initial state: Queue = [(0, 2)], Distance map updated]
[Action 1: Pop (0, 2), add neighbors (0, 3) and (1, 2) with dist 1]
[Action 2: Pop (0, 3), (1, 2), add further valid neighbors with dist 2]
[Final result: [[3, -1, 0, 1], [2, 2, 1, -1]]]

6. TIME & SPACE COMPLEXITY
- Time: O(M * N) where M is rows, N is columns. Every cell is visited at most once.
- Space: O(M * N) for the queue in the worst case.

7. TEST CASES
- grid = [[0, -1], [INF, INF]] -> [[0, -1], [1, 2]]
- grid = [[INF, -1], [-1, INF]] -> [[INF, -1], [-1, INF]]

8. CODE
"""
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))