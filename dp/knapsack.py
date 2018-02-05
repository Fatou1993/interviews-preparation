from collections import namedtuple
def knapsack(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    taken = [[False for _ in range(capacity + 1)] for _ in range(n)]
    path = [0] * (n)
    for j in range(capacity + 1):
        dp[0][j] = 0
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            without_using_item = dp[i - 1][j]
            using_item = 0 if j < items[i - 1].weight else dp[i - 1][j - items[i - 1].weight] + items[i - 1].value
            if using_item < without_using_item:
                dp[i][j] = without_using_item
            else:
                dp[i][j] = using_item
                taken[i - 1][j] = True
            if j >= items[i - 1].weight:
                dp[i][j] = max(dp[i][j],
                               dp[i - 1][j - items[i - 1].weight] + items[i - 1].value)  # include the item[i-1]
    # Reconstruct path
    total_weight = capacity
    for i in range(n - 1, -1, -1):
        if taken[i][total_weight]:
            path[i] += 1
            total_weight -= items[i].weight

    for i in range(n):
        for _ in range(path[i]):
            print items[i],
    print ""
    return dp[n][capacity]

if __name__ == "__main__":
    Item = namedtuple("Item", ("value", "weight"))
    max_size = 130
    #items = [Item(65, 20), Item(35, 8), Item(245, 60), Item(195, 55), Item(65, 40), Item(150, 70), Item(275, 85),
    #         Item(155, 25),Item(120, 30), Item(320, 65), Item(75, 75), Item(40, 10), Item(200, 95), Item(100, 50),
    #         Item(220, 40), Item(99, 10)]
    items = [Item(60,5),Item(50,3),Item(70,4),Item(30,2)]
    print knapsack(items, 5)