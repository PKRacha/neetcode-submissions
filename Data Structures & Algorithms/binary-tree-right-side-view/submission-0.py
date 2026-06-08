"""
1. Clarity Questions & Real-World Scenario
- Clarity: If a level has no right-side node, is it empty? (No, every level exists, and we take the right-most element available).
- Scenario: Used in UI development for rendering sidebars or previews where you only need the most "prominent" or outer element at each hierarchy level, or in network routing to identify the furthest visible node in a segment.

2. Corner Cases
- Empty root: Return [].
- Single node: Return [root.val].
- Skewed tree (left-only): Return the values of the left-most nodes, as they are the "right-most" visible nodes.

3. Brute Force Approach
- Perform a standard Level Order Traversal (BFS) to get a list of lists containing all nodes per level. Then, iterate through each inner list and append the last element to the result.
- Time: O(n). Space: O(n).

4. Best Approach
- Modified BFS: Traverse level by level. Instead of storing all nodes in a list, simply record the value of the last node in the queue before processing the next level. This saves memory by not keeping every node per level in the final result list.
- Time: O(n). Space: O(D), where D is the maximum diameter of the tree (for the queue).

5. Logic Walkthrough (Example: [1,2,3,null,4,null,5])
root = [1,2,3,null,4,null,5]
[Initial: Queue = [1], Result = []]
[Level 1: Pop 1. Result = [1]. Add children 2, 3.]
[Level 2: Pop 2, 3. Last is 3. Result = [1, 3]. Add children 4 (from 2), 5 (from 3).]
[Level 3: Pop 4, 5. Last is 5. Result = [1, 3, 5].]
[Final Result: [1, 3, 5]]

6. Time & Space Complexity
- Time: O(n) as we visit each node exactly once.
- Space: O(D) where D is the maximum width of the tree, as the queue holds at most one level at a time.

7. Test Cases
- Input: [1,2,3,null,5,null,4] -> Output: [1,3,4]
- Input: [1,null,3] -> Output: [1,3]
- Input: [] -> Output: []

8. Code
"""

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = collections.deque([root])
        
        while queue:
            # Add the last node of the current level to result
            res.append(queue[-1].val)
            
            # Process current level
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return res