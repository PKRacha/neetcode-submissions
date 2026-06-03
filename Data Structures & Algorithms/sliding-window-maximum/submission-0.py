"""
1. CLARITY QUESTIONS
- Is the window size k always valid (i.e., 1 <= k <= length of array)?
- Can the array contain negative numbers? (Yes, handled by the monotonic queue).

2. CORNER CASES
- k = 1: The result should be the same as the input array.
- k = len(nums): The result is a single element (the max of the whole array).
- Strictly decreasing/increasing arrays: Ensure the deque handles these correctly.

3. BRUTE FORCE APPROACH
For every possible window of size k, iterate through all elements in that window
to find the maximum. This results in O(n * k) time complexity, which is inefficient
for large inputs.

4. BEST APPROACH
Use a Monotonic Deque. Store indices of elements in the deque such that their 
corresponding values are in strictly decreasing order. The front of the deque 
will always contain the index of the maximum element for the current window.

5. LOGIC WALKTHROUGH (Whiteboarding)
nums = [1, 3, -1, -3], k = 3
[Initial: deque=[], output=[]]
[i=0 (val=1): deque=[0]]
[i=1 (val=3): 3 > 1, pop index 0, deque=[1]]
[i=2 (val=-1): deque=[1, 2], window size reached, output=[nums[1]=3]]
[i=3 (val=-3): deque=[1, 2, 3], index 1 is out of window, popleft, output=[3, nums[2]=-1]]

6. TIME AND SPACE COMPLEXITY
- Time: O(n), where n is the number of elements in nums. Each element is added and 
  removed from the deque at most once.
- Space: O(k), as the deque stores at most k indices at any time.

7. CODE
"""
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = deque()  # stores indices
        l = r = 0
        
        while r < len(nums):
            # Maintain decreasing order: remove smaller elements from the back
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # Remove index from front if it's outside the current window
            if l > q[0]:
                q.popleft()
            
            # If window size is reached, record the max (front of deque)
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
            
        return output