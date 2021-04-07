class Solution:
    def myAtoi(self, s: str) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        s = s.strip()
        if not s:
            return 0

        f = 1
        cur = 0
        start = False
        for i in range(len(s)):
            if s[i].isdigit():
                if not start:
                    start = True
                if cur*10 > MAX:
                    return MAX
                if cur*10 < MIN:
                    return MIN
                cur = cur*10 + int(s[i])*f
                if cur > MAX:
                    return MAX
                if cur < MIN:
                    return MIN
            elif not start and s[i] == "-":
                f = -1
                start = True
            elif not start and s[i] == "+":
                start = True
            else:
                if not start:
                    return 0
                else:
                    return cur
            i += 1

        return cur


if __name__ == "__main__":
    solution = Solution()
    s = "2147483646"
    print(solution.myAtoi(s))
