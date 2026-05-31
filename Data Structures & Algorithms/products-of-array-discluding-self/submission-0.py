class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # working on prefix and postfix multiplication approach
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        result = [1] * len(nums)

        current_prefix = 1
        current_postfix = 1
        zero_counts = 0 # if anytime two 0's we break and return all 0's as result
        
        # Loop to populate the prefix and postfix list
        for i in range(0, len(nums)):

            prefix[i] = current_prefix
            current_prefix *= nums[i]

            j = len(nums) - i - 1
            postfix[j] = current_postfix
            current_postfix *= nums[j]

            # two 0's check
            if nums[i] == 0:
                zero_counts += 1
            
            if zero_counts >= 2:
                return [0] * len(nums)

        # Combine the pre and post arrays to get the results
        for i in range(len(nums)):
            result[i] = prefix[i] * postfix[i]
        
        return result