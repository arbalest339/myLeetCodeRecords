class Solution:
    def strToInt(self, str: str) -> int:
        str = str.strip(" ")
        intStr = ""
        i = 0
        start = False
        neg = False
        for i in range(len(str)):
            if not start and '0' <= str[i] <= '9':
                intStr += str[i]
                start = True
            elif not start and str[i] == '-':
                neg = True
                start = True
            elif not start and str[i] == '+':
                start = True
            elif not start:
                break
            elif start and '0' <= str[i] <= '9':
                intStr += str[i]
            elif start and ('0' > str[i] or str[i] >= '9'):
                break
        res = 0
        for place in intStr:
            res = res*10 + int(place)
        if neg:
            return max(-2**31, -res)
        return min(2**31-1, res)


if __name__ == "__main__":
    solution = Solution()
    str = "-0012a42"
    solution.strToInt(str)
