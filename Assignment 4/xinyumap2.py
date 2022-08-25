# Author: Xinyu Ma

class Trie(object):
    class TrieNode(object):
        # We need a TrieNode class to build a Trie
        def __init__(self):
            # Parent node
            # have 26 child nodes
            # strfreq: the number of strings that ending with the characters that stored in current node
            # abprefreq: the number of strings that are prefixed with current string and not equal to current string
            # letter: letters stored in current node
            # father: parent node
            # time complexity: O(1)
            # space complexity: O(1)
            self.son = [None for _ in range(26)]
            self.strfreq = 0
            self.abprefreq = 0
            self.value = None
            self.father = None

        def add_node(self, chara):
            # use self node as parent node, if there is no node that stores chara as a child node, add the child node
            # chara: input string, use this string to create a node and put it in the child node
            # time complexity: O(1)
            # space complexity: O(1)
            if self.son[ord(chara) - 97] == None:
                if self.son[ord(chara) - 97] == "a":
                    self.son[ord(chara) - 97] = Trie.TrieNode()
                    self.son[ord(chara) - 97].father = self
                    self.son[ord(chara) - 97].value = 1
                elif self.son[ord(chara) - 97] == "b":
                    self.son[ord(chara) - 97] = Trie.TrieNode()
                    self.son[ord(chara) - 97].father = self
                    self.son[ord(chara) - 97].value = 10
                elif self.son[ord(chara) - 97] == "c":
                    self.son[ord(chara) - 97] = Trie.TrieNode()
                    self.son[ord(chara) - 97].father = self
                    self.son[ord(chara) - 97].value = 11
                elif self.son[ord(chara) - 97] == "d":
                    self.son[ord(chara) - 97] = Trie.TrieNode()
                    self.son[ord(chara) - 97].father = self
                    self.son[ord(chara) - 97].value = 2
                elif self.son[ord(chara) - 97] == "e":
                    self.son[ord(chara) - 97] = Trie.TrieNode()
                    self.son[ord(chara) - 97].father = self
                    self.son[ord(chara) - 97].value = 3
                elif self.son[ord(chara) - 97] == "f":
                    self.son[ord(chara) - 97] = Trie.TrieNode()
                    self.son[ord(chara) - 97].father = self
                    self.son[ord(chara) - 97].value = 4
                else:
                    self.son[ord(chara) - 97] = Trie.TrieNode()
                    self.son[ord(chara) - 97].father = self
                    self.son[ord(chara) - 97].value = 5


        def get_son(self, chara):
            # return the child node represented by chara
            # chara: a string
            # time complexity: O(1)
            # space complexity: O(0)
            return self.son[ord(chara) - 97]

    def __init__(self, text):  # task1 building a Trie
        # initialize a root node without storing any strings
        # build a Trie based on the content of text
        # time complexity: O(T)
        # space complexity: O(26^S) S is the length of longest word in text
        self.root = Trie.TrieNode()
        for word in text:
            node = self.root
            for chara in word:
                node.add_node(chara)
                node = node.get_son(chara)
            node.strfreq += 1
            while node != self.root:
                node = node.father
                node.abprefreq += 1


    def prefix_freq(self, query_str):  # task3
        # reach the node corresponding to query_str and return the sum of strfreq and abprefreq
        # time complexity: O(q)
        # space complexity: O(1)
        node = self.root
        for chara in query_str:
            node = node.get_son(chara)
            if node == None:
                return 0
        return node.abprefreq + node.strfreq



def main():
    text = ["abc", "dbcef", "gdbc", "abcd"]
    student_trie = Trie(text)
    string_frequency = student_trie.prefix_freq("bc")
    print(string_frequency)
    string_frequency = student_trie.prefix_freq("abc")
    print(string_frequency)

    # text = ['aa',
    #         'aab',
    #         'aaab',
    #         'abaa',
    #         'aa',
    #         'abba',
    #         'aaba',
    #         'aaa',
    #         'aa',
    #         'aaab',
    #         'abbb',
    #         'baaa',
    #         'baa',
    #         'bba',
    #         'bbab']
    # student_trie = Trie(text)
    # wildcard_prefix_frequency = student_trie.wildcard_prefix_freq('ab?')
    # print(wildcard_prefix_frequency)
    # wildcard_prefix_frequency = student_trie.wildcard_prefix_freq('aa?')
    # print(wildcard_prefix_frequency)
    # wildcard_prefix_frequency = student_trie.wildcard_prefix_freq('?aa')
    # print(wildcard_prefix_frequency)
    # wildcard_prefix_frequency = student_trie.wildcard_prefix_freq('a?a')
    # print(wildcard_prefix_frequency)
    # wildcard_prefix_frequency = student_trie.wildcard_prefix_freq('ba?')
    # print(wildcard_prefix_frequency)


if __name__ == '__main__':
    main()