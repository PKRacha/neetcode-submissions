"""
1. CLARITY QUESTIONS & REAL-WORLD SCENARIO
- Clarity Questions:
  * Can the input array 'nums' contain negative numbers or zero? (Constraints say 2 <= nums[i] <= 30, so no).
  * Is the target always positive? (Constraints say 2 <= target <= 30).
  * Does the order of combinations in the final output matter? (No).
- Real-World Scenario:
  * Making change for a specific monetary amount using a set of available coin denominations where you have an unlimited supply of each coin.

2. CORNER CASES
- Target is smaller than the minimum element in 'nums' (e.g., nums = [3, 5], target = 2) -> Output: []
- No combination can form the target (e.g., nums = [3], target = 5) -> Output: []
- Target matches one of the elements exactly (e.g., nums = [2, 3, 5], target = 3) -> Output: [[3]]

3. BRUTE FORCE APPROACH
- Try every possible combination of elements by recursively picking or skipping elements, including duplicate paths that form permutations of the same combination.
- Check if the sum equals the target. Filter out duplicate combinations at the end using a set/sorting.
- Time Complexity: O(N^T) where N is the number of elements and T is the target value.

4. BEST APPROACH
- Backtracking (Decision Tree):
  * For each element at index 'i', we have two choices:
    1. Include the current element 'nums[i]' and stay at index 'i' (since we can reuse elements).
    2. Skip the current element 'nums[i]' and move to the next index 'i + 1'.
  * This prevents generating duplicate combinations (permutations) and eliminates the need for a final filtering step.
  * Pruning: Stop the recursion branch immediately if the current sum exceeds the target.

5. LOGIC WALK THROUGH WITH EXAMPLE
nums = [2, 5], target = 5

[Initial state] i = 0, current_combination = [], remaining_target = 5
[Action 1: Choose 2] i = 0, current_combination = [2], remaining_target = 3
[Action 2: Choose 2] i = 0, current_combination = [2, 2], remaining_target = 1
[Action 3: Choose 2] i = 0, current_combination = [2, 2, 2], remaining_target = -1 -> Exceeds target, Backtrack!
[Action 4: Skip 2] i = 1, current_combination = [2, 2], remaining_target = 1
[Action 5: Choose 5] i = 1, current_combination = [2, 2, 5], remaining_target = -4 -> Exceeds target, Backtrack!
[Action 6: Skip 5] i = 2, current_combination = [2, 2], remaining_target = 1 -> Out of bounds, Backtrack!
[Action 7: Skip 2] i = 1, current_combination = [2], remaining_target = 3
[Action 8: Choose 5] i = 1, current_combination = [2, 5], remaining_target = -2 -> Exceeds target, Backtrack!
[Action 9: Skip 5] i = 2, current_combination = [2], remaining_target = 3 -> Out of bounds, Backtrack!
[Action 10: Skip 2] i = 1, current_combination = [], remaining_target = 5
[Action 11: Choose 5] i = 1, current_combination = [5], remaining_target = 0 -> Target reached! Add to results.
[Action 12: Choose 5] i = 1, current_combination = [5, 5], remaining_target = -5 -> Exceeds target, Backtrack!
[Action 13: Skip 5] i = 2, current_combination = [5], remaining_target = 0 -> Out of bounds, Backtrack!
[Action 14: Skip 5] i = 2, current_combination = [], remaining_target = 5 -> Out of bounds, Terminate.
[Final result] [[5]]

6. TIME AND SPACE COMPLEXITY
- Time Complexity: O(2^(T/M)) where T is the target value and M is the minimum value in 'nums'. The maximum depth of the tree is T/M.
- Space Complexity: O(T/M) to store the recursion stack and the current combination path.

7. TEST CASES
- Test Case 1: nums = [2, 3, 6, 7], target = 7 -> Expected: [[2, 2, 3], [7]]
- Test Case 2: nums = [2, 3, 5], target = 8 -> Expected: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
- Test Case 3: nums = [2], target = 1 -> Expected: []
"""

from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            # Choice 1: Include nums[i]
            cur.append(nums[i])
            backtrack(i, cur, total + nums[i])
            
            # Choice 2: Skip nums[i]
            cur.pop()
            backtrack(i + 1, cur, total)
            
        backtrack(0, [], 0)
        return res