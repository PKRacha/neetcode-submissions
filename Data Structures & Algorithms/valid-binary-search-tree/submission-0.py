"""
1. Clarity Questions & Real-World Scenario
- Clarity: Does the tree have duplicates? (No). Does "valid" mean every node in the left subtree must be strictly less than the root, and every node in the right subtree strictly greater? (Yes).
- Scenario: Database indexing where data must be strictly ordered to allow $O(\log n)$ search performance.

2. Corner Cases
- Single node tree: Always true.
- Empty tree: Always true.
- Skewed tree (linked list structure): Must validate every node against the parent's range.

3. Brute Force Approach
- For every node, traverse its subtrees to check if all values satisfy the BST property.
- Time: $O(n^2)$. Space: $O(h)$ where $h$ is tree height.

4. Best Approach
- Recursive Depth-First Search (DFS) with range tracking. Maintain a valid range `(min_val, max_val)` for each node.
- Time: $O(n)$. Space: $O(h)$ (recursion stack).

5. Logic Walkthrough (Example: [2, 1, 3])
root = [2, 1, 3]
[Initial State: root=2, range=(-inf, inf). Valid.]
[Action 1: Move left (1). Range=( -inf, 2). Valid.]
[Action 2: Move right (3). Range=(2, inf). Valid.]
[Final Result: True]

6. Time & Space Complexity
- Time: $O(n)$
- Space: $O(h)$

7. Test Cases
- Input: [2, 1, 3] -> True
- Input: [1, 2, 3] -> False
- Input: [5, 1, 4, null, null, 3, 6] -> False

8. Code
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        return validate(root, float('-inf'), float('inf'))