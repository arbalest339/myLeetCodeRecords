class Solution:
    def findContinuousSequence(self, target):
        if target<3:
            return []
        i = 1
        j = 2
        res = []
        while j < target//2+2:
            sum = (i+j)*(j-i+1)/2
            if sum == target:
                ans = list(range(i,j+1))
                res.append(ans)
                i += 1
                j = i+1
            elif sum < target:
                j += 1
            else:
                i += 1
                j = i+1
        return res


if __name__ == "__main__":
    solution = Solution()
    target = 9
    solution.findContinuousSequence(target)
