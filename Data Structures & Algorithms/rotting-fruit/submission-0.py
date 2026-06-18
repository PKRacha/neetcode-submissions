"""
1. Clarity & Real-world Scenario:
   - Clarity: Grid with empty (0), fresh (1), and rotten (2) oranges. Every minute, fresh oranges adjacent to rotten ones become rotten. Find minimum minutes to rot all, or -1 if impossible.
   - Scenario: Modeling the spread of infectious diseases in a population or the propagation of faults/errors across a distributed network.

2. Corner Cases:
   - No fresh oranges initially: Return 0.
   - Fresh oranges that cannot be reached: Return -1.
   - Empty grid: Return 0.

3. Brute Force Approach:
   - Repeatedly scan the grid, simulate the rotting process minute by minute by creating a new grid state, and stop when no more changes occur.
   - Time Complexity: O((m*n)^2).

4. Best Approach:
   - Multi-source Breadth-First Search (BFS). Initialize a queue with 
     all initially rotten oranges. Process level by level (each level 
     represents one minute).

5. Logic Walkthrough:
   grid = [[2, 1], [1, 0]]
   [Initial: Queue = [(0, 0)], fresh_count = 2, minutes = 0]
   [Minute 1: Pop (0,0), rot adjacent (0,1) and (1,0). 
        Queue = [(0,1), (1,0)], fresh_count = 0, minutes = 1]
   [Final: All fresh rotten, return minutes = 1]

6. Time and Space Complexity:
   - Time: O(m * n), where m is rows and n is columns; each cell is 
        visited once.
   - Space: O(m * n) for the queue.

7. Test Cases:
   - grid = [[2,1,1],[1,1,0],[0,1,1]] -> 4
   - grid = [[2,1,1],[0,1,1],[1,0,1]] -> -1

8. Code:
"""

from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue and fresh > 0:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
        
        return minutes if fresh == 0 else -1