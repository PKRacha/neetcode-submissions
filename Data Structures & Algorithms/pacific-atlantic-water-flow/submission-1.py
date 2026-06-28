"""
- Problem: 
    heights -> above sea level
    (r, c) -> coordinates 
    Ask: all cells [(r1,c1), (r2, c2),...] where water can 
        flow to both Atlantic and Pacific oceans.
        
        pacific
       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
    p |                             | a  
    a |                             | t
    c |                             | l
    i |                             | a
    f | 4 2 7 3 4                   | n
    i | 7 4 6 4 7                   | t
    c | 6 3 5 3 6                   | i
       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  c
        atlantic

1. CLARITY & REAL-WORLD SCENARIO
- Clarity: Does water flow diagonally? No, only cardinal directions. Can it flow up? Yes, if the neighbor is lower or equal.
- Scenario: Watershed management, mapping flow patterns on terrain, or determining if rainfall in a specific region reaches a common basin.

2. CORNER CASES
- Grid size 1x1: Always flows to both oceans.
- Flat island: All cells connected to both.
- Island with all same heights: Everything flows to both.

3. BRUTEFORCE APPROACH
- For every cell, run a BFS/DFS to see if it reaches the Pacific (Top/Left border) and Atlantic (Bottom/Right border).
- Complexity: O((M*N)^2).

4. BEST APPROACH
- Run DFS/BFS from the oceans "inwards."
- Find all cells that can reach the Pacific starting from its borders (up/left).
- Find all cells that can reach the Atlantic starting from its borders (down/right).
- Intersection of these two sets of cells is the result.

5. LOGIC WALK THROUGH (Example: 2x2 grid)
heights = [[1, 2], [2, 1]]
[Initial: PacificSet = {(0,0), (0,1), (1,0)}, AtlanticSet = {(0,1), (1,0), (1,1)}]
[Action 1: From Pacific, (0,0) can reach (1,0) if 1 >= 2 (False). (0,1) can reach (0,0) if 2 >= 1 (True).]
[Action 2: Intersection of PacificSet and AtlanticSet.]
[Final Result: {(0,1), (1,0)}]

6. TIME AND SPACE COMPLEXITY
- Time: O(M * N)
- Space: O(M * N)

7. TEST CASES
- [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
- [[1]]

8. CODE
"""
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights: return []
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set() # pacific and atlantic oceans

        def dfs(r, c, visit, prev_h):
            if ( 
                 (r, c) in visit # Already visited
                    or  not (0 <= r < ROWS and 0 <= c < COLS) # out of bounds
                    or heights[r][c] < prev_h # if less height than previous
                ):
                return
            # If not then add to the respective oceans
            visit.add((r, c))
            # Run the same for all the sides
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r + dr, c + dc, visit, heights[r][c])

        for c in range(COLS):
             # first and last rows all can reach pacific oceans
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            # first and last columns can reach atlantic oceans
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        return list(pac.intersection(atl))