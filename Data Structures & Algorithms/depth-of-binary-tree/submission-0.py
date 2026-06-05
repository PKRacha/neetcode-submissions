"""
1. Clarity questions and Real world scenario
- Q: What if the tree is empty? A: Return 0.
- Q: Does a single node count as depth 1? A: Yes.
- Scenario: Used in calculating the structure of file systems (directory nesting) or analyzing UI component hierarchies.

2. Corner cases
- Tree is empty (root is None).
- Tree has only one node.
- Tree is a straight line (skewed tree).

3. Brute force Approach
- Traverse the tree level by level using BFS. Keep a counter for each level. The total count of levels is the depth.

4. Best Approach
- Recursive DFS. The depth of a node is 1 + max(depth of left child, depth of right child).

5. Logic walk through
root = [3, 9, 20, null, null, 15, 7]

[Initial state: root is 3. Calculate maxDepth(3)]
[Action 1: maxDepth(3) = 1 + max(maxDepth(9), maxDepth(20))]
[Action 2: maxDepth(9) = 1; maxDepth(20) = 1 + max(maxDepth(15), maxDepth(7)) = 1 + 1 = 2]
[Final result: 1 + max(1, 2) = 3]

6. Time and space complexity
- Time Complexity: O(n), where n is the number of nodes, as we visit each node once.
- Space Complexity: O(h), where h is the tree height, due to the recursion stack.

7. Test cases
- Input: [3, 9, 20, null, null, 15, 7], Output: 3
- Input: [1, null, 2], Output: 2
- Input: [], Output: 0

8. Code
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)