"""
1. Clarity & Real-world Scenario:
   - Clarity: Input is unique integers. Output: All possible subsets (Power Set).
   - Scenario: Database indexing where you need to query every possible combination of filter criteria, or generating all possible permission sets for a user based on a list of available roles.

2. Corner Cases:
   - Empty input array: Result should be [[]].
   - Single element array: Result should be [[], [element]].
   - Negative numbers: The logic must handle signed integers correctly.

3. Brute Force Approach:
   - Use nested loops or recursion to generate all possible combinations of lengths 0 to n.
   - Time Complexity: O(n * 2^n), Space: O(n * 2^n).

4. Best Approach:
   - Backtracking. At each element, make two decisions: include it in the current subset or exclude it. 
   This explores the full binary decision tree.

5. Logic Walkthrough:
   nums = [1, 2]
   [Start: index 0, current_subset = []]
   [Include 1: subset becomes [1], recurse to index 1]
   [Include 2: subset becomes [1, 2], index 2 (base case), add [1, 2] to result]
   [Backtrack: remove 2, exclude 2, index 2 (base case), add [1] to result]
   [Backtrack: remove 1, index 1, exclude 1, recurse to index 1]
   [Include 2: subset becomes [2], index 2 (base case), add [2] to result]
   [Backtrack: remove 2, index 2 (base case), add [] to result]
   [Final result: [[1, 2], [1], [2], []]]

6. Time & Space Complexity:
   - Time: O(n * 2^n) - There are 2^n subsets, and each takes O(n) to copy.
   - Space: O(n) - Recursive stack depth.

7. Test Cases:
   - Input: [1, 2, 3] -> Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
   - Input: [7] -> Output: [[], [7]]

8. Code:
"""

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # Decision to exclude nums[i]
            subset.pop()
            dfs(i + 1)
            
        dfs(0)
        return res