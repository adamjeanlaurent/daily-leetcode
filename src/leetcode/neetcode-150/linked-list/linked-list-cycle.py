'''
    Link: https://leetcode.com/problems/linked-list-cycle/

    Time Took: 20 Minutes

    Time Complexity: O(N)

    Space Complexity: O(1)

    Date: 02/26/2025

    Problem Type: linked-list

    Solution Explained: Use a fast and slow ptr approach. Essentially have a slow ptr that moves 1 step each time, and a fast ptr that moves 2 steps each time. If the fast ptr every reaches the end of the list or becomes null, then that means that there is no cycle. If slow and fast ptr meet (which may take a couple rounds but I guess is guarneteed, then there is a cycle.

    Notes:
'''


'''
return bool if cycle

cycle = list nevers ends, a.k.a: at least one node's next ptr puts you backward in the list

sol 1:
- walk list
- store memory address of nodes you've seen
- if the list eventually ends, no cycle
- if you visit a node you've seen before, there is cycle

time: O(N)
space: O(N)

sol 2:
- slow ptr moves 1 step
- fast ptr moves 2 steps

- if fast ptr reaches end, no cycle
- if fast ptr and slow ptr meet, cycle

3 -> 2 -> 0 -> -4

sp:-4
fp:-4

time: O(N)
space: O(1)
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode):
        if head == None or head.next == None:
            return False

        slowPtr = head
        fastPtr = head

        while fastPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

            if slowPtr == fastPtr:
                return True

        return False


