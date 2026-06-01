class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointer from left and right because of the ascending order
        # TC: O(n) and SC: O(1)

        l, r = 0, len(numbers) - 1

        while l < r: # no <= because we can't use the same element twice.

            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]
        
        return []

