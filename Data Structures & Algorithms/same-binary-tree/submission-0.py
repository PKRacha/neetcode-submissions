"""
1. Clarity questions and Real world scenario
- Q: What if both trees are empty? A: True (they are equivalent).
- Q: Can the values be negative? A: Yes.
- Scenario: Used in version control systems or document comparison tools 
    to verify if two directory structures or file trees are identical.

2. Corner cases
- Both trees are None: True.
- One tree is None, other is not: False.
- Different structure but same values: False.
- Same structure but different values: False.

3. Brute force Approach
- Serialize both trees into lists (using a traversal like Pre-order) and compare the lists. 
    If the lists are identical, the trees are the same.

4. Best Approach
- Recursive DFS: Compare the root values, then recursively check left children and right children. 
    If any mismatch occurs, return False immediately.

5. Logic walk through
p = [1, 2, 3], q = [1, 2, 3]
[Initial state: Compare root values. 1 == 1. Recurse.]
[Action 1: Left child compare: 2 == 2. Recurse.]
[Action 2: Right child compare: 3 == 3. All matches.]
[Final result: True]

6. Time and space complexity
- Time: O(n), where n is the number of nodes in the smaller tree.
- Space: O(h), where h is the height of the tree for the recursion stack.

7. Test cases
- Input: p=[1,2,3], q=[1,2,3], Output: True
- Input: p=[1,2], q=[1,null,2], Output: False
- Input: p=[], q=[], Output: True

8. Code
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both are None, they are identical
        if not p and not q:
            return True
        
        # If one is None or values differ, they are not identical
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

