#from https://albertauyeung.github.io/2020/06/15/python-trie.html/
from io import *
import time as tm
class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a counter indicating how many times a word is inserted
        # (if this node's is_end is True)
        self.counter = 0

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}

class Trie(object):
    """The trie object"""

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")
    
    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            char = word[i]
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found, create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        # Mark the end of a word
        node.is_end = True

        # Increment the counter to indicate that we see this word once more
        node.counter += 1
        
    def dfs(self, node, prefix):
        """Depth-first traversal of the trie
        
        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))
        
        for child in node.children.values():
            self.dfs(child, prefix + node.char)
        
    def query(self, x):
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of 
        times they have been inserted
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        self.output = []
        node = self.root
        
        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []
        
        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)


def test():
    filename = 'Guiao5\palavras2.txt'

    option = input('Menu--------\n1 - search a word\npress enter to exit\n')
    while option !='':
        if int(option) ==1:
            toResearch = input('Word to research: ')
            t = Trie()
            iT = tm.time()
            with open(filename,'r',encoding='utf-8') as file:
                
                #words = list(x.replace('\n','') for x in file.readlines()) # other way 
                #print(words)
                #for word in words :
                #    t.insert(word)
                word = file.readline().replace('\n','')
                while word!='':
                    t.insert(word)
                    word = file.readline()[:-1]
            
            researched = t.query(toResearch)
            print(researched)
            fT = tm.time()
            tt = fT-iT
            print(f'done in {tt} seconds')
            option = input('Menu--------\n1 - search a word\npress enter to exit\n')
    print('bye')


if __name__ == "__main__":
    test()