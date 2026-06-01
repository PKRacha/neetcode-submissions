# BruteForce approach: iterate by computing leftMax, rightMax, min(leftMax, rightMax) arrays. 
#   Sum the min(..) array to get the results.

# Two pointer approach: l, r, track leftMax, rightMax as we are going. As we move the pointers, we keep track of the highest wall seen so far on each side (leftMax and rightMax).
# The water at each position is simply:

# max wall on that side – height at that position
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
        