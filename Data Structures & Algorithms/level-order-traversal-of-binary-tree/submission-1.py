"""
1. Clarity Questions & Real-World Scenario
- Clarity: Does the tree structure guarantee nodes are integers? (Yes). Is an empty tree possible? (Yes).
- Scenario: Used in social media platforms to display hierarchical comments (main posts -> replies -> nested replies) or in file system directory structures to represent files/folders level-by-level for UI rendering.

2. Corner Cases
- Empty root (null): Return [].
- Single node tree: Return [[val]].
- Unbalanced/Skewed trees (only left or right children): Ensure the algorithm still captures depth correctly.

3. Brute Force Approach
- Traverse the entire tree using DFS, storing each node's value along with its depth in a hash map. Then, sort the map by depth and reconstruct the list of lists.
- Time: O(n log n) due to sorting. Space: O(n).

4. Best Approach
- Breadth-First Search (BFS) using a Queue.
- By processing the queue level-by-level (using the queue's length at the start of each iteration), you capture nodes level-by-level naturally without extra storage or sorting.
- Time: O(n). Space: O(n).

5. Logic Walkthrough (Example: [3, 9, 20, null, null, 15, 7])
root = [3, 9, 20, null, null, 15, 7]
[Initial: Queue = [3], Result = []]
[Process Level 0: Pop 3, Add children 9, 20. Result = [[3]]]
[Process Level 1: Pop 9, 20. Add their children (none for 9; 15, 7 for 20). Result = [[3], [9, 20]]]
[Process Level 2: Pop 15, 7. Add children (none). Result = [[3], [9, 20], [15, 7]]]
[Final Result: [[3], [9, 20], [15, 7]]]

6. Time & Space Complexity
- Time: O(n) where n is the number of nodes in the binary tree.
- Space: O(n) to store the result list and the queue.

7. Test Cases
- Input: root = [3,9,20,null,null,15,7] -> Output: [[3],[9,20],[15,7]]
- Input: root = [1] -> Output: [[1]]
- Input: root = [] -> Output: []

8. Code
"""

import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque([root] if root else [])
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(level)
            
        return res