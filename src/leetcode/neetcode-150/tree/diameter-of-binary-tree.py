'''
    Link: https://leetcode.com/problems/diameter-of-binary-tree/

    Time Took: 17 Minutes

    Time Complexity: O(N) linear

    Space Complexity: O(N) linear

    Date: 02-02-2025

    Problem Type: Tree

    Solution Explained: Visit every node in the tree. At every node, to calculate the longest diameter running through the node, recurse left and right.
        The return value of the func should be the longest of left or right to support recursion, but use left and right in the func to check for deepest.

    Notes: I am no a big fan of defining func inside a func like a lot of python ppl do to reuse vars and avoid annoying params, tho I am a big fan of class Solutoin with member vars.
'''

# foo()
# visit node
# recurse left
# recurse right
# see if longest diam
# return right path length + left path length

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    deepest: int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameterOfBinaryTreeHelper(root)
        return self.deepest

    def diameterOfBinaryTreeHelper(self, node):
        if node is None:
            return 0

        leftDiam = self.diameterOfBinaryTreeHelper(node.left)
        rightDiam = self.diameterOfBinaryTreeHelper(node.right)

        diam = leftDiam + rightDiam

        self.deepest = max(self.deepest, diam)
        
        return 1 + max(leftDiam, rightDiam)


