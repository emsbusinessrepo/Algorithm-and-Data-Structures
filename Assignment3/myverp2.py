def binary_search_sort(lst, weird_kill_count):
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


def hero(attacks):
    atk_len = len(attacks)
    print(attacks)
    kill_count = [0] * atk_len
    kill_count[0] = attacks[0][-1]
    master_x_atk = []

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


if __name__ == '__main__':
    #Random test case 1
    attacks = [[1, 2, 7, 6], [2, 7, 9, 10], [3, 8, 9, 5]]
    print(hero(attacks))
    #expected = [[1, 2, 7, 6], [3, 8, 9, 5]]

    # #Random test case 2
    # attacks = [[1,1,3,9], [2,3,4,5], [3,1,5,2], [4,4,6,8], [5,3,9,1], [6,5,8,8], [7,5,10,6], [8,8,11,5]]
    # print(hero(attacks))
    # #expected = [[8,8,11,5], [4,4,6,8], [1,1,3,9]]
    #
    # #Random test case 3
    # attacks = [[1,1,100,7], [2,4,100,8], [3,23,100,12], [4,31,100,6], [5,51,100,9]]
    # print(hero(attacks))
    # #expected = [[3,23,100,12]]