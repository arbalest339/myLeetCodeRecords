def editDist(w1, w2):
    w1 = "#" + w1
    w2 = "#" + w2
    l1 = len(w1)
    l2 = len(w2)
    dp = [[0]*l2 for _ in range(l1)]
    for i in range(l1):
        dp[i][0] = i

    for j in range(l2):
        dp[0][j] = j

    for i in range(1, l1):
        for j in range(1, l2):
            if w1[i] == w2[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

    return dp[-1][-1]


if __name__ == "__main__":
    w1 = "arbalest"
    w2 = "arbelest"
    editDist(w1, w2)
