
class TrieNode:
    def __init__(self):
        self.children = TrieChildren()  # Custom data structure for children nodes
        self.is_word = False  # end of word


class TrieChildren:
    def __init__(self):
        self.characters = []  # key
        self.nodes = []  # value, the child node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            index = -1  # see if it is not found
            if char in node.children.characters:
                index = node.children.characters.index(char)  # update to the corresponding child node
            if index == -1:  # if not found
                new_node = TrieNode()
                node.children.characters.append(char)
                node.children.nodes.append(new_node)
                node = new_node
            else:
                node = node.children.nodes[index]
        node.is_word = True  # end of word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            index = -1
            if char in node.children.characters:
                index = node.children.characters.index(char)
            if index == -1:
                return False
            else:  # index != -1
                node = node.children.nodes[index]  # update the node to the child node
        return node.is_word  # the last node of the word meaning if True, it is found in Trie
