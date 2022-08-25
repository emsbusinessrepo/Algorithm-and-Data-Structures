"""
Name: Soh En Ming
Student ID: 32024975
Title: FIT2004 S1/2022: Assignment 4
Unit Code: FIT2004

This assignment was done on Python Version 3.9.2.
"""

"""
1 Sleepless Sysadmins (4 marks + 1 mark for documentation)
"""


def ford_fulkerson_algorithm(flow_g, src, t, spaces, s_adm_p_n, ttl_admin):
    """
        This function is one of my implementations for ford_fulkerson_algorithm. This function is a helper function for
        the function allocate. What this function does is that it is used to find the flow, starting from the intial
        flow to the augmenting path that is used to sink and follow the path flow to find a found path and a flow which
        uses the least residual capacity following the path and returning the maximum flow. This algorithm also
        uses breath_first_search which it calls when implementing the ford_fulkerson_algorithm.
        Written by Soh En Ming and inspired/referenced the code from
        https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/

        Time complexity:
            Best: As seen in the code below, there is no fast exit in this function therefore, the best and worst
            case of this function is the same.
            Worst: O(n^2). The Reason for this complexity is because in the function, although there is a lot of for
            loops which has been used, the highest complexity from the for loop is only an O(n^2) this is because there
            is only one situaiton where the for loop is within another for loop. Another case would be the calling of
            the bfs algorithm. Although the bfs algorithm is O(n) compelxity, the functions called within only can have
            a total of O(n) complexity where the n comes form the length of flow_g[prnt[x]] and that the for loop which
            has a O(n) complexity is not in the same loop as the while loop which contains the bfs algorithm. Therefore,
            the highest complexity will only total up to O(n^2).

        Space complexity:
            Input: O(n^2)
            Aux: O(n^2). This is because the there is new spaces being added like the start where an array was created
            or the modification of the array in the different loops.
    """
    # initialisation variables
    flow_g_length = len(flow_g)
    issuing = [ttl_admin * [0]]
    prnt = flow_g_length * [-1]
    m_flw = 0

    for n in range(spaces - 1):
        issuing.append(ttl_admin * [0])
    while breath_first_search(flow_g, src, t, prnt):
        # Maximum flow through the path found
        x = t
        p_flw = float("Inf")
        while src != x:
            idx = None
            for n_ind in range(len(flow_g[prnt[x]])):
                if flow_g[prnt[x]][n_ind][0] == x:
                    idx = n_ind
            p_flw = min(p_flw, flow_g[prnt[x]][idx][1])
            x = prnt[x]
        m_flw += p_flw
        # reverse edges along the path
        y = t
        while src != y:
            o = prnt[y]
            idx_y = None
            for n_ind in range(len(flow_g[o])):
                if flow_g[o][n_ind][0] == y:
                    idx_y = n_ind
            flow_g[o][idx_y][1] -= p_flw
            idx_o = None
            for n_ind in range(len(flow_g[y])):
                if flow_g[y][n_ind][0] == o:
                    idx_o = n_ind
            flow_g[y][idx_o][1] += p_flw
            y = prnt[y]
    if m_flw == s_adm_p_n * spaces:
        for n_ind in range(ttl_admin):
            # Issuing spaces and occupying them
            for a_ind, a_val in flow_g[2 + n_ind]:
                if a_ind != 2 + n_ind + ttl_admin and a_val == 0:
                    index = a_ind - (2 + 2 * ttl_admin)
                    issuing[index][n_ind] = 1
            for e_ind, e_val in flow_g[n_ind + 2 + ttl_admin]:
                if e_ind != 2 + n_ind and e_val == 0:
                    index = e_ind - (2 + 2 * ttl_admin)
                    issuing[index][n_ind] = 1
    else:
        issuing = None
    return issuing


