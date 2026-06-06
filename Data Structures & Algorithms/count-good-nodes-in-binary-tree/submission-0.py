"""
1. Clarity questions and Real world scenario
- Q: What if the root is None? A: Return 0.
- Q: Is the root itself always considered 'good'? A: Yes, there are no nodes above it.
- Scenario: Used in filtering data hierarchies, such as finding nodes in a corporate org chart that are not subservient to any higher-paid manager (identifying "top" talent in sub-trees).

2. Corner cases
- Tree with a single node (always good).
- Tree with all nodes in descending order (only the root is good).
- Tree with all nodes in ascending order (all nodes are good).

3. Brute force Approach
- For every node, traverse from the root to that node to check if any ancestor has a value greater than the current node. O(n^2).

4. Best Approach
- Recursive DFS: Pass the `max_val` seen so far down the path. If current node value >= `max_val`, it is good. Update `max_val` for children. O(n).

5. Logic walk through
root = [3, 1, 4, 3, null, 1, 5]

[Initial state: root 3, max_so_far = -infinity]
[Action 1: Node 3 >= -inf? Yes (Count=1). Recurse left (max=3), right (max=3)]
[Action 2: Left child 1 >= 3? No. Right child 4 >= 3? Yes (Count=2)]
[Final result: Continue until all nodes processed. Total Count = 4]

6. Time and space complexity
- Time: O(n) where n is the number of nodes.
- Space: O(h) where h is the tree height due to recursion stack.

7. Test cases
- Input: [3, 1, 4, 3, null, 1, 5], Output: 4
- Input: [3, 3, null, 4, 2], Output: 3
- Input: [1], Output: 1

8. Code
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            count = 1 if node.val >= max_val else 0
            new_max = max(max_val, node.val)
            
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            
            return count
            
        return dfs(root, float('-inf'))