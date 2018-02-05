def coins_in_line(coins):
    def coins_in_line_helper(dp, start, end):
        if end < start or start < 0 or end >= n:
            return 0
        if dp[start][end] == 0 :
            dp[start][end] = max(
                coins[start] + min(coins_in_line_helper(dp, start+2, end), coins_in_line_helper(dp, start+1, end-1)),
                coins[end] + min(coins_in_line_helper(dp, start+1, end-1), coins_in_line_helper(dp, start, end-2))
            )
        return dp[start][end]

    n = len(coins)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    return coins_in_line_helper(dp, 0, n-1)

if __name__ == "__main__":
    coins = [10,25,5,1,10,5]
    print coins_in_line(coins)