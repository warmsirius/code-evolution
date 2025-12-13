
def _fib_0(n):
    """时间复杂度O(2^n)"""
    if n == 0 or n == 1:
        return 1
    return _fib_0(n - 1) + _fib_0(n - 2)

def fib_1(n, memo=None):
    """带备忘录的递归: 时间复杂度O(n)，空间复杂度O(n)"""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = fib_1(n - 1, memo) + fib_1(n - 2, memo)
    return memo[n]

def fib_2(n):
    """dp+空间压缩: 时间复杂度O(n)，空间复杂度O(1)"""
    if n == 0 or n == 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fib_3(n):
    """dp: 时间复杂度O(n)，空间复杂度O(n)"""
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]