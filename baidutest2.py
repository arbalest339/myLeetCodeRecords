# 现在有n个长度为m的字符串，编号为从1到n，每个字符串由m个大写字母组成。现在你可以完成以下操作，请你任选第 i 个字符串和第 j 个字符串，并交换长度为 k 的前缀。你可以在变换后的基础上进行任意次这样的操作。

# 例如：ABCD 和 EFGH，令k=2则变为 EFCD 和 ABGH。

# 此时对于新的字符串 EFCD 和 ABGH 令k=1则变为 AFCD 和 EBGH。

# 显然变化后的字符串是不同的。

# 现在请问你可以生成多少个不同的字符串。包含原串本身。

def exchangePrefix(lines, m):
    cols = []
    for i in range(m):
        col = set([line[i] for line in lines])
        cols.append(len(col))
    
    res = 1
    for c in cols:
        res *= c
    
    print(res % 1000000007)

if __name__=="__main__":
    line1 = input()
    n, m = line1.split(" ")
    n = int(n)
    m = int(m)
    lines = []
    for _ in range(n):
        line = input()
        lines.append(list(line.strip()))
    exchangePrefix(lines, m)
'''
2 3
ABC
DEF

8
'''
