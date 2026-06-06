"""
1. Clarity questions and Real world scenario
- Q: Does the diameter have to pass through the root? A: No.
- Q: Is the diameter defined by nodes or edges? A: Edges (number of nodes - 1).
- Scenario: Used in networking to find the longest path between any two devices in a tree-structured topology (maximum latency).

2. Corner cases
- Empty tree: Diameter is 0.
- Single node: Diameter is 0.
- Skewed tree (linked list): Diameter is N-1.

3. Brute force Approach
- For every node, calculate its height. The diameter at each node is (left_height + right_height). Keep track of the global maximum. O(n^2) time.

4. Best Approach
- Post-order DFS. For each node, return its height (1 + max(left_height, right_height)) and simultaneously update a global variable for the diameter using (left_height + right_height).

5. Logic walk through
root = [1, null, 2, 3, 4, 5]

[Initial state: root 1. diameter = 0]
[Action 1: Calculate height for subtrees. Node 2 has left 3, right 4. Node 3 has left 5.]
[Action 2: At node 2: left_h=2 (path 3-5), right_h=1. Diameter = 2+1=3. Update global max.]
[Final result: 3]

6. Time and space complexity
- Time: O(n) where n is the number of nodes.
- Space: O(h) where h is the tree height for the recursion stack.

7. Test cases
- Input: [1, 2, 3, 4, 5], Output: 3
- Input: [1, 2], Output: 1
- Input: [], Output: 0

8. Code
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left_h = dfs(node.left)
            right_h = dfs(node.right)
            
            # Update global max diameter
            self.diameter = max(self.diameter, left_h + right_h)
            
            # Return height of this node
            return 1 + max(left_h, right_h)
        
        dfs(root)
        return self.diameter