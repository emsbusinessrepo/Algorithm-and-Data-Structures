"""
Name: Soh En Ming
Student ID: 32024975
Title: FIT2004 S1/2022: Assignment 3
Unit Code: FIT2004

This assignment was done on Python Version 3.9.2.
"""


"""
1 Salesperson Revenue (4 marks + 1 mark for documentation)
"""


def best_revenue(revenue, travel_days, start):
    """
        This function takes inputs of lists from revenue, travel_day and inputs of a integer value from start city
        which it then computes it through the function to find the largest maximum possible revenue. The approach I've
        taken is through using the bellman-ford algorithm to find the largest possible revenue that could be made in
        that day, then using some loops to update the total revenue for each day in the city then lastly using some
        loops to find the max revenue in the array.
        Written by Soh En Ming

        Precondition: 1 set of lists which contains the revenue that a person would make, 1 set of list which
            contains integers that indicate how many days you need to spend to travel and lastly a integer to
            denote the starting day
        Postcondition: Returns a integer contains the largest maximum possible revenue

        Input:
            revenue:    [[[1, 2, 1],
                        [3, 3, 1],
                        [1, 1, 100]]

            travel_days:[[-1, 1, 1],
                        [1, -1, 1],
                        [1, 2, -1]]

            start = 0

        Return:
            answer: 101

        Time complexity
            Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
            complexity will be the same.
            Worst: O(n^2(d+n)). The reason for this complexity is because in this function, there has been a couple of
            loops used, like a for loop which has a complexity of O(d) where d is length of the revenue and another
            for loop within which has a complexity O(d^2) since it is within another for loop. There is also complexity
            of O(n^2) from the bellman-ford algorithm function bellow which has been instantiated inside the function.
            This would create a total complexity of O(n^2(d+n)).
        Space complexity:
            Input: O(n).
            Aux: O(n). This is because there has been a new array created
    """
    yesterdays_gain = []
    day_gain = [float('-inf')] * len(revenue[-1])
    day_gain[start] = 0

    for day in range(len(revenue)):
        # for loop to help iterate through every day in revenue list and update the total revenue
        yesterdays_gain.append(day_gain.copy())
        for city in range(len(revenue[-1])):
            if day_gain[city] != float('inf'):
                day_gain[city] += revenue[day][city]
        bell_algorithm(travel_days, day_gain, day, yesterdays_gain)
    max_possible_revenue = day_gain[0]
    for idx in day_gain:
        # to find the max revenue within the array
        if idx > max_possible_revenue:
            max_possible_revenue = idx
    return max_possible_revenue

def bell_algorithm(travel_days, day_gain, day, yesterdays_gain):
    """
        This function is one of my implementations for a bellman_ford_algorithm. This function is a helper for the
        function above. What this function does is that it is used to find the largest revenue made on that day in the
        city.
        Written by Soh En Ming

        Time complexity:
            Best: As seen in the code below, there is no fast exit in this function therefore, the best and worst
            case of this function is the same.
            Worst: O(n^2). The Reason for this complexity is because in the function, there was intially a for loop
            used which has a complexity of O(n) where n is the length of day_gain but since there is another for loop
            within it, the complexity will now be O(n^2) and since the rest are all constant complexity, the final
            worse case complexity will be O(n^2).

        Space complexity:
            Input: O(1)
            Aux: O(1)
    """
    for city_x in range(len(day_gain)):
        if day_gain[city_x] != 0:
            for city_y in range(len(travel_days[city_x])):
                next_day = day + 1
                current_total_days = travel_days[city_x][city_y]
                if current_total_days != -1 and next_day >= current_total_days:
                    if day_gain[city_y] == float('-inf'):
                        day_gain[city_y] = 0
                    elif day_gain[city_y] < yesterdays_gain[current_total_days - next_day][city_x]:
                        day_gain[city_y] = yesterdays_gain[current_total_days - next_day][city_x]


"""
2 Saving the Multiverse (4 marks + 1 mark for documentation)
"""


def hero(attacks):
    """
        This function takes a input which is a non-empty list of N attacks where the attack contains 4 items inside
        to find the final combination which is a list that contains the most number of clones defeated from the
        list given while not having any days where you are occupied. The approach I've taken is using binary search
        firstly to sort the array and find the middle value then using if loops to compare between Dr weird kill count
        and the kill count in the attack list. After that it was just using process of elimination to append the correct
        values of the list into another list.
        Written by Soh En Ming

        Precondition: A non-empty list of N attacks where each attack is a list of 4 items which is the integer of
            which multiverse the villain is attacking, the starting and ending days of the attack and lastly the number
            of clones that were in the attack.
        Postcondition: A list which contains the optimal solution that contains the largest number of clones defeated
        while also having no days where you will be occupied.

        Input:
            attacks: [[1, 2, 7, 6], [2, 7, 9, 10], [3, 8, 9, 5]]

        Return:
            answer: [[3, 8, 9, 5], [1, 2, 7, 6]]

        Time complexity
            Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
            complexity will be the same.
            Worst: O(NlogN). The reason for this complexity is because in the function, there is a for loop inside the
            function which has a complexity of O(n) where n is the length of attack array then furthermore, the
            function binary search has been called inside the for loop which has a complexity of O(LogN) therefore,
            adding all the complexity together, the final worse case time complexity will be O(NLogN).
        Space complexity:
            Input: O(N). This is because there was an input list given which takes up O(n) space
            Aux: O(N) auxiliary space complexity
    """
    master_x_atk = []
    atk_len = len(attacks)
    kill_count = [0] * atk_len
    kill_count[0] = attacks[0][-1]

    for idx in range(1, atk_len):
        weird_kill_count = attacks[idx][-1]
        check = binary_search_sort(attacks, idx)
        # if loops to check and figure out which contains the most kill count
        if check != -1:
            weird_kill_count += kill_count[check]
        if weird_kill_count >= kill_count[idx - 1]:
            kill_count[idx] = weird_kill_count
            master_x_atk.append(attacks[check])
        elif weird_kill_count <= kill_count[idx - 1]:
            kill_count[idx] = kill_count[idx - 1]
            master_x_atk.append(attacks[idx - 1])
    return master_x_atk

def binary_search_sort(lst, weird_kill_count):
    """
        This function is one of my implementations for binary search sorting algorithm but in this case it has been
        inplemented for the function hero(attack). How I implemented this sorting algorithm is using the while loop
        and splitting the array in half, after that I can use comparison to match and find the middle of the array.
        Written by Soh En Ming and taken inspiration/sourced from https://www.geeksforgeeks.org/binary-search/

        Time complexity:
            Best: As seen in the code below, there is no fast exit in this function therefore, the best and worst
            case of this function is the same.
            Worst: O(LogN). The reason for the complexity is because in the function, there is a while loop that's been
            used, the time complexity for while loops are normally Log N because of the total number of comparisons
            required. The rest of the code is constant therefore the worse case time complexity is O(LogN)

        Space complexity:
            Input: O(1). This binary search sort isn't the recursive version therefore, the space complexity will be
            O(1)
            Aux: O(1)
    """
    hi = weird_kill_count - 1
    lo = 0

    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid][2] < lst[weird_kill_count][1]:
            if lst[mid + 1][2] < lst[weird_kill_count][1]:
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1

