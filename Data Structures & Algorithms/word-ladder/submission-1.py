"""
1. Clarity Questions & Real-World Scenario
- Clarity: Are transformation words limited to the wordList? (Yes). Does the sequence require transforming the entire word at once? (No, one letter at a time).
- Scenario: Used in bioinformatics to determine the evolutionary distance between DNA sequences or in search engines for query suggestion/spell correction.

2. Corner Cases
- endWord not in wordList: Return 0.
- beginWord == endWord: Return 0.
- No possible transformation path: Return 0.

3. Brute Force Approach
- Model the problem as a graph where words are nodes and edges exist between words differing by one character. Perform BFS to find the shortest path.
- Precomputing all edges: O(n^2 * m) where n is word count, m is length.

4. Best Approach
- Optimized BFS with Pattern Matching: Instead of comparing every word pair, generate "wildcard" patterns (e.g., "h*t") for each word. Group words by these patterns in a hash map. BFS traverses these patterns to find the shortest path in O(m^2 * n) time.

5. Logic Walkthrough (Example: begin="hit", end="cog", list=["hot","dot","dog","lot","log","cog"])
s = "hit", t = "cog"
[Initial state: Queue = ["hit"], Visited = {"hit"}, Dist = 1]
[Action 1: Pop "hit". Generate patterns: "*it", "h*t", "hi*". "h*t" matches "hot". Add "hot" to queue.]
[Action 2: Pop "hot". Match patterns to "dot", "lot". Continue until "cog" reached.]
[Final result/Update: Return distance (5)]

6. Time and Space Complexity
- Time: O(m^2 * n)
- Space: O(m^2 * n)

7. Test Cases
- Input: "hit", "cog", ["hot","dot","dog","lot","log","cog"] -> Output: 5
- Input: "hit", "cog", ["hot","dot","dog","lot","log"] -> Output: 0
- Input: "a", "c", ["a","b","c"] -> Output: 2

8. Code
"""

from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Precompute pattern buckets
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                # For each pattern, go through the neighboring words
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
            
        return 0