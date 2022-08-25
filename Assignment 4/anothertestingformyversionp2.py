

class trie_alphabet_nodes:
    """
    Class for a linked array implementation. This is done to make implementation of the questions easier.
    """

    def __init__(self):
        self.dollar = False                 # Indicates if end of string
        self.next_letters = [None] * 26     # Array. Should be obvious what for.
        self.count = 0                      # Counts occurrences of string
        self.prefix_count = 0               # Counts for the number of strings with this as a prefix


class Trie:
    """
    Class for tries, as required in the questions, using linked arrays.
    """

    def __init__(self, timelines):
        """
        Initialising function for the trie

        @param self                 The trie we are creating
        @param text                 The text (strings list) we are inserting into the trie
        @complexity                 O(T) where T is the total length of the strings in the list combined
        """
        # Initialise the class
        self.root = trie_alphabet_nodes()

        # Call the insert method for each string:
        for stri in timelines:
            self.insert(stri)

    def insert(self, timelines):
        """
        Inserts strings into the trie

        @param self                 The trie we are referencing
        @param stri                 The text individual string we are inserting into the trie
        @complexity                 0(n) where n is the length of the string
        """
        # Start at the origin
        base = self.root
        base.prefix_count += 1

        # Iterate through all characters
        i = 0
        while i < len(timelines):
            char_num = int(ord(timelines[i]) - ord('a'))         # Convert charcter to a 0-25 index number

            # Test if need to add a 'child':
            if base.next_letters[char_num] == None:
                base.next_letters[char_num] = trie_alphabet_nodes()

            # Move down
            base = base.next_letters[char_num]
            base.prefix_count += 1

            # Iterate
            i += 1

        # Set end of word equal to true
        base.dollar = True
        base.count += 1

    def getLongestChain(self, noccurence):
        """
        Function that gets the number of times a prefix is in the trie

        @param self                     The trie we are referencing
        @param query_str                The text individual prefix we are searching for in the trie
        @return origin.prefix_count     The number of times a prefix is 'in' the referenced trie
        @complexity                     0(q) where q is the length of the prefix
        """
        # Start at the origin
        origin = self.root

        # Iterate through all characters
        i = 0
        while i < len(query_str):
            char_num = int(ord(query_str[i]) - ord('a'))  # Convert charcter to a 0-25 index number

            # Test if appropriate child doesn't exist:
            if origin.next_letters[char_num] == None:
                return 0

            # Move down
            origin = origin.next_letters[char_num]

            # Iterate
            i += 1

        # Return the prefix count at the final point:
        return origin.prefix_count

text = ["abc", "dbcef", "gdbc", "abcd"]
student_trie = Trie(text)
string_frequency = student_trie.prefix_freq("bc")
print(string_frequency)
string_frequency = student_trie.prefix_freq("abc")
print(string_frequency)