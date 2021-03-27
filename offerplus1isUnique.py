class Solution:
    def isUnique(self, astr: str) -> bool:
        if not astr:
            return True
        astr = list(astr)
        astr.sort()
        last = astr[0]
        for i in range(1, len(astr)):
            if astr[i] == last:
                return False
            last = astr[i]
        return True


if __name__ == "__main__":
    solution = Solution()
    s = "leetcode"
    solution.isUnique(s)
