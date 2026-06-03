"""
Clarification QuestionsCharacters: 
Are we strictly limited to uppercase English letters as stated in the prompt, or could the input include lowercase or symbols?
Performance: Given $N$ (string length) up to 1000, is O(N) expected, or is $O(N log N)$ acceptable?
Mutations: Does "replace" mean the characters are permanently changed in the string, or just logically treated as such during the window calculation?

Corner Cases
$k = 0$: The longest substring must already consist of identical characters.
$k >= string length: The answer should be the total length of the string.
Single character string: Result should be 1.
String with all distinct characters: If k = 0, result is 1; if k>0, result is k+1.

Logic Walkthrough: 
Sliding Window
Goal: Maintain a window [L, R] where (window_size - max_frequency) <= k.
Initialize: L=0, max_freq=0, char_counts = {}.
Expand: Iterate R from 0 to len(s) - 1.
    Update count of s[R] in the hash map.
    Update max_freq = max(max_freq, char_counts[s[R]]).
Shrink: If (window_size - max_freq) > k:
    Decrement count of s[L].
    Increment L.
Result: max_len = max(max_len, R - L + 1).

Example: 
s = "AAABABB", k = 1 
R=0: [A], max_f=1, len=1
R=2: [AAA], max_f=3, len=3
R=3: [AAAB], max_f=3, len=4. (4-3) = 1 (valid as 1 <= k)
R=4: [AAABA], max_f=4, len=5. (5-4) = 1 (valid)
R=5: [AAABAB], max_f=4, len=6. (6-4) = 2 (invalid: 2 > 1). Shrink L until valid.

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res