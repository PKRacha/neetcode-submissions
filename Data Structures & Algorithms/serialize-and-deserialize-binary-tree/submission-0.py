"""
1. Clarity questions and Real world scenario
- Q: What characters can values contain? A: Integers (can be negative).
- Q: Is it guaranteed to be a valid tree? A: Yes.
- Scenario: This is used to persist complex object graphs (like UI component trees or game scene graphs) into a flat file or stream, then restore them without losing the parent-child relationships.

2. Corner cases
- Empty tree (root is None).
- Tree with a single node.
- Left-skewed or right-skewed trees.

3. Brute force Approach
- Serialize: Perform Level-order traversal (BFS) and store every node including null placeholders.
- Deserialize: Use a queue to rebuild the tree level by level.

4. Best Approach
- DFS (Pre-order traversal). Serialize: Visit node, then left child, then right child. Store as a string with "None" as a placeholder. Deserialize: Use a recursive function with a pointer/iterator to reconstruct the nodes in the exact same pre-order sequence.

5. Logic walk through
root = [1, 2, 3, null, null, 4, 5]

[Initial state: Pre-order traversal is 1,2,N,N,3,4,N,N,5,N,N]
[Action 1: Serialize: append '1,2,N,N,3,4,N,N,5,N,N']
[Action 2: Deserialize: pointer at '1', build root(1). Recurse left -> build node(2), then two 'N's (leaf 2 finished). Recurse right -> build node(3)...]
[Final result: Full tree reconstructed]

6. Time and space complexity
- Time: O(n) to traverse and process each node once.
- Space: O(n) to store the serialized string and the recursion stack.

7. Test cases
- Input: [1, 2, 3, null, null, 4, 5], Output: [1, 2, 3, null, null, 4, 5]
- Input: [], Output: []
- Input: [1], Output: [1]

8. Code
"""

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()