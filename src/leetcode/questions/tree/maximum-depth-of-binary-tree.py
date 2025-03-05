'''
    Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

    Time Took: 11 Minutes.

    Time Complexity: O(N)

    Space Complexity: O(N)

    Date: 03/03/2025

    Problem Type: tree

    Solution Explained: start at root node. have helper func that has as a param the current depth. As you visit nodes you increment that param.
    So everytime you are at a node, you know it's depth, compare that depth to the res depth that lives on the class instance.

    Notes:
'''

'''
need to traverse the entire tree
count as we get deeper 

dfs or bfs?

s1:
    dfs
'''

class TreeNode:
    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val

from typing import Optional

class Solution:
    resDepth: int = 0
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        self.maxDepthHelper(root, 1)
        return self.resDepth
    
    def maxDepthHelper(self, root: Optional[TreeNode], currentDepth: int):
        if root == None:
            return

        self.resDepth = max(currentDepth, self.resDepth)

        self.maxDepthHelper(root.left, currentDepth + 1)
        self.maxDepthHelper(root.right, currentDepth + 1)
