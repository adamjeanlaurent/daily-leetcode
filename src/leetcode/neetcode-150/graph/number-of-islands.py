'''
    Link: https://leetcode.com/problems/number-of-islands/description/

    Time Took: 25 mins (I messed up and forgot to only add to queue if land)

    Time Complexity: O(M x N), scales with size of grid

    Space Complexity: O(L), scales with amount of land, not grid, even with HUGE grid, if so land, no memory used

    Date: 02-02-2025

    Problem Type: graph

    Solution Explained: Use BFS, loop through matrix, when you see land, start BFS. BFS will find all adjacent land, to avoid cycles. looks in all 4 directions to find adjacent land.

    Notes: python while queue: will stop when queue is empty, use deque for a queue, has .append and .popleft, tuples are nice for dirs, since you can loop through easily.
'''

from collections import deque
from typing import List

LAND='1'
WATER='0'

dirs = [
    (0, -1),
    (0, 1),
    (1, 0),
    (-1, 0),
]

class Solution:
    grid = []
    rows = 0
    cols = 0

    def bfs(self, startRow, startCol):
        queue = deque([(startRow, startCol)])

        while queue:
            row, col = queue.popleft()

            for rowShift, colShift in dirs:
                newRow, newCol = row + rowShift, col + colShift

                if newCol >= 0 and newCol < self.cols and newRow >= 0 and newRow < self.rows:
                    if self.grid[newRow][newCol] == LAND:
                        self.grid[newRow][newCol] = WATER
                        queue.append((newRow, newCol))


    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        islands = 0

        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == LAND:
                    self.bfs(row, col)
                    islands += 1

        return islands
