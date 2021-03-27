def findPrincess(puzzle, dp, x, y, z):
    changed = True
    while changed:
        changed = False
        for i in range(z):
            for j in range(x):
                for k in range(y):
                    if puzzle[i][j][k] == "#":
                        continue
                    if puzzle[i][j][k] == "*":
                        hpchange = -1
                    else:
                        hpchange = 0
                    if i > 0:
                        for newhp, newdis in dp[i-1][j][k].items():
                            newhp += hpchange
                            newdis += 1
                            if newhp > 0 and newhp not in dp[i][j][k]:
                                dp[i][j][k][newhp] = newdis
                                changed = True
                            elif newhp > 0 and dp[i][j][k][newhp] > newdis:
                                dp[i][j][k][newhp] = newdis
                                changed = True
                    if i < z-1:
                        for newhp, newdis in dp[i+1][j][k].items():
                            newhp += hpchange
                            newdis += 1
                            if newhp > 0 and newhp not in dp[i][j][k]:
                                dp[i][j][k][newhp] = newdis
                                changed = True
                            elif newhp > 0 and dp[i][j][k][newhp] > newdis:
                                dp[i][j][k][newhp] = newdis
                                changed = True
                    if j > 0:
                        for newhp, newdis in dp[i][j-1][k].items():
                            newhp += hpchange
                            newdis += 1
                            if newhp > 0 and newhp not in dp[i][j][k]:
                                dp[i][j][k][newhp] = newdis
                                changed = True
                            elif newhp > 0 and dp[i][j][k][newhp] > newdis:
                                dp[i][j][k][newhp] = newdis
                                changed = True
                    if j < x-1:
                        for newhp, newdis in dp[i][j+1][k].items():
                            newhp += hpchange
                            newdis += 1
                            if newhp > 0 and newhp not in dp[i][j][k]:
                                dp[i][j][k][newhp] = newdis
                                changed = True
                            elif newhp > 0 and dp[i][j][k][newhp] > newdis:
                                dp[i][j][k][newhp] = newdis
                                changed = True
                    if k > 0:
                        for newhp, newdis in dp[i][j][k-1].items():
                            newhp += hpchange
                            newdis += 1
                            if newhp > 0 and newhp not in dp[i][j][k]:
                                dp[i][j][k][newhp] = newdis
                                changed = True
                            elif newhp > 0 and dp[i][j][k][newhp] > newdis:
                                dp[i][j][k][newhp] = newdis
                                changed = True
                    if k < y-1:
                        for newhp, newdis in dp[i][j][k+1].items():
                            newhp += hpchange
                            newdis += 1
                            if newhp > 0 and newhp not in dp[i][j][k]:
                                dp[i][j][k][newhp] = newdis
                                changed = True
                            elif newhp > 0 and dp[i][j][k][newhp] > newdis:
                                dp[i][j][k][newhp] = newdis
                                changed = True
                    
                    # finded[i][j][k] = True

    return dp


if __name__ == "__main__":
    s = input()
    s = s.split(" ")
    x, y, z, hp = int(s[0]), int(s[1]), int(s[2]), int(s[3])

    puzzle = []
    dp = []
    for i in range(z):
        floor = []
        dpfloor = []
        for j in range(x):
            line = input()
            dpline = [{} for _ in range(len(line))]
            floor.append(line)
            dpfloor.append(dpline)
            for k, c in enumerate(line):
                if c == "S":
                    start = [i, j, k]
                elif c == "E":
                    final = [i, j, k]
        puzzle.append(floor)
        dp.append(dpfloor)
        if i < z-1:
            input()
    dp[start[0]][start[1]][start[2]][hp] = 0
    dp = findPrincess(puzzle, dp, x, y, z)
    ans = 99999
    for key, v in dp[final[0]][final[1]][final[2]].items():
        ans = min(ans, v)
    
    if ans != 99999:
        print(ans)
    else:
        print("No solution")
'''
3 3 3 2
..S
*..
.#.

#**
***
###

*.*
##E
...

'''