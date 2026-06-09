"""
1. Clarity Questions & Real-World Scenario
- Clarity: Are diagonal connections allowed? (No, only horizontal/vertical). Are the grid boundaries fixed? (Yes, max 50x50).
- Scenario: Used in computer vision for segmenting connected components in an image, or in game development to identify distinct geographical features on a tile-based map.

2. Corner Cases
- Empty grid: Return 0.
- Grid with no land (all 0s): Return 0.
- Grid entirely land (all 1s): Return the total area (rows * cols).

3. Brute Force Approach
- Iterate through every cell. If you find a '1', initiate a search (BFS/DFS) to count all connected '1's, marking them as visited (or flipping to '0') to avoid re-counting. Track the global maximum.
- Time: O(m * n). Space: O(m * n) for recursion/queue.

4. Best Approach
- DFS with In-place Modification: Traverse the grid. When a '1' is found, start a DFS. To save space, mark visited land cells by changing them to '0' directly in the input `grid`.
- Time: O(m * n). Space: O(m * n) (worst case recursion depth if grid is all land).

5. Logic Walkthrough (Example: grid[0][1]=1)
grid = [[0,1,1,0,1], ...]
[Initial: grid[0][0]=0, skip. grid[0][1]=1, area=0]
[Action 1: Start DFS at (0,1). Set grid[0][1]=0. area=1.]
[Action 2: Recursive calls visit neighbors (0,2) and (1,2). Set them to 0. Area increments.]
[Final result: Update max_area with total count of current connected land.]

6. Time and Space Complexity
- Time: O(m * n)
- Space: O(m * n) (worst-case recursion stack)

7. Test Cases
- Input: [[0,0,1,0,0],[1,1,1,0,0]] -> Output: 4
- Input: [[0,0,0],[0,0,0]] -> Output: 0
- Input: [[1]] -> Output: 1

8. Code
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            # Mark as visited
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
                    
        return max_area