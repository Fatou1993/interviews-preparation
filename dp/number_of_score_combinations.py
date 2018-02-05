def number_of_score_combinations(final_score, scores):
    m = len(scores)
    dp = [1]+[0]*final_score
    for i in range(1,m+1):
        for j in range(1, final_score+1):
            tmp = dp[j]
            #dp[i][j] = dp[i-1][j] #not use scores[i-1]
            if j-scores[i-1]>=0 :
                tmp += dp[j-scores[i-1]] #use scores[i-1]
            dp[j] = tmp

    return dp[final_score]

if __name__ == "__main__":
    scores = [2,3,7]
    final_score = 12
    print number_of_score_combinations(final_score, scores)
