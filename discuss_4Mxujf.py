# 有M种字符。输入两个字符串S与P，P可空。现在在P中插入连续相同的字符，问需经过几步可由P转化为S，若不能输出-1。
# 示例：输入：ABBCCCBAA ""
# 输出：3
# 层层剥皮，保存剥下来的皮
paths = []


def leftFirst(S, path):     # 从左向右判断，取左侧为规约字符
    if len(S) == 0:
        paths.append(path)
        return
    elif len(S) == 1:
        path.append([S, path[-1][-1].replace("|", S)])    # 规约S,剩余空
        paths.append(path)
        return

    cur_c = S[0]

    i = 1
    striped = cur_c
    for i in range(1, len(S)):
        if S[i] != cur_c:
            break
        striped += cur_c
    if i == len(S)-1 and S[i] == cur_c:
        path.append([cur_c, path[-1][-1].replace("|", S)])
        paths.append(path)
        return

    striped += "|"
    j = len(S)-1
    for j in range(len(S)-1, i, -1):
        if S[j] != cur_c:
            break
        striped += cur_c
    path.append([cur_c, path[-1][-1].replace("|", striped)])

    leftFirst(S[i:j+1], path.copy())
    rightFirst(S[i:j+1], path.copy())
    return


def rightFirst(S, path):    # 从右向左判断，取右侧为规约字符
    if len(S) == 0:
        paths.append(path)
        return
    elif len(S) == 1:
        path.append([S, path[-1][-1].replace("|", S)])    # 规约S,剩余空
        paths.append(path)
        return

    cur_c = S[-1]
    striped = cur_c

    j = len(S)-2
    for j in range(len(S)-2, -1, -1):
        if S[j] != cur_c:
            break
        striped = cur_c + striped
    if j == 0 and S[j] == cur_c:
        path.append([cur_c, path[-1][-1].replace("|", S)])
        paths.append(path)
        return

    i = 1
    striped = "|" + striped
    for i in range(1, j):
        if S[i] != cur_c:
            break
        striped = cur_c + striped
    path.append([cur_c, path[-1][-1].replace("|", striped)])
    leftFirst(S[i:j+1], path.copy())
    rightFirst(S[i:j+1], path.copy())
    return


if __name__ == "__main__":
    path = [["", "|"]]  # 规约字符，规约字串，竖线表示插入位置
    S = "BBCCCBAA"
    P = "AA"
    leftFirst(S, path.copy())
    rightFirst(S, path.copy())

    min = len(S)
    find = False
    for path in paths:
        for i, status in enumerate(path):
            if P == status[-1].replace("|", "") and len(path)-1-i < min:
                min = len(path)-1-i
                find = True
    if find:
        print(min)
    else:
        print(-1)