def breath_first_search(flow_g, s_vtrx, ttl_admin, prnt):
    """
        This function is one of my implementations for breath_first_search algorithm. This function is a helper function
        for ford_fulkerson_algorithm. What this function does is that it will return the path from the s_vrtx and also
        sink the ttl_admin and find the values of parnt[] with the storage of the path.
        Written by Soh En Ming and inspired/referenced the code from
        https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/

        Time complexity:
            Best: As seen in the code below, there is no fast exit in this function therefore, the best and worst
            case of this function is the same.
            Worst: O(n^2). The Reason for this complexity is because in the function, there is the use of while loop
            which in this case does not iterate faster therefore, the complexity will be O(V) where n is the s_vrtx
            values. After that a for loop is used which has a complexity of O(n) where n is the value of flow_g[x].
            After the combination of the complexities, the total complexity will be O(V+n) where V is the number of
            nodes and n is the number of edges. The final comlexity will be O(n) since if V+n the total complexity will
            only be O(n) or O(V) in this case I choose O(n)
            is used which uses

        Space complexity:
            Input: O(1)
            Aux: O(n). This is because there is new space being added.
    """
    # referenced from https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
    # Instantiation of variables
    q = []
    vstd = len(flow_g) * [False]
    vstd[s_vtrx] = True
    q.append(s_vtrx)

    while q:
        x = q.pop(0)
        # Assimilate all adjacent vertices of the dequeued vertex
        for idx, val in flow_g[x]:
            if 0 < val and vstd[idx] == False:
                q.append(idx)
                prnt[idx] = x
                vstd[idx] = True
                if ttl_admin == idx:
                    return True
            else:
                pass
    # Unable to reach sink
    return False

