"""
1. Clarity questions and Real world scenario
- Q: Why is BFS sometimes preferred over DFS for this problem? A: BFS explores the island layer by layer (like a ripple in a pond), which is often more intuitive for "shortest path" or "boundary" related problems and avoids the recursion depth limits of DFS in extremely large grids.
- Scenario: Used in search-and-rescue operations to map out a continuous region or in image processing to identify connected components (blobs).

2. Corner cases
- Empty grid: 0 islands.
- Grid with no land: 0 islands.
- Grid entirely land: 1 island.
- Grid with a single '1' cell: 1 island.

3. Brute force Approach
- Naive search: Scan every cell. For every '1', try to find all connected neighbors manually without a formal queue or stack. Very inefficient due to repeat work.

4. Best Approach (BFS)
- Iterative BFS using a queue: Iterate through the grid. When a '1' is found, increment the island count, then use a queue to traverse and 'sink' (set to '0') all connected land cells level by level.

5. Logic walk through
grid = [["1","1","0"], ["0","0","0"], ["0","1","1"]]

[Initial state: Search grid. Found '1' at (0,0). Increment count = 1]
[Action 1: Queue: [(0,0)]. Pop (0,0). Neighbors (0,1) are '1'. Queue: [(0,1)]. Set grid[0][0]='0']
[Action 2: Pop (0,1). Neighbors are '0'. Queue empty. Search grid... Found '1' at (2,1). Increment count = 2.]
[Final result: Total islands = 2]

6. Time and space complexity
- Time Complexity: O(M * N), where M = rows, N = columns. Each cell is added to the queue at most once.
- Space Complexity: O(min(M, N)) in the best case or O(M * N) in the worst case for the queue storage.

7. Test cases
- Input: [["1","1","1"], ["0","1","0"], ["1","0","0"]], Output: 1
- Input: [["1","0"], ["0","1"]], Output: 2
- Input: [], Output: 0

8. Code
"""

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = "0"  # Mark as visited
            while q:
                curr_r, curr_c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = "0"  # Mark as visited
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
                    
        return islands