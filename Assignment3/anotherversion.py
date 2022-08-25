def best_revenue(revenue, travel_days, start):
    yesterdays_gain = []
    day_gain = [float('-inf')] * len(revenue[-1])
    day_gain[start] = 0

    for day in range(len(revenue)):
        yesterdays_gain.append(day_gain.copy())
        print(yesterdays_gain)
        for city in range(len(revenue[-1])):
            if day_gain[city] != float('inf'):
                day_gain[city] += revenue[day][city]
                print(day_gain)
        bell_algorithm(travel_days, day_gain, day, yesterdays_gain)
    print(day_gain)
    max_possible_revenue = day_gain[0]
    for idx in day_gain:
        if idx > max_possible_revenue:
            max_possible_revenue = idx
    return max_possible_revenue

def bell_algorithm(travel_days, day_gain, day, yesterdays_gain):
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



# Testing

# #       city:    0  1  2  3   # city:
# travel_days = [[-1,-1, 3, 1], # 0
#                 [-1,-1,-1, 1], # 1
#                 [ 1,-1,-1, 1], # 2
#                 [ 1, 1, 2,-1]] # 3
#
# #       city:    0     1  2  3 # day:
# revenue =     [[ 1,    2, 3, 4], # 0
#                 [ 3,    6, 1, 5], # 1
#                 [ 1,    8, 4, 1], # 2
#                 [ 1,   10, 4, 5], # 3
#                 [10,    4, 5, 9]] # 4
# start = 3

# travel_days = [[-1, 1, 1],  # 0
#                        [1, -1, 1],  # 1
#                        [1, 2, -1]]  # 2
#         #     city: 0  1    2     # day:
# revenue = [[1, 2, 1],  # 0
#                    [3, 3, 1],  # 1
#                    [1, 1, 100]]  # 2
# start = 2

# travel_days = [[-1, -1, 3, 1],  # 0
#                        [-1, -1, -1, 1],  # 1
#                        [1, -1, -1, 1],  # 2
#                        [1, 1, 2, -1]]  # 3
#
# #       city:    0     1  2  3 # day:
# revenue = [[1, 2, 3, 4],  # 0
#            [3, 6, 1, 5],  # 1
#            [1, 8, 4, 1],  # 2
#            [1, 10, 4, 5],  # 3
#            [10, 4, 5, 9]]  # 4
# start = 3

#         city:  0   1   2    # city:
travel_days = [[-1, 1, 1],  # 0
               [1, -1, 1],  # 1
               [1, 2, -1]]  # 2
#     city: 0  1    2     # day:
revenue = [[1, 2, 1],  # 0
           [3, 3, 1],  # 1
           [1, 1, 100]]  # 2
start = 1
# expected_max_profit = 102


print(best_revenue(revenue, travel_days, start))