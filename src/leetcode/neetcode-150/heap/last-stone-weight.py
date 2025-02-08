'''
    Link: https://leetcode.com/problems/last-stone-weight/description/

    Time Took: 17 minutes

    Time Complexity: O(log n)

    Space Complexity: O(n)

    Date: 02-08-2025

    Problem Type: heap

    Solution Explained: essentially this problem boils down to, you want to maintain a sorted list of numbers. you are constanly editing a couple of those numbers and re-inserting them back into the list. this type of operation is great for a heap. use a max heap, insert all stones into it, while the heap still has at least 2 elements, pull the first 2 (larget 2), do the smashing, and insert back into heap if non equal stones.
    
    Notes: python doesn't seem to support max heap technically. heapq is by nature a min heap, but you can trick it into being a max heap by making all the elements negative. also pythton ternary support is nice, unlike tradional ternary, the condition goes second. it's like x if y else z.
'''

# each turn pick 2 heaviest stones (x,y)
# if x == y, destroyed both stones
# if x < y, smash them together, y = y - x
# at the end there is only 1 stone left

# heap
# max heap, since you're picking 2 largest elements

'''
foo(stones):
    maxHeap = heapify(stones)
    
    while len(maxHeap) > 1:
        y = maxHeap.pull()
        x = maxHeap.pull()

        if x != y
            put y - x back in heap

    return last element
'''

import heapq
def lastStoneWeight(stones):
    maxHeap = []

    for stone in stones:
        heapq.heappush(maxHeap, -stone)

    while len(maxHeap) > 1:
        largest = abs(heapq.heappop(maxHeap))
        nextLargest = abs(heapq.heappop(maxHeap))

        if largest != nextLargest:
            largest = largest - nextLargest
            heapq.heappush(maxHeap, largest)
    
    return abs(maxHeap[0]) if len(maxHeap) == 1 else 0

