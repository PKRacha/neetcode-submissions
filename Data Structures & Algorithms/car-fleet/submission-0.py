"""
n-cars one-lane

position[i]
speed[i]
target 

e.g.1: target = 10, position = [1,4], speed = [3,2]
time to destination -> 3s    3s           --> 3s and 3s, so 1
speed               -> 3     2   
cars                -> c1    c2
line                -> --------------------
nums                -> 1 2 3 4 5 6 7 8 9 10


e.g.2: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
                        []  []   [    ]
time to destination -> 10s 4.5s 3s  3s  
speed               -> 1.  2.   2.  1
cars                -> c3  c2   c1  c4  
line                -> ----------------------
nums                -> 0 1 2 3 4 5 6 7 8 9 10


-> Object: Car { position: int, speed: int , time_to_destination() }
Steps:
 1. sorted cars by position
 2. Highest Position car will go first 
 3. If the next position car time to destination is less than the first car, then these become fleet.
 TC: O(n logn) --> because of sorting & SC: O(n)
 
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        