def allocate(preferences, sysadmins_per_night, max_unwanted_shifts, min_shifts):
    """
        This function takes inputs which is a set of array which is the preferences, a integer value which represents
        the min_shifts, a integer value which represents max_unwanted_shifts and lastly a integer value which represents
        the sys_admins_per_night which will be computed inside the function to create a list of list called allocation.
        The approach I've taken is to use helper functions, to take the inputed values from allocate function and
        conpute them in different helper functions to help get the final solution I wanted. In this case, I implemented
        ford_fulkerson_algorithm which is helpful in taking the values of preferences, sysadmins_per_night,
        max_unwanted_shifts and min_shifts to help compute to find which is the possible flow whic contains the minimum
        residual capacity which is the maximum flow and the final answer in a list of list. However, to get the
        correct specifed inputs to be used in the helper functions, I created the different rows of nodes based on
        the different preferences and the input values.
        Written by Soh En Ming

        Precondition: A set of array which is the preferences[i][j], the values for i is the number of people who are
        interested in working at night shift, the values for j is the number of unwanted shifts. The next precondition
        is a 3 separate input integer values. The first shows the number of minimum shifts, the next is to show the
        maximum number of unwanted shifts and lastly it is to show the number of system administrators that would be
        there per night.
        Postcondition: Returns either a Python NoneType due to the constraints not being satasfied or a list of list
        which should be either 1 or 0 depending on the inputted values.

        Input:
            preferences:  [[0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                           [1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                           [0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
                           [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
                           [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
                           [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
                           [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                           [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                           [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
                           [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                           [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                           [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
                           [0, 1, 0, 1, 0, 0, 0, 1, 1, 1],
                           [0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
                           [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                           [0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                           [1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
                           [1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                           [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
                           [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                           [0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
                           [1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
                           [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
                           [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
                           [0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                           [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                           [1, 0, 0, 1, 0, 1, 1, 1, 1, 0],
                           [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                           [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 1, 0, 1, 0, 0]]


            min_shifts: 5

            max_unwanted_shifts: 10

            sys_admins_per_night: 8

        Return:
            answer: None

        Time complexity
            Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
            complexity will be the same.
            Worst: O(n^2). The reason for this complexity is because in this function, if we exclude the calling of the
            function of ford_fulkerson_algorithm, we can see that the complexity will be at most O(n^2) since there is
            only one for which contains another for loop inside where the n is the length of the ttl_admins and the
            inner for loop is the preference the length. Although the complexity of the ford_fulkerson_algorithm is
            O(n^2), since it is called outside of the for loop, the complexity will only be O(n^2 + n^2) this will only
            combine together and form the total complexity of O(n^2).
        Space complexity:
            Input: O(n^2).
            Aux: O(n^2). This is because there has been a new array created and the calling of functions which have a
            Auxilary space complexity of O(n^2)
    """
    issuing = None
    spaces = 30
    ttl_admins = len(preferences[0])
    wanted_option = 1 + 2 + spaces + (ttl_admins * 2)
    overall_required_shifts = sysadmins_per_night * spaces

    if 0 > overall_required_shifts - (ttl_admins * min_shifts):
        return issuing
    fw_g = (wanted_option) * [None]
    # First starting row node has been added as well as the reversal for the remaining residual left
    if fw_g[0] == None:
        fw_g[0] = [[1, overall_required_shifts - (min_shifts * ttl_admins)]]
    else:
        fw_g[0].append([1, overall_required_shifts - (min_shifts * ttl_admins)])
    if fw_g[1] == None:
        fw_g[1] = [[0, 0]]
    else:
        fw_g[1].append([0, 0])
    # Preferences of the system administrator is added below. After each row node has been added, there will be a
    # reversal for the remaining residual
    for j in range(ttl_admins):
        if fw_g[0] == None:
            fw_g[0] = [[2 + j, min_shifts]]
        else:
            fw_g[0].append([2 + j, min_shifts])
        if fw_g[2 + j] == None:
            fw_g[2 + j] = [[0, 0]]
        else:
            fw_g[2 + j].append([0, 0])
        if fw_g[1] == None:
            fw_g[1] = [[2 + j, spaces]]
        else:
            fw_g[1].append([2 + j, spaces])
        if fw_g[2 + j] == None:
            fw_g[2 + j] = [[1, 0]]
        else:
            fw_g[2 + j].append([1, 0])
        # The remaining rows which are the max unwanted shifts will be filled in
        if fw_g[2 + j] == None:
            fw_g[2 + j] = [[2 + j + ttl_admins, max_unwanted_shifts]]
        else:
            fw_g[2 + j].append([2 + j + ttl_admins, max_unwanted_shifts])
        if fw_g[2 + j + ttl_admins] == None:
            fw_g[2 + j + ttl_admins] = [[2 + j, 0]]
        else:
            fw_g[2 + j + ttl_admins].append([2 + j, 0])
    # Remaining interior list following the preferences[i][j] is filled below
    for i in range(spaces):
        for j in range(len(preferences[i])):
            if preferences[i][j] == 1:
                if fw_g[2 + j] == None:
                    fw_g[2 + j] = [[i + 2 + (ttl_admins * 2), 1]]
                else:
                    fw_g[2 + j].append([i + 2 + (ttl_admins * 2), 1])
                if fw_g[i + 2 + (ttl_admins * 2)] == None:
                    fw_g[i + 2 + (ttl_admins * 2)] = [[2 + j, 0]]
                else:
                    fw_g[i + 2 + (ttl_admins * 2)].append([2 + j, 0])
            else:
                if fw_g[j + 2 + ttl_admins] == None:
                    fw_g[j + 2 + ttl_admins] = [[2 + i + (ttl_admins * 2), 1]]
                else:
                    fw_g[j + 2 + ttl_admins].append([2 + i + (ttl_admins * 2), 1])
                if fw_g[i + 2 + (ttl_admins * 2)] == None:
                    fw_g[i + 2 + (ttl_admins * 2)] = [[j + 2 + ttl_admins, 0]]
                else:
                    fw_g[i + 2 + (ttl_admins * 2)].append([j + 2 + ttl_admins, 0])
        # Reamining flow graph left for the system administrators who have their wanted options
        if fw_g[i + 2 + (ttl_admins * 2)] == None:
            fw_g[i + 2 + (ttl_admins * 2)] = [[wanted_option - 1, sys_admins_per_night]]
        else:
            fw_g[i + 2 + (ttl_admins * 2)].append([wanted_option - 1, sys_admins_per_night])
        if fw_g[wanted_option - 1] == None:
            fw_g[wanted_option - 1] = [[i + 2 + (ttl_admins * 2), 0]]
        else:
            fw_g[wanted_option - 1].append([i + 2 + (ttl_admins * 2), 0])
    # If statement to check whether answer should be None or a list of list
    if fw_g[wanted_option - 1] == None:
        fw_g[wanted_option - 1] = [[0, 0]]
    else:
        fw_g[wanted_option - 1].append([0, 0])
    issuing = ford_fulkerson_algorithm(fw_g, 0, wanted_option - 1, spaces, sysadmins_per_night, ttl_admins)
    return issuing

