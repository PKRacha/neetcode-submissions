"""
1. Clarity & Real World Scenario:
- Clarity: The input is a BST; common ancestor is the lowest node having p and q as descendants.
- Scenario: File system directory path resolution or finding the common root namespace for two classes/modules in a code dependency tree.

2. Corner Cases:
- p or q is the root node.
- p is a direct child of q (or vice versa).
- The tree contains only two nodes.
- Tree with all nodes in a single line (skewed tree).

3. Brute Force Approach:
- Find the path from root to p and root to q by storing node references in two lists.
- Compare the lists and return the last node that is common to both.
- Time: O(N), Space: O(N).

4. Best Approach:
- Utilize BST properties: If both p and q are less than current, move left. If both are greater, move right. If they split (one less, one greater), the current node is the LCA.
- Time: O(h), Space: O(1).

5. Logic Walkthrough (p=3, q=8):
root = 5, p = 3, q = 8
[Initial: Current node is 5]
[Compare: 3 < 5 and 8 > 5. Since p and q are on different sides, 5 is the split point]
[Final Result: 5]

6. Time and Space Complexity:
- Time: O(h), where h is tree height.
- Space: O(1) for iterative approach.

7. Test Cases:
- root=[5,3,8,1,4,7,9,null,2], p=3, q=4 -> 3
- root=[5,3,8], p=5, q=8 -> 5

8. Code:
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            # Both less than curr
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # Both greater than curr
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If split or itself return curr
            else:
                return curr
