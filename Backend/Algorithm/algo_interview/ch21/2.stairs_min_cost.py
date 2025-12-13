# LC 746
def stairMinCost_1(cost):
    return process(len(cost), cost)

def process(i, cost):
    if i < 2:
        return cost[i]
    return min(process(i - 1, cost) + cost[i - 1], process(i - 2, cost) + cost[i - 2])


def starrMinCost_2(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 0
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return dp[n]