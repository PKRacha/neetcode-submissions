"""
-- nums array, which can be rotated 1 to n times. 
    -> Means, it could be all sorted (when n times) and 2 parts of sorted when rotated
-- Return the index of target value. -1 for not found case.
-- UNIQUE numbers...

-- Simply we can iterated and just look for the target and return the index. 
    TC: O(n) and SC: O(1)

I think I could apply Binary Search here with some additional conditions
nums = 3, 4, 5, 6, 1, 2 target = 1
First lets check if its l < m < r, then this is rotated n times and its already sorted.
    so, we can just do normal binary search TC: O(log n)

If not, 3, 4, 5, 6, 1, 2 
mid           |          
           6, 1, 2    
mid           |            
TC: O(log n) 


"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1