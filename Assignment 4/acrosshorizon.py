import math

global unwanted_shifts_taken, total_shift_taken, numdays, numSysAdmins


def allocate(preferences, sysadmins_per_night, max_unwanted_shifts, min_shifts):
    graph = []
    global unwanted_shifts_taken, total_shift_taken, numdays, numSysAdmins
    unwanted_shifts_taken = [0] * len(preferences[0])
    total_shift_taken = [0] * len(preferences[0])
    numdays = len(preferences)
    numSysAdmins = len(preferences[0])
    table = []
    for i in range(len(preferences)):
        temp = []
        for j in range(len(preferences[0])):
            temp.append(0)
        table.append(temp)

    generateGraph(graph, preferences, sysadmins_per_night, max_unwanted_shifts)
    # for x in graph:print(x, ", ")print("######################################################")

    maxFlow = FordFulkerson(graph, 0, len(graph[0]) - 1, max_unwanted_shifts, table)
    # print(maxFlow)
    # print("++++++++++++++++++++++")
    # for item in result:print(item)
    # print("++++++++++++++++++++++")
    print("Max flow expected: ", numdays * sysadmins_per_night)
    print("Max flow result: ", maxFlow)
    print("numdays: ", numdays)
    print("sysadmins_per_night: ", sysadmins_per_night)
    for x in graph:
        print(x, ", ")
    print("######################################################")

    if check(max_unwanted_shifts, min_shifts) and maxFlow >= numdays * sysadmins_per_night:

        return table
    else:
        return None


def generateGraph(graph, preferences, sysadmins_per_night, max_unwanted_shifts):
    global unwanted_shifts_taken, total_shift_taken, numdays, numSysAdmins
    # print("numdays: ", numdays)
    # print("numSysAdmins: ", numSysAdmins)
    for i in range(2 * numSysAdmins + 2 + numdays):
        temp = []
        for j in range(2 * numSysAdmins + 2 + numdays):
            temp.append(0)
        graph.append(temp)

    # Initialize capacity from each day to sink by sysadmins_per_night
    for i in range(2 * numSysAdmins + 1, 2 * numSysAdmins + 1 + numdays):
        graph[i][2 * numSysAdmins + 1 + numdays] = sysadmins_per_night
    # Initialize capacity from source to each employee node of preferred working day by numdays
    for j in range(1, numSysAdmins + 1):
        graph[0][j] = numdays
    # #Initialize capacity from source to each employee node of non-preferred working day by max_unwanted_shifts
    for j in range(1 + numSysAdmins, 2 * numSysAdmins + 1):
        graph[0][j] = max_unwanted_shifts
    # Initilize capacity from each employee node of preferred working day to each day by 1
    for i in range(1, numSysAdmins + 1):
        for j in range(2 * numSysAdmins + 1, 2 * numSysAdmins + 1 + numdays):
            graph[i][j] = preferences[j - (2 * numSysAdmins + 1)][i - 1]
    # Initilize capacity from each employee node of non-preferred working day to each day by 1
    for i in range(1 + numSysAdmins, 2 * numSysAdmins + 1):
        for j in range(2 * numSysAdmins + 1, 2 * numSysAdmins + 1 + numdays):
            temp = 0
            if preferences[j - (2 * numSysAdmins + 1)][i - numSysAdmins - 1] == 0:
                temp = 1
            graph[i][j] = temp


def BFS(graph, s, t, parent, max_unwanted_shifts):
    global unwanted_shifts_taken, total_shift_taken, numdays, numSysAdmins
    visited = [False] * len(graph[0])
    q = []
    q.append(s)
    visited[s] = True

    while len(q) > 0:
        x = q[0]
        q.pop(0)
        for y in range(len(graph[0])):
            if y > 0 and y <= numSysAdmins:
                # print("From BFS: RUN IF")
                if visited[y] == False and graph[x][y] > 0 and unwanted_shifts_taken[y - 1] < max_unwanted_shifts:
                    # print("### Run satisfied ### \t node: ", y, "\ton day: ", x)
                    visited[y] = True
                    parent[y] = x
                    q.append(y)
            elif y > numSysAdmins and y < len(graph[0]) - numdays - 1:
                # print("From BFS: RUN ELIF")
                if visited[y] == False and graph[x][y] > 0 and unwanted_shifts_taken[
                    y - numSysAdmins - 1] < max_unwanted_shifts:
                    # print("### Run satisfied ###")
                    # print("### Run satisfied ### \t node: ", y, "\ton day: ", x)
                    visited[y] = True
                    parent[y] = x
                    q.append(y)
            else:
                # print("From BFS: RUN ELSE")
                if visited[y] == False and graph[x][y] > 0:
                    # print("### Run satisfied ###")
                    visited[y] = True
                    parent[y] = x
                    q.append(y)

            '''
            if visited[y] == False and graph[x][y] > 0:
                visited[y] = True
                parent[y] = x
                q.append(y)
            '''

    # for x in graph:print(x)print("--------------------------------------------")
    return visited[t] == True


def FordFulkerson(graph, s, t, max_unwanted_shifts, table):
    parent = [-1] * len(graph[0])
    sum = 0
    global unwanted_shifts_taken, total_shift_taken, numdays, numSysAdmins
    while BFS(graph, s, t, parent, max_unwanted_shifts):
        temp = math.inf
        y = t
        while y != s:
            x = parent[y]
            temp = min(temp, graph[x][y])
            if x != s:
                if x <= numSysAdmins:
                    # print("index preferred: ", x, "\ton day: ", y)
                    total_shift_taken[x - 1] += 1
                    appendResult(x, y, table)
                    preNode = x
                    # print(result)
                if x > numSysAdmins and x < 2 * numSysAdmins + 1:
                    # print("index unwanted: ", x, "\ton day: ", y)
                    unwanted_shifts_taken[x - (2 * numSysAdmins) - 1] += 1
                    total_shift_taken[x - (2 * numSysAdmins) - 1] += 1
                    appendResult(x, y, table)
                    preNode = x
                    # print(result)

            y = parent[y]

        y = t
        while y != s:
            x = parent[y]
            graph[x][y] -= temp
            graph[y][x] += temp
            y = parent[y]

        sum += temp
    # print("---------------------------------------------------------")
    # for x in graph:print(x)
    return sum


# x: sysadmins number, y: day
def appendResult(x, y, table):
    global unwanted_shifts_taken, total_shift_taken, numdays, numSysAdmins
    if x > 0 and x <= numSysAdmins:
        table[y - (2 * numSysAdmins) - 1][x - 1] = 1
    if x > numSysAdmins and x <= 2 * numSysAdmins:
        table[y - (2 * numSysAdmins) - 1][x - numSysAdmins - 1] = 1


def check(max_unwanted_shifts, min_shifts):
    global unwanted_shifts_taken, total_shift_taken, numdays, numSysAdmins
    for x in unwanted_shifts_taken:
        if x > max_unwanted_shifts:
            print("1.Not passed Check()")
            print(x)
            return False
    for y in total_shift_taken:
        if y < min_shifts:
            print("2.Not passed Check()")
            return False
    print("Check() satisfied")
    return True


if __name__ == '__main__':
    preferences = [[0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
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
    min_shifts = 5
    max_unwanted_shifts = 10
    sys_admins_per_night = 7
    expectingNone = False
    print(allocate(preferences, sys_admins_per_night, max_unwanted_shifts, min_shifts))
    global unwanted_shifts_taken, total_shift_taken
    print("Total: ", total_shift_taken)
    print("Shift: ", unwanted_shifts_taken)
