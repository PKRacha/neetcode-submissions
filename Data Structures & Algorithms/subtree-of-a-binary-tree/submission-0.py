"""
1. Clarity questions and Real world scenario
- Q: What if root or subRoot is empty? A: If subRoot is empty, it's technically a subtree. If root is empty, it's not.
- Q: Is it possible for the subRoot to be larger than the root? A: Yes, in which case it cannot be a subtree.
- Scenario: This is used in DOM tree manipulation to check if a specific element structure exists within a larger HTML/XML document fragment.

2. Corner cases
- Empty trees (root or subRoot).
- subRoot is larger than root.
- All values are the same, but structures differ.

3. Brute force Approach
- Traverse the `root` tree. For every node encountered, perform a full tree comparison (`isSameTree`) with the `subRoot`.

4. Best Approach
- Recursive DFS: A tree `root` contains `subRoot` if:
  1. `root` and `subRoot` are identical.
  2. `subRoot` is a subtree of `root.left`.
  3. `subRoot` is a subtree of `root.right`.

5. Logic walk through
root = [1, 2, 3, 4, 5], subRoot = [2, 4, 5]

[Initial: Compare root(1) with subRoot(2). Not identical.]
[Action 1: Recurse to left child(2). Compare tree rooted at 2 with subRoot(2). They match.]
[Action 2: Verify all children match (4==4, 5==5). Return True.]
[Final result: True]

6. Time and space complexity
- Time: O(M * N), where M and N are the number of nodes in root and subRoot.
- Space: O(max(H_root, H_subRoot)) for the recursion stack.

7. Test cases
- root=[1,2,3,4,5], subRoot=[2,4,5] -> True
- root=[1,2,3,4,5,null,null,6], subRoot=[2,4,5] -> False
- root=[1], subRoot=[1] -> True

8. Code
"""

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        
        if self.isSameTree(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p, q):
        if not p and not q: return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
