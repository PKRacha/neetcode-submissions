"""
1. Clarity Questions & Real-World Scenario
- Clarity: Are there duplicate values in the tree? (Typically no, problem assumes unique values).
- Scenario: Used in compilers or interpreters to reconstruct the expression tree from serialized traversal data, or in data synchronization systems to rebuild a tree structure from its logs.

2. Corner Cases
- Empty arrays: Return None.
- Single node tree: Return a node with that single value.
- Skewed trees: Ensure recursion depth handles linear structure.

3. Brute Force Approach
- Take the first element of preorder as the root. Find its index in inorder. Slice the inorder array into left/right subtrees and calculate the size of the left subtree. Use this size to slice the preorder array. Recursively build.
- Time: O(n^2) due to searching for index and array slicing. Space: O(n).

4. Best Approach
- Use a hash map to pre-store the indices of all inorder values for O(1) lookup. Pass boundary indices (l, r) to the recursive function instead of slicing arrays.
- Time: O(n). Space: O(n) (for hash map and recursion stack).

5. Logic Walkthrough (Example: preorder=[3,9,20], inorder=[9,3,20])
preorder=[3,9,20], inorder=[9,3,20]
[Initial state: Root=3, mid=1 (index of 3 in inorder)]
[Action 1: Build left subtree with preorder[1:2] and inorder[0:1], result=Node(9)]
[Action 2: Build right subtree with preorder[2:3] and inorder[2:3], result=Node(20)]
[Final result: Tree with root 3, left child 9, right child 20]

6. Time and Space Complexity
- Time: O(n)
- Space: O(n)

7. Test Cases
- Input: preorder=[3,9,20,15,7], inorder=[9,3,15,20,7] -> Output: [3,9,20,null,null,15,7]
- Input: preorder=[-1], inorder=[-1] -> Output: [-1]
- Input: preorder=[], inorder=[] -> Output: []

8. Code
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Precompute index map for O(1) lookup
        indices = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def dfs(l, r):
            if l > r:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
            
        return dfs(0, len(inorder) - 1)