
def fib_2_n(n):
    """时间复杂度为O(2^n)的斐波那契数列实现"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_2_n(n - 1) + fib_2_n(n - 2)


def fib_n(n):
    """时间复杂度为O(n)的斐波那契数列实现"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    pre = 0
    res = 1
    tmp = 0
    while n > 1:
        tmp = res
        res += pre
        pre = tmp
    return res


def fib_logn(n):
    """时间复杂度为O(log n)的斐波那契数列实现"""
    def matrix_mult(A: list[list], B: list[list]):
        """矩阵乘法"""
        res = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(A[0])):
                    res[i][j] += A[i][k] * B[k][j]
        return res


    def matrix_pow(M: list[list], p):
        """矩阵快速幂"""
        res = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
        for i in range(len(M)):
            res[i][i] = 1
        
        tmp = M
        while p > 0:
            if (p & 1):
                res = matrix_mult(res, tmp)
            tmp = matrix_mult(tmp, tmp)
            # 幂数右移一位
            p >>= 1
        return res

    if n == 0:
        return 0
    if n == 1:
        return 1

    initial = [[1, 1]]
    M = [[1, 1], [1, 0]]
    M_pow = matrix_pow(M, n - 2)
    res = matrix_mult(initial, M_pow)
    return res[0][0]


