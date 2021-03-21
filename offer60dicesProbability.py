class Solution:
    def __init__(self):
        self.res = [[0]]
        for n in range(1, 12):
            if n == 1:
                self.res.append([1, 1, 1, 1, 1, 1])
                continue
            line = []
            min_num = n
            max_num = n*6
            mid = (min_num+max_num) // 2
            for i in range(n, mid+1):
                end = i-n+1
                begin = max(0, end-6)
                sum = 0
                for j in range(begin, end):
                    sum += self.res[n-1][j]
                line.append(sum)
            if (min_num+max_num)%2 == 0:
                reverse = line[:-1].copy()
            else:
                reverse = line.copy()
            while reverse:
                line.append(reverse.pop())
            self.res.append(line)
        

    def dicesProbability(self, n: int):
        prob = (1/6)**n
        res = [case * prob for case in self.res[n]]
        return res



if __name__ == "__main__":
    solution = Solution()
    n = 2
    solution.dicesProbability(n)
