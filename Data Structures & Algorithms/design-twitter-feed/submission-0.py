"""
1. CLARITY & REAL-WORLD SCENARIO
Clarity:
- Can a user follow themselves? (Implied no/irrelevant).
- Are tweet IDs globally unique? (Yes, assume so).
- Order of tweets in feed: must be strictly chronological.

Real-world: 
- Social media feed generation, activity streams, or notification systems
  where filtering content by relationships (who you follow) is required.

2. CORNER CASES
- getNewsFeed() called for user with no tweets and no followees.
- getNewsFeed() called with 0 tweets total in system.
- unfollow() called on a user not currently followed.
- follow() called on a user already followed.
- getNewsFeed() returns < 10 tweets if less exist.

3. BRUTEFORCE APPROACH
- Store all tweets in a global list.
- For getNewsFeed(userId), iterate through all tweets, filter those 
  from self or followees, sort by timestamp descending, return first 10.
- Time: O(T log T) per query where T is total tweets.

4. BEST APPROACH
- Use HashMaps:
    - tweetMap: userId -> List of (timestamp, tweetId)
    - followMap: userId -> Set of followeeIds
- Use a Global Counter (timestamp) to order tweets.
- Use Max-Heap (Priority Queue) in getNewsFeed to merge top 10 
  from all followees efficiently without full sorting.

5. LOGIC WALKTHROUGH (Whiteboarding)
Example: User 1 follows User 2. User 1 posts 10, User 2 posts 20.
getNewsFeed(1):
[State: tweetMap={1:[(1,10)], 2:[(2,20)]}, followMap={1:{2}}]
[Action: Add (1,10, 1, 0) and (2,20, 2, 0) to Max-Heap]
[Action: Pop (2,20) - append 20, Pop (1,10) - append 10]
[Final: [20, 10]]

6. TIME & SPACE COMPLEXITY
- postTweet: O(1)
- follow/unfollow: O(1)
- getNewsFeed: O(k log n) where n = number of followees, k = 10.
- Space: O(T + U + F) where T=tweets, U=users, F=follows.

7. TEST CASES
- postTweet(1, 5), getNewsFeed(1) -> [5]
- follow(1, 2), postTweet(2, 6), getNewsFeed(1) -> [6, 5]
- unfollow(1, 2), getNewsFeed(1) -> [5]

8. CODE
"""
from collections import defaultdict, deque
import heapq

class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index])
        
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index > 0:
                count, tweetId = self.tweetMap[followeeId][index - 1]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)