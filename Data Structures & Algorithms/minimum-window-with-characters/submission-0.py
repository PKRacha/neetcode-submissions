"""
CLARITY QUESTIONS:
1. Since the problem guarantees a unique shortest substring, can we return any valid shortest one if multiple exist?
2. Are we guaranteed that both s and t consist only of uppercase/lowercase English letters? (Yes, per constraints)

CORNER CASES:
- t is longer than s: Return "".
- No valid window exists in s: Return "".
- s contains all characters of t exactly: Return s.

LOGIC WALKTHROUGH (Whiteboarding):
- Use a sliding window [l, r] and two frequency maps: 'target' (for t) and 'window' (for s).
- 'have' counts how many unique characters in the window meet the frequency requirement of 'target'.

Example: s="axtyz", t="xy"
- [Initial] Target: {x:1, y:1}
- [l=0, r=0]: {a:1}
- [l=0, r=1]: {a:1, x:1}
- [l=0, r=2]: {a:1, x:1, y:1} -> Found "axy", res="axy"
- [l=1, r=2]: {x:1, y:1} -> Found "xy", res="xy" (shorter!)
- [l=1, r=3]: {x:1, y:1, z:1} -> res remains "xy"

TIME AND SPACE COMPLEXITY:
- Time: O(n + m), where n is length of s and m is length of t.
- Space: O(m) to store character counts.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        
        target, window = {}, {}
        for char in t:
            target[char] = target.get(char, 0) + 1
            
        have, need = 0, len(target)
        res, res_len = [-1, -1], float("infinity")
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            
            if char in target and window[char] == target[char]:
                have += 1
                
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
                
        l, r = res
        return s[l : r + 1] if res_len != float("infinity") else ""