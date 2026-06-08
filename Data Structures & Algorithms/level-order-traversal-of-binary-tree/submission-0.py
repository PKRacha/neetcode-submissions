"""
    - Clarify questions:
        * Is it Binary Tree or Binary Search Tree or Tree? Binary Tree
        * order is from left to right
    
    - Edge conditions:
        * If single element - return array of that element in an array
        * empty is empty array
        * None ? empty array
    
    - Simple or brute force: Iterate through the array and store the elements in multiple of 2 intervals as sub-arrays.
        O(n) and O(1)
    - will need to apply BFS with recursive approach:
        O(log n) because it happens in parallel and O(1)



-- DFS (Depth First Search)

                         1
                       /   \
                      2      3
                    /  \    /  \
                   4    5  6    7 

       processing order:  1, 2, 4, 5, 3, 6, 7

 - BFS

                         1
                       /   \
                      2      3
                    /  \    /  \
                   4    5  6    7

       processing order: 1, 2, 3, 4, 5, 6, 7
    TC: O(n) and SC: O(n)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        res = []
        queue = collections.deque([root] if root else [])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level)
        
        return res
            



        