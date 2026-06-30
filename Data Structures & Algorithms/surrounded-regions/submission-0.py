"""
1. CLARITY QUESTIONS & REAL-WORLD SCENARIO
- Clarity Questions:
  * Can the board be empty or have 0 rows/columns? (Constraints say 1 <= m, n <= 200).
  * Should we modify the board in-place or return a new board? 
      (Problem specifies in-place, return nothing).
- Real-World Scenario:
  * Image Processing/Segmentation: Flooding a closed region or identifying isolated 
    clusters of pixels (e.g., separating a background from a foreground object that 
    doesn't touch the image borders).

2. CORNER CASES
- Matrix size 1x1, 1xN, or Mx1: No cells can be truly "surrounded" because everything 
     is on the border or adjacent to it.
- Board with no 'O's: No changes needed.
- Board with all 'O's: No changes needed (all connect to borders).
- 'O's completely trapped in the center vs. 'O's snaking out to touch a border.

3. BRUTE FORCE APPROACH
- Iterate through every cell. If it is an 'O', run a standard DFS/BFS to see if 
    it can reach the boundary.
- If the traversal reaches a boundary, none of the 'O's in that cluster are captured.
- If the traversal finishes without hitting a boundary, run a second traversal 
   to turn all those 'O's into 'X's.
- Time Complexity: O(M * N) per cluster, up to O((M * N)^2) worst-case if repeated.

4. BEST APPROACH (Boundary DFS / Flood Fill)
- Reverse the thinking: Instead of finding trapped regions, find the *un-trapped* regions.
- Any 'O' on the border cannot be captured. Any 'O' connected to a border 'O' 
    also cannot be captured.
- Strategy:
  1. Traverse the 4 borders. If an 'O' is found, run DFS/BFS to mark it 
       and all connected 'O's with a temporary marker (e.g., 'T').
  2. Iterate through the entire board:
     - Change remaining 'O's (which are trapped) to 'X'.
     - Change 'T's (which are safe) back to 'O'.

5. LOGIC WALK THROUGH
board = [
  ["X", "X", "X", "X"],
  ["X", "O", "O", "X"],
  ["X", "X", "O", "X"],
  ["X", "O", "X", "X"]
]

[Initial state]
Borders checked. Bottom row has 'O' at (3, 1). 
Run DFS from (3, 1) -> Marks itself as 'T'. No neighboring 'O's.

[After Boundary DFS]
board = [
  ["X", "X", "X", "X"],
  ["X", "O", "O", "X"],
  ["X", "X", "O", "X"],
  ["X", "T", "X", "X"]
]

[Final result/Update]
Iterate through entire board. 
Cells (1,1), (1,2), and (2,2) are 'O' -> converted to 'X'.
Cell (3,1) is 'T' -> converted back to 'O'.

board = [
  ["X", "X", "X", "X"],
  ["X", "X", "X", "X"],
  ["X", "X", "X", "X"],
  ["X", "O", "X", "X"]
]

6. TIME AND SPACE COMPLEXITY
- Time Complexity: O(M * N) where M is rows and N is columns. Every cell is visited a constant number of times.
- Space Complexity: O(M * N) for the recursion stack in the worst-case scenario where the entire board is filled with 'O's.

7. TEST CASES
- Case 1 (Standard): board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
- Case 2 (No capture): board = [["X","O","X"],["O","X","O"],["X","O","X"]] (All 'O's are on borders)
- Case 3 (Single Element): board = [["O"]] -> Out: [["O"]]
"""

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return
        
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Step 1: Mark unsubmerged border-connected regions
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
            
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
            
        # Step 2: Flip captured regions to 'X' and restore border regions to 'O'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
