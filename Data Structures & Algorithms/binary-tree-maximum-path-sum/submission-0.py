"""
1. Clarity & Real World Scenario:
- Clarity: Find the maximum path sum in a binary tree. A path is any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to pass through the root.
- Scenario: Identifying the most profitable route in a network of connected nodes where each node has a profit/cost value.

2. Corner Cases:
- Tree with only one node (positive or negative value).
- Tree with all negative values (result should be the single largest node value).
- Tree with only left or right children (a line).

3. Brute Force Approach:
- For every node, calculate the maximum path sum that passes through it as the highest point.
- Recursively visit every node and perform an O(N) search for each, leading to O(N^2) time complexity.

4. Best Approach:
- Use DFS to calculate the max "gain" from each subtree.
- At each node, calculate the max path passing through it: node.val + left_gain + right_gain.
- Return the max path starting from the node and extending to one side: node.val + max(left_gain, right_gain).
- Time: O(N), Space: O(H) where H is tree height.

5. Logic Walkthrough (root = [1, 2, 3]):
root = 1, left = 2, right = 3
[Initial: DFS at root 1]
[Action: Visit left child 2 (returns 2), visit right child 3 (returns 3)]
[Action: Calculate path through 1: 1 + 2 + 3 = 6. Update max_sum = 6]
[Final result: 6]

6. Time and Space Complexity:
- Time: O(N) where N is the number of nodes.
- Space: O(H) for recursion stack.

7. Test Cases:
- root = [1, 2, 3] -> 6
- root = [-10, 9, 20, null, null, 15, 7] -> 42

8. Code:
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            res = max(res, node.val + left + right)
            return node.val + max(left, right)
            
        dfs(root)
        return res