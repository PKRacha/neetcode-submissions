"""
CLARITY QUESTIONS:
1. Since strings only contain lowercase letters, can we assume 
    a fixed frequency array of size 26?
2. If len(s1) > len(s2), is it impossible to have a permutation, 
    allowing an immediate False return?

CORNER CASES:
- s1.length > s2.length: Always False.
- s1.length == 1: Direct character match check.
- No permutation exists: Ensure the loop covers all 
        possible windows in s2.

LOGIC WALKTHROUGH:
- Use a sliding window of size len(s1) over s2.
- Maintain frequency counts of characters in s1 and the current window of s2.
- Example: s1="abc", s2="lecabee"
  1. Count s1: {a:1, b:1, c:1}
  2. Window [0:3] in s2 ("lec"): {l:1, e:1, c:1} -> No match.
  3. Slide: Remove 'l', add 'a'. Window [1:4] 
        ("eca"): {e:1, c:1, a:1} -> Match found! Return True.
  TC: O(N) N = len(s2) & SC: O(1)

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counts = [0] * 26
        s2_counts = [0] * 26
        
        # Initialize frequencies for s1 and first window of s2
        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1
            
        # Slide the window across s2
        for i in range(len(s2) - len(s1)):
            if s1_counts == s2_counts:
                return True
            
            # Slide window: remove left char, add new right char
            s2_counts[ord(s2[i]) - ord('a')] -= 1
            s2_counts[ord(s2[i + len(s1)]) - ord('a')] += 1
            
        return s1_counts == s2_counts