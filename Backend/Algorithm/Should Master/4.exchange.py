def minCoins1(arr, m):
    if arr is None or len(arr) == 0 or m <= 0:
        return -1
    return process(arr, 0, m)

def process(arr, i, rest):
    if i == len(arr):
        return 0 if rest == 0 else -1
    res = -1
    k = 0
    while k * arr[i] <= rest:
        next = process(arr, i + 1, rest - k * arr[i])
        if next != -1:
            if res == -1:
                rest = next + k
            else:
                res = min(res, next+k)
        k += 1
    return res

def minCoins2(arr, m):
    if arr is None or len(arr) == 0 or m <= 0:
        return -1
    N = len(arr)
    dp = [[0 for _ in range(m + 1)] for _ in range(N + 1)]

    dp[N][0] = 0
    for i in range(1, m + 1):
        dp[N][i] = -1
    
    for i in range(N-1, -1, -1):
        for rest in range(m+1):
            dp[i][rest] = -1
            if dp[i+1][rest] != -1:
                dp[i][rest] = dp[i+1][rest]
            
            if rest - arr[i] >= 0 and dp[i][rest-arr[i]] != -1:
                if dp[i][rest] == -1:
                    dp[i][rest] = dp[i][rest-arr[i]] + 1
                else:
                    dp[i][rest] = min(dp[i][rest], dp[i][rest-arr[i]] + 1)
    return dp[0][m]