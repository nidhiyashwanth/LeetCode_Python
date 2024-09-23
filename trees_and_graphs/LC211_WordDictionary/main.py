class WordNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = WordNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        self.res = False
        self.dfs(self.root, word)
        return self.res
    
    def dfs(self, node, word):
        if not word:
            if node.is_end_of_word:
                self.res = True
            return
        
        next_char = word[0]
        if next_char == ".":
            for child in node.children.values():
                self.dfs(child, word[1:])
        else:
            if next_char in node.children:
                self.dfs(node.children[next_char], word[1:])