# s = input()
# s = s.split(" ")
# n, m = int(s[0]), int(s[1])

# dp = [[0] * n for _ in range(m)]

# dp[0][1] = 1
# dp[0][-1] = 1

# for i in range(1,m):
#     for j in range(n):
#         dp[i][j] = dp[i-1][j-1] + dp[i-1][(j+1)%n]

# print(dp[-1][0])

ch = input()
x = []
count= 0
for i in  ch:
    if i.isdigit() is True or i.isalpha() is True:
        x.append('1')
    else:
        x.append('0')
num = list(input())
for i ,j in zip(num,x):
    if i == j:
        count +=1
print("%.2f%%"%(count/float(len(ch))*100))