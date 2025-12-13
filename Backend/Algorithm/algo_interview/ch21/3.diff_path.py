def uniquePath_1(m, n):
    """递归"""
    if m < 1 or n < 1:
        return 0
    return process(m, n, 0, 0)

def process(m, n, i, j):
    """m:行;n:列;i:当前行位置"""
    if i == m - 1 or j == n - 1:
        return 1
    return process(m, n, i + 1, j) + process(m, n, i, j + 1)


def uniquePath_2(m, n):
    """dp"""
    if m < 1 or n < 1:
        return 0
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for i in range(n):
        dp[0][i] = 1
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]