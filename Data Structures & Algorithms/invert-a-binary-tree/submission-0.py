"""
1. Clarity questions and Real world scenario
- Q: Can the tree be empty? A: Yes. 
- Q: What if the tree has only one node? A: The node remains as is.
- Scenario: This is used in UI rendering engines to mirror tree structures or in data processing to reverse hierarchical relationships.

2. Corner cases
- Empty tree (root is None).
- Tree with only a root node.
- Tree with only left children (skewed left).
- Tree with only right children (skewed right).

3. Brute force Approach
- Traverse the tree (DFS or BFS). For each node encountered, swap its left and right pointers. Continue recursively for children.

4. Best Approach
- Recursive DFS. Visit each node once, swap left and right, and return the modified node. This visits each node exactly once.

5. Logic walk through
root = [4, 2, 7, 1, 3, 6, 9]

[Initial: root node is 4. Left child 2, Right child 7]
[Action: Swap 2 and 7. Recursive call on left(2) and right(7)]
[Action: Swap children of 2 (1, 3) -> now 3, 1. Swap children of 7 (6, 9) -> now 9, 6]
[Final result: [4, 7, 2, 9, 6, 3, 1]]

6. Time and space complexity
- Time: O(n), where n is the number of nodes, as we visit each node once.
- Space: O(h), where h is the height of the tree due to the recursion stack.

7. Test cases
- Input: [], Output: []
- Input: [2, 1, 3], Output: [2, 3, 1]
- Input: [1, 2], Output: [1, None, 2]

8. Code
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Swap the children
        root.left, root.right = root.right, root.left
        
        # Recurse
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root