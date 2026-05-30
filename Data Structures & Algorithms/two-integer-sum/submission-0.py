class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
     # Use a nested loop that adds up to the target for non-matching indices
     
     # Because there is only one exact pair that matches same,
     # we can use the Hashmap with key as number and value as index.
     # for checking if we have the key + current value in loop matches the target thats our results.

     nums_dict = {}
     for i, n in enumerate(nums):

        if target - n in nums_dict:
            return [nums_dict[target-n], i]
        nums_dict[n] = i
    
     return []