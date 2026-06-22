"""
1. CLARITY & REAL-WORLD SCENARIO
Clarity:
- Can elements be reused? No.
- Do duplicates exist in the input array? Yes.
- Must the output contain unique combinations? Yes.

Real-world: 
- Resource allocation where you have distinct items (some identical in value) 
  and need to find every unique way to reach a total capacity without reusing items.

2. CORNER CASES
- Target is 0 (return empty list or [[]]).
- Empty input array.
- No combination sums to the target.
- Array elements are larger than the target.

3. BRUTE FORCE
- Generate all possible subsets (Power Set).
- Filter subsets that sum to the target.
- Use a Set to store results to ensure uniqueness.
- Complexity: O(2^n * n), highly inefficient.

4. BEST APPROACH
- Sort the array first to handle duplicates easily.
- Backtracking with pruning.
- Skip duplicate elements at the same recursion depth to ensure unique combinations.

5. LOGIC WALKTHROUGH (Example: candidates=[1, 1, 2], target=3)
candidates = [1, 1, 2], target = 3, sorted
[Start: index 0, current_path=[], remaining=3]
- Include candidates[0]=1, remaining=2, index=1
- Include candidates[1]=1, remaining=1, index=2
- Include candidates[2]=2 -> 1+1+2=4 (Exceeds 3, backtrack)
- Skip index 1 (duplicate 1), move to index 2
- Include candidates[2]=2, remaining=0 -> Path [1, 2] Found
[Final result: [[1, 2]]]

6. TIME AND SPACE COMPLEXITY
- Time: O(2^n) in worst case (where n is length of candidates).
- Space: O(n) for recursion stack.

7. TEST CASES
- Input: [10,1,2,7,6,1,5], Target: 8 -> Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
- Input: [2,5,2,1,2], Target: 5 -> Output: [[1,2,2],[5]]

8. CODE
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()
        
        def backtrack(remaining, start, path):
            if remaining == 0:
                results.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at the same level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] > remaining:
                    break
                    
                path.append(candidates[i])
                backtrack(remaining - candidates[i], i + 1, path)
                path.pop()
                
        backtrack(target, 0, [])
        return results