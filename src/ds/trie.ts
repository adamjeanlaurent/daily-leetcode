class TrieNode {
    children: Map<string, TrieNode>;
    isEnd: boolean;

    constructor(isEnd: boolean) {
        this.children = new Map();
        this.isEnd = isEnd;
    }
}

class Trie2 {
    private root: TrieNode;
    constructor() {
        this.root = new TrieNode(false);
    }

    // O(1)
    insert(word: string): void {
        let curPtr: TrieNode = this.root;

        for (const letter of word) {
            // if current node doesn't have an edge to the next letter of the word,
            // add a new node for that letter, and add a edge to it
            if (!curPtr.children.has(letter)) {
                curPtr.children.set(letter, new TrieNode(false));
            }

            // move curptr to existing or newly inserted node
            curPtr = curPtr.children.get(letter)!;
        }

        // curPtr at this point, points to the node at the end of the word, mark it as such
        curPtr.isEnd = true;
    }
    
    // O(1)
    search(word: string): boolean {
        let curPtr: TrieNode = this.root;
        
        for (const letter of word) {
            // if the current node doesn't have an edge to a node of the next letter,
            // then that means the word doesn't exist in the tree, as there is no path to it
            if (!curPtr.children.has(letter)) {
                return false;
            }

            // move curptr to next node
            curPtr = curPtr.children.get(letter)!;
        }

        // curPtr at this point, points to the node at the end of the word,
        // only return true if that node signifies the end of a word
        return curPtr.isEnd;
    }

    // O(1)
    startsWith(prefix: string): boolean {
        let curPtr: TrieNode = this.root;

        for (const letter of prefix) {
            // if the current node doesn't have an edge to a node of the next letter,
            // then that means the prefix doesn't exist in the tree, as there is no path to it
            if (!curPtr.children.has(letter)) {
                return false;
            }

            // move curptr to next node
            curPtr = curPtr.children.get(letter)!;
        }

        // return true, because if we got to this point, we found a path containing the prefix
        return true;
    }
}