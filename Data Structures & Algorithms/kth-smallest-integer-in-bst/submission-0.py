"""
1. Clarity Questions & Real-World Scenario
- Clarity: Is the BST guaranteed to be valid? (Yes). Is k always within 1 and the number of nodes? (Yes).
- Scenario: Used in database systems for retrieving the "k-th" ranked entry (e.g., finding the k-th lowest price item) in a sorted search index.

2. Corner Cases
- Single node tree: Always returns the root value.
- k = 1: Always returns the minimum value (left-most node).
- k = Total nodes: Always returns the maximum value (right-most node).

3. Brute Force Approach
- Perform an In-Order Traversal to collect all node values into a list. Since an In-Order traversal of a BST is always sorted, simply return the element at index `k - 1`.
- Time: O(n). Space: O(n).

4. Best Approach
- Iterative In-Order Traversal using a stack. Traverse left as far as possible, popping and decrementing k until k reaches 0. This stops early as soon as the k-th element is found.
- Time: O(h + k) where h is tree height. Space: O(h).

5. Logic Walkthrough (Example: [3, 1, 4, null, 2], k = 1)
root = [3, 1, 4, null, 2]
[Initial: Stack = [], Current = 3, k = 1]
[Action 1: Push 3, 1. Stack = [3, 1]. Current = 1.]
[Action 2: Pop 1, k becomes 0. Return 1.]
[Final Result: 1]

6. Time & Space Complexity
- Time: O(h + k)
- Space: O(h)

7. Test Cases
- Input: [3,1,4,null,2], k = 1 -> Output: 1
- Input: [5,3,6,2,4,null,null,1], k = 3 -> Output: 3
- Input: [1], k = 1 -> Output: 1

8. Code
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while curr or stack:
            # keep iterating node and lefts 
            #   until the left most leaf element
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # see if we reached k elements, then its our answer.
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right