class Solution:  # 动态规划，保存从i开始到j结束的部分是不是回文，之后判断i-1到j+1是否是回文
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]

    def newLongestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans

    def init0(self, s):  # 预处理s
        r = "#".join(s)
        r = list(r)
        r.append("#")
        r.insert(0, "#")
        return r

    def manacher(self, s):
        mx = -1
        id0 = -1
        max_length = -1
        rIndex = -1
        s = self.init0(s)
        p = [-1 for i in range(len(s))]
        print(s)
        for i in range(1, len(s)-1):
            if i < mx:
                p[i] = min(mx-i, p[2*id0-i])
            else:
                p[i] = 1

            while i >= p[i] and i+p[i] < len(p) and s[i-p[i]] == s[i+p[i]]:
                p[i] += 1

            if mx < i + p[i]:
                mx = i + p[i]
                id0 = i

            if p[i]-1 > max_length:
                rIndex = i
                max_length = p[i]-1

        tmp = s[rIndex-p[rIndex]+1:rIndex+p[rIndex]]

        return "".join("".join(tmp).split("#"))


if __name__ == "__main__":
    s = "abbasaas"
    solution = Solution()
    print(solution.longestPalindrome(s))
    s = solution.init0(s)
    print(solution.manacher(s))
