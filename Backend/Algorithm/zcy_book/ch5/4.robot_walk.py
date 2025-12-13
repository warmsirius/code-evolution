def ways_1(N, M, K, P):
    """暴力递归"""
    if N < 2 or M < 1 or M > N or K < 1 or P < 1 or P > N:
        return 0
    return process(N, M, K, P)

def process(N, cur, rest, P):
    if rest == 0:
        return 1 if cur == P else 0
    if cur == 1:
        return process(N, 2, rest - 1, P)
    elif cur == N:
        return process(N, N - 1, rest - 1, P)
    else:
        return process(N, cur - 1, rest - 1, P) + process(N, cur + 1, rest - 1, P)
    

def ways_2(N, M, K, P):
    """dp"""
    if N < 2 or M < 1 or M > N or K < 1 or P < 1 or P > N:
        return 0
    
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    dp[P][0] = 1
    for rest in range(1, K+1):
        for cur in range(1, N+1):
            if cur == 1:
                dp[cur][rest] = dp[2][rest - 1]
            elif cur == N:
                dp[cur][rest] = dp[N-1][rest-1]
            else:
                dp[cur][rest] = dp[cur+1][rest-1] + dp[cur-1][rest-1]
    return dp[M][K]


def was_3(N, M, K, P):
    """dp+空间压缩"""
    if N < 2 or M < 1 or M > N or K < 1 or P < 1 or P > N:
        return 0
    
    dp = [0 for _ in range(N+1)]
    dp[P] = 1

    for rest in range(1, K+1):
        leftUp = dp[1] # dp[cur-1][rest-1]
        for cur in range(1, N+1):
            tmp = dp[cur] # dp[cur][rest-1]
            if cur == 1:
                dp[cur] = dp[2]
            elif cur == N:
                dp[cur] = leftUp
            else:
                dp[cur] = leftUp + dp[cur+1]
            leftUp = tmp
    return dp[M]
