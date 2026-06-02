"""
    Binary search : 
        - left and right pointers
        - iterate left < right
        - divide by 2 and check if its target
        - if value at the pointer is
            if equal return that index
            elif less than target, then look in the right half
            otherwise in the left half
        

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # (l + r) // 2 can lead to overflow
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1