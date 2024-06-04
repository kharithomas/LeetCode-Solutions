class TrieNode:
    """A single node of a Trie"""

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Inserts a new TrieNode()"""

        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """Finds if a word exists in the Trie"""

        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix):
        """Finds if any existing word has the prefix"""

        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == "__main__":
    trie = Trie()

    trie.insert("apple")
    print(trie.search("apple"))     # True
    print(trie.search("app"))       # False
    print(trie.startsWith("app"))   # True

    trie.insert("app")
    print(trie.search("app"))       # True
