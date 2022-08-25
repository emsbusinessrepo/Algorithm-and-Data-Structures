def binary_search_attack(attacks, curr_attack_index):
    low = 0
    high = curr_attack_index - 1

    while low <= high:
        mid = (low + high) // 2
        if attacks[mid][2] < attacks[curr_attack_index][1]:
            if attacks[mid + 1][2] < attacks[curr_attack_index][1]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1


def hero(attacks):
    sorted_attacks = sorted(attacks, key=lambda x: x[2])

    n = len(sorted_attacks)
    kill_count = [0] * n
    kill_count[0] = sorted_attacks[0][-1]

    counters = []

    for i in range(1, n):
        curr_clone_kill_count = sorted_attacks[i][-1]

        qj = binary_search_attack(sorted_attacks, i)

        if qj != -1:
            curr_clone_kill_count += kill_count[qj]

        # kill_count[i] = max(curr_clone_kill_count, kill_count[i-1])
        if curr_clone_kill_count >= kill_count[i - 1]:
            kill_count[i] = curr_clone_kill_count
            counters.append(sorted_attacks[qj])
        else:
            kill_count[i] = kill_count[i - 1]
            counters.append(sorted_attacks[i - 1])

    return counters


if __name__ == '__main__':
    #Random test case 1
    attacks = [[1, 2, 7, 6], [2, 7, 9, 10], [3, 8, 9, 5]]
    print(hero(attacks))
    #expected = [[1, 2, 7, 6], [3, 8, 9, 5]]

    #Random test case 2
    attacks = [[1,1,3,9], [2,3,4,5], [3,1,5,2], [4,4,6,8], [5,3,9,1], [6,5,8,8], [7,5,10,6], [8,8,11,5]]
    print(hero(attacks))
    #expected = [[8,8,11,5], [4,4,6,8], [1,1,3,9]]

    #Random test case 3
    attacks = [[1,1,100,7], [2,4,100,8], [3,23,100,12], [4,31,100,6], [5,51,100,9]]
    print(hero(attacks))
    #expected = [[3,23,100,12]]