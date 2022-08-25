from typing import Tuple

class TrieNode:
    """
    This class implements the node of a Trie
    """
    def __init__(self):
        self.child = [None] * 26
        self.terminator = False

class Trie(object):
    """
    Purpose: use tree heirarchy to quickly add/retrieve characters from words.
    Input: character, string, prefix  
    Output: matching char, string, prefix if found
    """

    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Turns true when end of word is reached
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.counter = 1

    def getNode(self):
        """
        this method returns an TrieNode object
        @param: none
        @return: a TrieNode object
        @time-complexity: O(1)
        @space-complexity: O(1)
        """
        return TrieNode()


    def add(self, word: str):
        """
        Add word to Trie, character-wise
        If character exists point node to child
        If char not exists recursively call class to make new char in node
        Add whole word to Trie.
        """
        self.root =
        for char in word:
            found_in_child = False
            # Search for the character in the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # We found it, increase the counter by 1 to keep track that another
                    # word has it as well
                    child.counter += 1
                    # And point the node to the child that contains this char
                    node = child
                    found_in_child = True
                    break
            # We did not find it so add a new chlid recursively
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                # And then point node to the new child
                node = new_node
        # Everything finished. Mark it as the end of a word.
        node.word_finished = True


    def find_prefix(self, prefix: str):
        """
        Check and return
          1. If the prefix exsists in any of the words we added so far
          2. If yes then how may words actually have the prefix
        """
        node = root
        # If the root node has no children, then return False.
        # Because it means we are trying to search in an empty trie
        if not root.children:
            return False, 0
        for char in prefix:
            char_not_found = True
            # Search through all the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # We found the char existing in the child.
                    char_not_found = False
                    # Assign node as the child containing the char and break
                    node = child
                    break
            # Return False anyway when we did not find a char.
            if char_not_found:
                return False, 0
        # Well, we are here means we have found the prefix. Return true to indicate that
        # And also the counter of the last node. This indicates how many words have this
        # prefix
        return True, node.counter


if __name__ == "__main__":
    text = ["abc", "dbcef", "gdbc"," abcd"]
    student_trie = Trie(text)

    print(student_trie.find_prefix("ab"))


'''main steps
1. add function, inputs root node (no char assigned to it), and the whole word.
2. iterate through the word, character-wise, starting with first char
3. check if current 'node' (points to root at beginning) has a child node with that char
4. check if found increment counter, indicate it has repeated occurence of the char
5. check if not found, add new node as child of current node
6. assign child node as current node, which means next iteration will start from here, before it starts with next character of the word. 
7. mark end of word as finished word True

searching for prefix
1. start with root node and prefix word to search for
2. for each character search through children of current node (start at root with no char), searches by level (bfs?)
3. check if found and point (reassign) current node to child node
4. if not found, return False to indicate prefix doesn't exist.
5. handle case where prefix is bigger than word
'''