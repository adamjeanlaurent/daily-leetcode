
'''
    Link: https://leetcode.com/problems/min-stack/description/

    Time Took: 15 minutes

    Time Complexity: O(1)

    Space Complexity: O(N), N = number of insertions. Techincally, O(2N) since duplicating elements in 2 stacks.
    
    Date: 02-02-2025

    Problem Type: Stack

    Solution Explained: Have a second stack for the minimum value at each point, you need this so that you can instanly know the current minimun, and keep the current minimum up to date on removals (espically) and insertions.

    Notes: python's last elem in list syntax is nice.
'''

# regular stack, with a get min operation

# option 1: store min in member var
# in insertion, update min var
# doesn't work on removal, you'd have to recompute

# when you remove min, get the previous min. Stack?

# option 2: 2nd stack for min

# option 2a: only push onto stack 2 when new min
# s1: [1,2,0,3,4,5,0] s2: [1,0]
# won't work cuz could be duplicates

# option 2b: always push on stack 2 on insertion
# s1: [1,2,0,3,4,5,0] s2: [1,1,0,0,0,0]
# always remove from s2 when remove s1
# always insert s2 when insert s1

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minStack) == 0:
            self.minStack.append(val)

        else:
            self.minStack.append(min(val, self.minStack[-1]))


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

