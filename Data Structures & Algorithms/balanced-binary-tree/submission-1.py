"""
1. Clarity questions and Real world scenario
- Q: What defines a height-balanced tree? A: The difference between the heights of the left and right subtrees of any node is at most 1.
- Scenario: Used in database indexing (AVL trees) to ensure logarithmic search time by preventing the tree from becoming a linked list.

2. Corner cases
- Empty tree: Height-balanced (True).
- Single node tree: Height-balanced (True).
- Deeply skewed tree (e.g., all right children): Not height-balanced.

3. Brute force Approach
- For every node, calculate the height of its left and right subtrees. 
    If the absolute difference is > 1, return False. Else, recurse. This is O(n^2).

4. Best Approach
- Modified DFS: Compute height and check balance in one pass. 
    If a subtree is unbalanced, return -1. 
    Otherwise, return the actual height.

5. Logic walk through
root = [1, 2, 2, 3, 3, null, null, 4, 4]

[Initial state: Check balance at root]
[Action 1: Calculate left height (subtree 2). Left branch height=2, right branch height=1. Balanced.]
[Action 2: Compare left height (2) and right height (2). Difference is 0 <= 1.]
[Final result: True]

6. Time and space complexity
- Time: O(n) as we visit every node exactly once.
- Space: O(h) where h is the tree height due to recursion stack.

7. Test cases
- Input: [1, 2, 3, null, null, 4], Output: True
- Input: [1, 2, 3, null, null, 4, null, 5], Output: False
- Input: [], Output: True

8. Code
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0
            
            left = check(node.left)
            if left == -1: return -1
            
            right = check(node.right)
            if right == -1: return -1
            
            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
            
        return check(root) != -1