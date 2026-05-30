class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if any of them null and return false
        if (not s or not t) or len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT