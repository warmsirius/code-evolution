def minCoins_1(arr, aim):
    """暴力递归"""
    if arr is None or len(arr) == 0 or aim < 0:
        return -1
    return process(arr, 0, aim)

def process(arr, i, rest):
    if i == len(arr):
        return 0 if rest == 0 else -1
    res = -1
    k = 0
    while k * arr[i] <= rest:
        next = process(arr, i + 1, rest - k * arr[i])
        if next != -1:
            res = next + k if res == -1 else min(res, next + k)
        k += 1
    return res


def minCoins_2(arr, aim):
    """dp"""
    if arr is None or len(arr) == 0 or aim < 0:
        return -1
    dp = [[0 for _ in range(aim+1)] for _ in range(len(arr) + 1)]
    dp[][] = 0