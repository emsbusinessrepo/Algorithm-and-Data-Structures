def best_revenue(revenue, travel_days, start):
    total_revenue = 0
    numCity = len(revenue[0])    #numColumn
    numDays= len(revenue) #numRow
    dp = [-1]*numCity
    total_revenue = findBestRevenue(revenue, travel_days, start, numDays, dp)
    return total_revenue


def findBestRevenue(revenue, travel_days, start, numDays, dp):
    if start == numDays:
        return 0
    max = 0
    if dp[start] != -1:
        return dp[start]
    for day in travel_days[start]:
        if travel_days[start][day] != -1:
            max = max(revenue[start][day] + findBestRevenue(revenue, travel_days, start + travel_days[start][day], numDays, dp), findBestRevenue(revenue, travel_days, start + travel_days[start][day] - 1, numDays, dp))
        else:
            max = findBestRevenue(revenue, travel_days, start + travel_days[start][day] - 1, numDays, dp)
    dp[start] = max
    return dp[start]

# #         city:  0   1   2    # city:
# travel_days = [[-1,  1,  1],  # 0
#             [ 1, -1,  1],  # 1
#             [ 1,  2, -1]]  # 2
# #     city: 0  1    2     # day:
# revenue = [[1, 2,   1],   # 0
#         [3, 3,   1],   # 1
#         [3, 4,   1],   # 1
#         [1, 1, 100]]   # 2
# start = 0
# best_revenue(revenue, travel_days, start)

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
best_revenue(revenue, travel_days, start)