"""
2 A Chain of Events (4 marks + 1 mark for documentation)
"""
class events_trie_alphabet_nodes:
    """
    This is just a helper class for the main class eventsTrie. This was created so that during the implementation of the
    eventsTrie class it would make implementation the methods more simpler.
    """

    def __init__(self):
        """
        This function is the __init__ function of the helper class events_trie_alphabet_nodes. It is used for a couple
        reasons, the first is to instantiate a occurence_count which will be implemented later during the
        getLongestChain method and it keeps a count on how many times the string has been used with the prefix selected,
        the next is to show the full letters of the alphabet from a-z, the next is to count how many times the timeline
        has appeared and the last method is to indicate the ending of the timeline string
        """
        self.occurence_count = 0
        self.next_letters = [None] * 26
        self.count = 0
        self.dollar = False


class EventsTrie:
    def __init__(self, timelines):
        """
            This function takes input of a string array to compute through a function to create a generalised suffix
            trie data structure which will be used in another function. The approach I've taken is use the helper
            class which is used to help create the trie. Then use a series of for loops and while loops to help
            calculate the longest_chain_timelines
            Written by Soh En Ming

            Precondition: A set of string array which contains string values of the different timelines that was
                converted into words that consisted of events as the characters that Master X would have been through.
            Postcondition: Returns a generalised suffix trie data structure and also returns the value of
            longest_chain_timelines.

            Input:
                timelines: ["abaaac", "dbce", "aabcba", "dbce", "caaaa"]

            Return:
                answer: A generalised suffix trie data structure which is normally stored in a variable after calling
                the function in the class. In this case it would be mytrie = EventsTrie(timelines)

            Time complexity
                Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
                complexity will be the same.
                Worst: O(NM^2). The reason for this complexity is because in this function is because the code which
                calculates the longest_chain_timeline has the total combined complexity of O(NM^2).
            Space complexity:
                Input: O(1). This is becayse the
                Aux: O(n). This is because there has been a new array created
        """
        self.timelines = timelines
        self.longest_chain_timelines = [None] * (len(timelines) + 1)
        # Initialise the class
        self.root = events_trie_alphabet_nodes()
        trie_node_selected = self.starting_node

        # Call the insert method for each string:
        for timeline_string in timelines:
            self.insert(timeline_string)
            prefix_q = []
            for n in range(len(timeline_string)):
                prefix_value = prefix_q.append(timeline_string)
            while prefix_q:
            # For the longest_chain_timelines
                if self.longest_chain_timelines[trie_node_selected.return_chain()] == None:
                    self.longest_timelines[trie_node_selected.return_chain()] = prefix_value[:trie_node_selected.return_depth()]
                elif len(trie_node_selected.return_depth() > self.longest_timelines[trie_node_selected.return_chain()]):
                    self.longest_timelines[trie_node_selected.return_chain()] = prefix_value[:trie_node_selected.return_depth()]

    def insert(self, timelines):
        """
        This function is used to help insert the timeline created into the trie.

        Time complexity
                Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
                complexity will be the same.
                Worst: O(n). The reason for this complexity is because in this function is because there is a while loop
                used which has a complexity of O(n) where the n is the length of the string.
        """
        base = self.root
        base.occurence_count += 1

        # Used to iterate through all characters in the alphabet
        idx = 0
        while idx < len(timelines):
            char_num = int(ord(timelines[idx]) - ord('a'))
            if base.next_letters[char_num] == None:
                base.next_letters[char_num] = events_trie_alphabet_nodes()
            base = base.next_letters[char_num]
            base.occurence_count += 1

            idx += 1
        base.dollar = True
        base.count += 1

    def getLongestChain(self, noccurence):
            """
                This function takes a input of a integer value which is a positive noccurence that can range from 1 to N
                which will be computed through the function to return a string that represents the longest chain of events
                that occurs based on the noccurence integer chosen. The approach I've taken is to just to call it to the
                init function.
                Written by Soh En Ming

                Precondition: A positive noccurence integer which is in a range of 1 to N
                Postcondition: Returns a string which represents the longest chain of events that occurs in the noccurence
                timelimes which was stated in the noccurence integer input

                Input:
                    noccurence: 1

                Return:
                    answer: Since this is a function in the class, after the trie data has been stored in mytrie, it would
                    be called like this mytrie.getLongestChain(noccurence) then the answer that is formed will be abaaac

                Time complexity
                    Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
                    complexity will be the same.
                    Worst: O(1). This is because this function just returns the code which calls to another function
                    which will only have the complexity of O(1)
                Space complexity:
                    Input: O(1).
                    Aux: O(1).
            """
            return self.longest_chain_timelines[noccurence]

