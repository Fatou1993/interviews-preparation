def minimum_messiness(words, line_length):
    n = len(words)
    dp = [0]*(n+1)
    lengths = [len(word) for word in words]
    for i in range(1, n+1):
        space_left = line_length - lengths[i-1]
        if space_left < 0 :
            raise ValueError(" Impossible to place one of the words in a line")
        dp[i] = dp[i-1] + space_left*space_left #words[i-1] placed in new line alone
        for j in range(i-2,-1,-1):
            space_left -= (lengths[j]+1)
            if space_left < 0 :
                break
            dp[i] = min(dp[i], dp[j]+space_left*space_left)
    #print dp[i]
    return dp[n]

if __name__ == "__main__":
    words = ["I", "have", "inserted", "a", "large", "number", "of", "new", "examples", "from", "the", "papers",
             "for", "the", "Mathematical", "Tripes", "during", "the", "last", "twenty", "years,", "which", "should",
             "be", "useful", "to", "Cambridge", "students."]
    line_length = 36
    print minimum_messiness(words, line_length)
