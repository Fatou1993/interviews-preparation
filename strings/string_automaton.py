NUM_CHARACTERS = 256

def compute_transition_function(pattern, m) :
    """
    Compute the transition matrix : there are m+1 states
    O(NUM_CHARACTERS*m^^3) complexity
    TF[state][c] = length of longest substring of P that matches P[:p]+c
    :param pattern:
    :param m:
    :return:
    """
    global NUM_CHARACTERS
    TF = [[0 for _ in range(NUM_CHARACTERS)] for _ in range(m+1)]
    for state in range(m+1):
        for c in range(NUM_CHARACTERS):
            k = min(state+1,m)
            while k > 0 and pattern[:k] != pattern[state-k+1:state]+chr(c):
                k -= 1
            TF[state][c] = k
    return TF

def finite_automaton_matcher(text, pattern):
    """
    Idea is to know at every text[i] a state that gives us the length of the longest prefix of P that ends at text[i]
    :param text:
    :param pattern:
    :return:
    """
    global NUM_CHARACTERS

    n, m = len(text), len(pattern)
    res = []
    if n < m :
        return res
    TF = compute_transition_function(pattern, m)
    state = 0
    for i in range(n):
        #print state, text[i]
        state = TF[state][ord(text[i])]
        if state == m : #m characters have been matched
            res.append(i-m+1)
    return res

if __name__ == "__main__":
    text = "AABAACAADAABAABA"
    patt = "AABA"
    res = finite_automaton_matcher(text, patt)
    for r in res :
        print "Pattern found at index:", r

