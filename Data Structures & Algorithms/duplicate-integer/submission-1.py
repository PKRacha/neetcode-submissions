class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Hashset Length
        return len(set(nums)) < len(nums)