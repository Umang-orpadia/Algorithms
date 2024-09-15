def lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    lcs = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    
    return lcs[m][n]

# Example usage
s1 = "AGGTAB"
s2 = "GXTXAYB"
print(lcs(s1, s2)) # Output: 4
