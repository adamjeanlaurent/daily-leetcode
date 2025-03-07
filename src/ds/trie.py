
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
