/*
    Link: https://leetcode.com/problems/implement-trie-prefix-tree/description/

    Time Took: 35 Minutes 

    Time Complexity: 
        - addWord(): O(N)
        - search(): O(N)

    Space Complexity:
        - O(N), space for the trie itself

    Solution Explained:
        - Use a trie.
        - addWord() is the sample as a regular trie insert.
        - search() is similar to a regular trie search, with the caveat of '.'.
            When '.' is encountered, the only option is to now attempt to replace the '.' with every possibility until you find a path the sufficies.
*/

class TrieNode2 {
    children: Map<string, TrieNode2> = new Map();
    isEnd: boolean = false;
}

class WordDictionary {
    trie: TrieNode2 = new TrieNode2();

    constructor() {

    }

    addWord(word: string): void {
        let curPtr: TrieNode2 = this.trie;

        for (const letter of word) {
            if (!curPtr.children.has(letter))
                curPtr.children.set(letter, new TrieNode2());

            curPtr = curPtr.children.get(letter)!;
        }

        curPtr.isEnd = true;
    }

    search(word: string): boolean {
        return this.searchHelper(this.trie, word);
    }

    searchHelper(node: TrieNode2, word: string): boolean {
        let curPtr: TrieNode2 = node;

        for (let i = 0; i < word.length; i++) {
            const letter: string = word[i];

            if (letter === '.') {
                // fork
                for (const childNode of curPtr.children.values()) {
                    if (this.searchHelper(childNode, word.substring(i)))
                        return true;
                }

                return false;
            }

            if (!curPtr.children.has(letter))
                return false;

            curPtr = curPtr.children.get(letter)!;
        }

        return curPtr.isEnd;
    }
}
