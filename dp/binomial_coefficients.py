import math
def test(n, k):
    """

    :param n:
    :param k:
    :return:
    """
    return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))

def binomial_coefficients(n, k):
    """

    :param n:
    :param k:
    :return:
    """
    if k > n :
        return 0
    dp = [1]+[0]*(k)
    for i in range(1,n+1):
        tmp = [1]
        for j in range(1,k+1):
            tmp.append(dp[j]+dp[j-1])
        dp = tmp
    return dp[k]


if __name__ == "__main__":
    n, k = 235, 132
    assert binomial_coefficients(n,k) ==  test(n,k)