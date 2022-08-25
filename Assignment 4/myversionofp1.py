

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