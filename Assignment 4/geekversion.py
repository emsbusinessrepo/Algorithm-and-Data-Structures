# Python3 implementation of counting the
# number of words in a trie with a
# given prefix

# Trie Node
class TrieNode:

    def __init__(self):
        # Using map to store the pointers
        # of children nodes for dynamic
        # implementation, for making the
        # program space efficient
        self.children = dict()

        # If isEndOfWord is true, then
        # node represents end of word
        self.isEndOfWord = False

        # num represents number of times
        # a character has appeared during
        # insertion of the words in the
        # trie
        self.num = dict()


# Declare root node
root = None


# Function to create New Trie Node
def getNewTrieNode():
    pNode = TrieNode()
    return pNode


# Function to insert a string in trie
def insertWord(word):
    global root

    # To hold the value of root
    current = root

    # To hold letters of the word
    s = ''

    # Traverse through strings in list
    for i in range(len(word)):
        s = word[i]

        # If s is not present in the
        # character field of current node
        if (s not in current.children):

            # Get new node
            p = getNewTrieNode()

            # Insert s in character
            # field of current node
            # with reference to node p
            current.children[s] = p

            # Insert s in num field
            # of current node with
            # value 1
            current.num[s] = 1
        else:

            # Increment the count
            # corresponding to the
            # character s
            current.num[s] = current.num[s] + 1

        # Go to next node
        current = current.children[s]

    current.isEndOfWord = True


# Function to count the number of
# words in trie with given prefix
def countWords(words, prefix):
    global root
    root = getNewTrieNode()

    # Size of list of string
    n = len(words)

    # Construct trie containing
    # all the words
    for i in range(n):
        insertWord(words[i])

    current = root
    s = ''

    # Initialize the wordCount = 0
    wordCount = 0

    for i in range(len(prefix)):
        s = prefix[i]

        # If the complete prefix is
        # not present in the trie
        if (s not in current.children):
            # Make wordCount 0 and
            # break out of loop
            wordCount = 0
            break

        # Update the wordCount
        wordCount = (current.num)[s]

        # Go to next node
        current = (current.children)[s]

    return wordCount


# Driver Code
if __name__ == '__main__':
    # input list of words
    words = ["abc", "dbcef", "gdbc"]

    # Given prefix to find
    prefix = "bc"

    # Print the number of words with
    # given prefix
    print(countWords(words, prefix))

# This code is contributed by rutvik_56

