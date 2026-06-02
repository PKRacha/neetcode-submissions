"""
Confirmation questions:
 1. Sorted Timestamps: "Are the timestamp values for set calls guaranteed to be strictly increasing, or could they be out of order?"
 2. Duplicate Keys: "Can the same key be updated with different values at the same timestamp?"
 3. Empty Requests: "How should I handle a get request for a key that has never been set?"
 4. Range Expectations: "What is the expected scale of timestamp values? Will they fit within standard integer limits?"

APPROACH:
        - Use a Hash Map to store keys.
        - Each key points to a list of [value, timestamp] pairs.
        - Since 'set' calls are strictly increasing in time, the list for 
          each key is naturally sorted by timestamp.

ALGORITHM: Binary Search
        - Access the list of pairs for the given key.
        - Binary search on the list to find the largest timestamp <= target.
        - Time Complexity: O(log N) per get call.
        - Space Complexity: O(N * M) total.

"""


class TimeMap:

    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res