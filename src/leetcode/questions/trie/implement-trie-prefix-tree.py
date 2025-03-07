'''
    Link: https://leetcode.com/problems/implement-trie-prefix-tree/

    Time Took: 13 mins

    Time Complexity: search O(N), insert O(N), startWith O(N)

    Space Complexity: O(N)

    Date: 03/07/2025

    Problem Type: trie

    Solution Explained: Is sort of like a tree. Each node has a map of map<string, node> and isEnd.

    Notes:
'''

class Node:
    def __init__(self):
        self.childen = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        curPtr = self.root
        for letter in word:
            if letter not in curPtr.childen:
                curPtr.childen[letter] = Node()

            curPtr = curPtr.childen[letter]

        curPtr.isEnd = True


    def search(self, word: str) -> bool:
        curPtr = self.root
        for letter in word:
            if letter not in curPtr.childen:
                return False

            curPtr = curPtr.childen[letter]

        return curPtr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curPtr = self.root
        for letter in prefix:
            if letter not in curPtr.childen:
                return False

            curPtr = curPtr.childen[letter]

        return True
