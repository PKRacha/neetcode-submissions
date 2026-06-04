"""
1. Clarity questions
   - Are the integers in the range [1, n]? Yes.
   - Is the array modification allowed? No (per follow-up constraint).
   - Can we use O(n) extra space? No (per follow-up constraint).

2. Corner cases to consider
   - Minimum n=1 (array [1, 1]).
   - Array with all elements same except duplicate.

3. Brute force Approach
   - Nested loops to compare each element with every other element.
   - Time: O(n^2), Space: O(1).

4. Best Approach
   - Floyd’s Cycle-Finding Algorithm (Two Pointers).
   - Treat array values as pointers to indices. Since values are [1, n], they map to valid indices.
   - The duplicate number creates a cycle in the linked list structure.
   - Time: O(n), Space: O(1).

5. Logic walk through
   nums = [1, 3, 4, 2, 2]
   [Initial: slow=nums[0]=1, fast=nums[nums[0]]=3]
   [Step 1: slow=nums[1]=3, fast=nums[nums[3]]=2]
   [Step 2: slow=nums[3]=2, fast=nums[nums[2]]=4]
   [Step 3: slow=nums[2]=4, fast=nums[nums[4]]=2]
   [Intersection found at 2, reset slow=0, move both 1 step until they meet at 2]
   [Final result: 2]

6. Time and space complexity
   - Time: O(n)
   - Space: O(1)

7. Code
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow