"""
Name: Soh En Ming
Student ID: 3224975
Title: FIT2004 S1/2022: Assignment 1
Unit Code: FIT2004

This assignment was done on Python Version 3.9.2.
"""

"""
1 Partial Wordle Trainer (5 marks + 1 mark for documentation)
"""
def trainer(wordlist, word, marker):
    """
    This function take inputs which are wordlist, word and marker then compute them together to produce a list
    which contains the predicted word based on the wordlist given and the marker of which characters from the word
    you wrote is correct.
    Written by Soh En Ming

    Precondition: A list of words given, a word written by the user and lastly a marker which has inputs of 0
    and 1 and shows whether the letter of the word is correct or is not in the right spot.
    Postcondition: A list of predicted words matches which has been identified from the wordlist given.

    Input:
        wordlist: wordlist = ["costar", "carets", "recast", "traces", "reacts", "caster", "caters",
                            "crates", "actors", "castor"]
        word: "catrse"
        marker: [1, 1, 0, 0, 0, 0]
    Return:
        answer: ["carets", "caster"]

    Time complexity:
        Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
        complexity will be the same.
        Worst: O(NM). How I ended up with O(NM) time complexity is through a combinations of different code
        complexities. Firstly, there is a for loop to fill up the word array which has a complexity of O(n), n being
        the complexity from the length of word. The other for loop has a complexity of O(NM) from the first for loop
        and the for loop within the for loop. Then there's another for loop which is to sort the answer to
        lexigraphical order. In that for loop the total complexity is O(MN) since it calls teh function count sort
        which has a complexity of O(n). In total, the worse case complexity of this function is O(NM).
    Space complexity:
        Input: O(NM)
        Aux: O(N) because of the list created despite being empty and then being appended later with elements into
        the list created.
    """
    wordLength = len(word)
    wordlistLength = len(wordlist)
    markerLength = len(marker)
    valid_words = []
    numLtrWord = [0] * 26 # for the number of letters in a alphabet

    for n in range(wordLength):
        numLtrWord[ord(word[n]) - 97] += 1

    # for loop to check whether the wordlist matches the word based on the marker value
    for n in range(wordlistLength):
        numLtrWordList = counter(wordlist[n])
        if numLtrWordList == numLtrWord:
            correct_word = True
            for idx in range(markerLength):
                if marker[idx] == 0 and wordlist[n][idx] == word[idx]:
                    correct_word = False
                elif marker[idx] == 1 and wordlist[n][idx] != word[idx]:
                    correct_word = False
            if correct_word:
                valid_words.append(wordlist[n])

    # counting sort to make sure the words are arranged in lexicographic order
    for n in range(markerLength):
        if marker[markerLength - 1 - n] == 0:
            valid_words = non_comparison_sort(valid_words, markerLength - 1 - n)
    return valid_words

def non_comparison_sort(wordlist, idx):
    """
        This function is one of my implementations for a non comparison sort which is counting sort. What this
        function does is to sort the order of the wordlist to be in lexicographical order.
        Written by Soh En Ming

        Time complexity:
            Best: As seen in the code below, there is no fast exit in this function therefore, the best and worst
            case of this function is the same.
            Worst: The worst case time complexity is O(n). The reason for this is because there's for loops being used
            for e.g. to fill up the count array you need to use a for loop which has a complexity of O(n), n for the
            length of the wordlist. Similarly for other codes in this function which are also for loop have O(n)
            time complexity and since there's no for loop within a for loop and the codes don't take much time
            complexity, the final worse case time complexity for this function is O(n).

        Space complexity:
            Input: O(1)
            Aux: O(1)
        """
    ASCIIForSmallLetters = 97
    wordlist_length = len(wordlist)
    num_alphabet_letters = 26

    count = [0] * num_alphabet_letters
    for ncs in range(wordlist_length):
        count[ord(wordlist[ncs][idx]) - ASCIIForSmallLetters] += 1

    position = [0] * num_alphabet_letters
    for ncs in range(1, num_alphabet_letters):
        position[ncs] = count[ncs - 1] + position[ncs - 1]

    # filling the output array
    output = [0] * wordlist_length
    for ncs in range(wordlist_length):
        output[position[ord(wordlist[ncs][idx]) - ASCIIForSmallLetters]] = wordlist[ncs]
        position[ord(wordlist[ncs][idx]) - ASCIIForSmallLetters] += 1

    return output

def counter(word):
    """
        What this function does is go through every single letter in the respective word chosen and change each
        letter in the word into increments of one and store it into the counter
        Written by Soh En Ming

        Precondition: A string which contains the word you want to change into a counter
        Postcondition: A list which contains a counter for the word that ranges from a to z

        Time complexity:
            Best: There is no fast exit, therefore both best and worst case are the same.
            Worst: O(M). The reason for this choice is because there is a for loop used which went through the
            length of the word giving O(M) where M is the length of the word.

        Space complexity:
            Input: O(1)
            Aux: O(1). The array that has been created is a fixed sized so the aux is O(1)
        """
    count = [0] * 26
    for n in range(len(word)):
        # the -97 is because the ascii small a is on 97 so to make it 0 it has to minus.
        count[ord(word[n]) - 97] += 1
    return count

"""
2 Finding a Local Maximum (3 + 1 marks for documentation)
"""
def local_maximum(M):
    """
        This function takes a N by N grid as input and uses divide and conquer to find the local maximum in the
        N by N matrix and return the row and column of where the local maximum is located within the N by N matrix.
        Written by Soh En Ming

        Precondition: Takes a N by N matrix as input
        Postcondition: Computes and returns a list that contains row index and column index of where the local
        maximum is at.

        Input: M = [[1, 2, 27, 28, 29, 30, 49],
                    [3, 4, 25, 26, 31, 32, 48],
                    [5, 6, 23, 24, 33, 34, 47],
                    [7, 8, 21, 22, 35, 36, 46],
                    [9, 10, 19, 20, 37, 38, 45],
                    [11, 12, 17, 18, 39, 40, 44],
                    [13, 14, 15, 16, 41, 42, 43],
                    [13, 14, 15, 16, 41, 42, 43]]
        Return:
            answer: [0, 6]

        Time complexity:
            Best: Since there's no fast exit, the best case complexity and the worse will be the same.
            Worst: O(n). Looking at the code below, the function below calls functions from findMaxColIndex or
            findMaxRowIndexNeighborhood and both of those functions have O(n) complexity. However, since function
            is within the same while loop and not within each other. The total complexity only adds up to be O(n)
        Space complexity:
            Input: O(n)
            Aux: O(1)
        """
    matrix_length = len(M)
    topRowIdx = 0
    bottomRowIdx = matrix_length - 1
    while topRowIdx <= bottomRowIdx:
        # finding the middle row in the matrix
        midRowIdx = topRowIdx + (bottomRowIdx - topRowIdx) // 2
        # finding the column index that contains the local maximum
        maxColIdx = findMaxColIndex(M[midRowIdx])
        # finding the row index that contains the local maximum
        maxRowIdx = findMaxRowIndexNeighborhood(M, midRowIdx, maxColIdx)
        # using both the values calculated above to get the value of the final answer which is the row idx and col idx
        if maxRowIdx == midRowIdx:
            return [maxRowIdx, maxColIdx]
        elif maxRowIdx < midRowIdx:
            bottomRowIdx = midRowIdx - 1
        else:
            topRowIdx = midRowIdx + 1

def findMaxRowIndexNeighborhood(M, middleRow, maxColIndex):
    """
        This function is used to find the row in the matrix where the local maximum is located. How it works is
        through comparing values of the number above and below to determine which is larger and ultimately finding
        which row index the local maximum is located.
        Written by Soh En Ming

        Parameter: A N by N matrix that contains integers, a integer containing the index for the middle row in
        the matrix and lastly a integer value which contains the max coloumn index of the local minimum

        Returns: The function will return a integer which contains the row index that contains the local maximum

        Time complexity:
            Best: O(n). Despite there being more a lot of if loops which will compute a complexity of O(1), this
            function uses max() which has a complexity of O(n).
            Worst: O(n). There is no for loop in this function, and there isn't any loops that will increase the
            complexity. The only function that stops this from being a O(1) complexity is the max() function which
            will always be O(n) complexity since it needs to check every element.
        Space complexity:
            Input: O(n)
            Aux: O(1)
    """
    matrix_length = len(M)
    valueBelow, valueAbove = float('-inf'), float('-inf')
    valueMiddle = M[middleRow][maxColIndex]

    if middleRow - 1 >= 0:
        valueBelow = M[middleRow - 1][maxColIndex]

    if middleRow + 1 <= matrix_length:
        valueAbove = M[middleRow + 1][maxColIndex]

    # checking between the values above and below to see which row index contains the local maximum
    maxValue = max(valueMiddle, valueBelow, valueAbove)
    if maxValue == valueMiddle:
        return middleRow
    elif maxValue == valueBelow:
        return middleRow - 1
    else:
        return middleRow + 1


def findMaxColIndex(M):
    """
        This function is used to find the column index in the matrix that contains the largest local maximum. It
        uses enumerate to look through the matrix M and then compare with the max element. Which then after the for
        loop has finished, the max column index has been found.
        Written by Soh En Ming

        Parameter: A N by N matrix that contains integers starting at the middle row index.

        Returns: The function will return a integer containing the column index where the local maximum is stored

        Time complexity:
            Best: There is no best case in this function, as there is no fast exits within the function which could
            give it a different time complexity
            Worst: O(n). This mostly comes from the enumerate function which takes O(n) time complexity.
        Space complexity:
            Input: O(1). Since the space can be reused
            Aux: O(1)
    """
    maxRow = 0
    maxElement = float('-inf')
    # finding the column index that contains the local maximum
    for idx, value in enumerate(M):
        if value > maxElement:
            maxElement = value
            maxRow = idx
    return maxRow

