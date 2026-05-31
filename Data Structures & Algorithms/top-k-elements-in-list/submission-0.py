"""
    Approach 1:
    1. Create a hashmap to store the frequency of each number
    2. Build an array with [frequency, num] and sort it based on frequency
    3. Pop the k elements from the array in #2 and return it as the result

    TC: O(n log n) & SC: O(n)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # get the counts of each number
        num_freq = {}
        for num in nums:
            num_freq[num] = 1 + num_freq.get(num, 0)
        
        # Lets build array with frequency, num and sort it
        arr = []
        for num, cnt in num_freq.items():
            arr.append([cnt, num])
        arr.sort()

        # Get the results using k
        res = []
        while len(res) < k: # its "<" because we are using while loop
            res.append(arr.pop()[1])

        return res