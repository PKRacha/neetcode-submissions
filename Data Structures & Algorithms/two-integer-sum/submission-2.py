"""
Goal: 
    - get 2 SMALLER indexes that make the sum as target
    - Result is unique

Corner cases: 
    - when empty or None array? return None
    - Are negative values possible? Yes
    - 

Approach:
    - nested iterate, and add non matching indices values 
            to see if it adds to target. TC: O(n^2) and SC: O(1)
    - Hashmap: 
        Create a hashmap with key as nums[i] and i as value in it.
        iterate the list and then for each value, check if the key exists for (target - value)
        when it does, the hashmap's value and current i are the result. 
        - If we did not find anything by the end, return None. NA


"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if not nums or len(nums) == 0:
            return None

        hash = {}

        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            hash[nums[i]] = i
        
        return []

    