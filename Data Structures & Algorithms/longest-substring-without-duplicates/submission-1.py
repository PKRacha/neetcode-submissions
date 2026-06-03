"""
Brute Force: 
- using an hashset, from starting point, keep tracking substring 
until we see a repeated character and record the length.
- we should keep doing until the end. 
TC: O(n * m) SC: O(m) -> m is the total number of unique characters

sliding windows approach:
- start from index 0 both left and right pointers 
    and keep moving right pointer.
- keep adding the unique chars to a hash
- when we find repeated character, remove s[l] and move l to right
- result size = r - l + 1 ; (1 b/c index starts at 0)

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
        