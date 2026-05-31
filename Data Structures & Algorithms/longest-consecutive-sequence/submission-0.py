"""
 - we can sort the nums and then calculate the longest_consecutive 
        using max_longest and current_longest by checking 
        if the current value + 1 is next value at index.
 - 
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

        