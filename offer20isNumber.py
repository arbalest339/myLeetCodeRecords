# [+-]?\d+(\.\d+)?([Ee][+-]*\d+)?

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip(" ")
        s = s.split("E")
        if len(s) == 2:
            s, exp = s
            if exp.startswith("+") or exp.startswith("-"):
                exp = exp[1:]
            if not exp:
                return False
            for d in exp:
                if d > '9' or d < '0':
                    return False
        elif len(s) == 1:
            s = s[0].split("e")
            if len(s) == 2:
                s, exp = s
                if exp.startswith("+") or exp.startswith("-"):
                    exp = exp[1:]
                if not exp:
                    return False
                for d in exp:
                    if d > '9' or d < '0':
                        return False
            elif len(s) == 1:
                s = s[0]
            else:
                return False
        else:
            return False

        if s.startswith("+") or s.startswith("-"):
            s = s[1:]

        s = s.split(".")
        if len(s) == 2:
            if not s[0] and not s[1]:
                return False
            for d in s[0]:
                if d > '9' or d < '0':
                    return False
            for d in s[1]:
                if d > '9' or d < '0':
                    return False
        elif len(s) == 1:
            if not s[0]:
                return False
            for d in s[0]:
                if d > '9' or d < '0':
                    return False
        else:
            return False

        return True


if __name__ == "__main__":
    solution = Solution()
    s = "0e"  # "+100.43e-2."
    print(solution.isNumber(s))
