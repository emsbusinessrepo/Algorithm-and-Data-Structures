from audioop import add


def allocate(preferences, sysadmins_per_night, max_unwanted_shifts, min_shifts):
    allocation = None
    n = 30
    total_required_shifts = n * sysadmins_per_night
    total_admins = len(preferences[0])
    target = 2 + total_admins * 2 + n + 1

    # Quick check to see if there are enough shifts to go around
    if (total_required_shifts - (min_shifts * total_admins)) < 0:
        return allocation

    flow_graph = [None] * (target)

    # Filling up the first row
    add_node(flow_graph, 0, 1, total_required_shifts - (min_shifts * total_admins))
    # Reversed for residual
    add_node(flow_graph, 1, 0, 0)

    #  Filling in admins preference.
    for j in range(total_admins):
        # Still filling in the first row
        add_node(flow_graph, 0, j + 2, min_shifts)
        # Reversed for residual
        add_node(flow_graph, j + 2, 0, 0)

        # Filling the second row
        add_node(flow_graph, 1, j + 2, n)
        # Reversed for residual
        add_node(flow_graph, j + 2, 1, 0)

        # Filling in each admin row to unwanted admin row
        add_node(flow_graph, j + 2, total_admins + j + 2, max_unwanted_shifts)
        # Reversed for residual
        add_node(flow_graph, total_admins + j + 2, j + 2, 0)

        # Filling in unwanted admin to days

    # Filling out preferences
    for i in range(n):
        for k in range(len(preferences[i])):
            if preferences[i][k] == 1:
                add_node(flow_graph, k + 2, 2 + total_admins * 2 + i, 1)
                # Reversed for residual
                add_node(flow_graph, 2 + total_admins * 2 + i, k + 2, 0)
            else:
                # Unwanted to each day
                add_node(flow_graph, 2 + total_admins + k, 2 + total_admins * 2 + i, 1)
                # Reversed for residual
                add_node(flow_graph, 2 + total_admins * 2 + i, 2 + total_admins + k, 0)

        # Filling out each day to target variable/ end of our flow graph
        add_node(flow_graph, 2 + total_admins * 2 + i, target - 1, sys_admins_per_night)
        # Reversed for residual
        add_node(flow_graph, target - 1, 2 + total_admins * 2 + i, 0)

    # Last variable, so it doesn't equal to none
    # add_node(flow_graph, target-1, 0, 0)

    allocation = FordFulkerson(flow_graph, 0, target - 1, n, sysadmins_per_night, total_admins)

    return allocation


def add_node(graph, node, other_node, weight):
    if graph[node] == None:
        graph[node] = [[other_node, weight]]
    else:
        graph[node].append([other_node, weight])


def BFS(graph, s, t, parent):
    visted = [False] * len(graph)
    queue = []
    queue.append(s)
    visted[s] = True

    while queue:
        cur_index = queue.pop(0)

        for i in graph[cur_index]:
            adj_index = i[0]
            if visted[adj_index] == False and i[1] > 0:
                queue.append(adj_index)
                visted[adj_index] = True
                parent[adj_index] = cur_index
                if adj_index == t:
                    return True
    return False


def FordFulkerson(graph, source, sink, n, sysadmin_per_night, total_admins):
    allocation = [[0] * total_admins]

    for i in range(n - 1):
        allocation.append([0] * total_admins)

    parent = [-1] * len(graph)

    max_flow = 0

    while BFS(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while (s != source):
            # Index finder for the linked list
            ind = None
            for i in range(len(graph[parent[s]])):
                if graph[parent[s]][i][0] == s:
                    ind = i
            path_flow = min(path_flow, graph[parent[s]][ind][1])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while (v != source):
            u = parent[v]
            ind_v = None
            for i in range(len(graph[u])):
                if graph[u][i][0] == v:
                    ind_v = i
            graph[u][ind_v][1] -= path_flow

            ind_u = None
            for i in range(len(graph[v])):
                if graph[v][i][0] == u:
                    ind_u = i
            graph[v][ind_u][1] += path_flow

            v = parent[v]

    # Filling out the allocations
    if (max_flow == sysadmin_per_night * n):
        for i in range(total_admins):
            for j in graph[i + 2]:
                if (j[0] != total_admins + i + 2) and j[1] == 0:
                    index = j[0] - (total_admins * 2 + 2)
                    allocation[index][i] = 1
            for k in graph[i + 2 + total_admins]:
                if (k[0] != i + 2) and k[1] == 0:
                    index = k[0] - (total_admins * 2 + 2)
                    allocation[index][i] = 1
    else:
        allocation = None
    return allocation

def ford_fulkerson_algorithm(flow_g, src, t, spaces, s_adm_p_n, ttl_admin):
    # referenced from https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
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
                    index = a_ind - (ttl_admin * 2 + 2)
                    issuing[index][n_ind] = 1
            for e_ind, e_val in flow_g[2 + ttl_admin + n_ind]:
                if e_ind != 2 + n_ind and e_val == 0:
                    index = (2 + 2 * ttl_admin) - e_ind
                    issuing[index][n_ind] = 1
    else:
        issuing = None
    return issuing

# preferences = [[0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
#                [1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
#                [0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
#                [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
#                [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
#                [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
#                [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
#                [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
#                [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
#                [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
#                [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
#                [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
#                [0, 1, 0, 1, 0, 0, 0, 1, 1, 1],
#                [0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
#                [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
#                [0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
#                [1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
#                [1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
#                [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
#                [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
#                [0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
#                [1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
#                [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
#                [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
#                [0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
#                [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
#                [1, 0, 0, 1, 0, 1, 1, 1, 1, 0],
#                [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
#                [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
#                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0]]
# min_shifts = 5
# max_unwanted_shifts = 10
# sys_admins_per_night = 6
#
# res = allocate(preferences, sys_admins_per_night, max_unwanted_shifts, min_shifts)
# print(res)

# preferences = [[0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
#                [1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
#                [0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
#                [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
#                [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
#                [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
#                [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
#                [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
#                [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
#                [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
#                [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
#                [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
#                [0, 1, 0, 1, 0, 0, 0, 1, 1, 1],
#                [0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
#                [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
#                [0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
#                [1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
#                [1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
#                [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
#                [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
#                [0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
#                [1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
#                [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
#                [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
#                [0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
#                [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
#                [1, 0, 0, 1, 0, 1, 1, 1, 1, 0],
#                [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
#                [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
#                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0]]
# min_shifts = 5
# max_unwanted_shifts = 10
# sys_admins_per_night = 6
# expectingNone = False
#
# res = allocate(preferences, sys_admins_per_night, max_unwanted_shifts, min_shifts)
# print(res)
#
# print(len(preferences))

# preferences = [[0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
#                [1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
#                [0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
#                [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
#                [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
#                [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
#                [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
#                [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
#                [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
#                [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
#                [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
#                [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
#                [0, 1, 0, 1, 0, 0, 0, 1, 1, 1],
#                [0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
#                [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
#                [0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
#                [1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
#                [1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
#                [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
#                [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
#                [0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
#                [1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
#                [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
#                [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
#                [0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
#                [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
#                [1, 0, 0, 1, 0, 1, 1, 1, 1, 0],
#                [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
#                [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
#                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0]]
#
# min_shifts = 5
# max_unwanted_shifts = 10
# sys_admins_per_night = 8
# expectingNone = True
#
# res = allocate(preferences, sys_admins_per_night, max_unwanted_shifts, min_shifts)
# print(res)

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

res = allocate(preferences, sys_admins_per_night, max_unwanted_shifts, min_shifts)
print(res)