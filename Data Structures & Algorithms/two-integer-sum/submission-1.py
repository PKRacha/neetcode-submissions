class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Use a nested loop that adds up to the target for non-matching indices
        
        # Because there is only one exact pair that matches same,
        # we can use the Hashmap with key as number and value as index.
        # for checking if we have the key + current value in loop matches the target thats our results.

        hashmap = {}

        for i, n in enumerate(nums):

            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            
            hashmap[n] = i

        # Not found case
        return []
