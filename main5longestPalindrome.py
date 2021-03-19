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
        if len(s) < 2:
            return s
        res = s[0]
        for i in range(2, len(s)):
            if s[i-2] == s[i]:
                h, t = i-2, i
                while h >= 0 and t < len(s) and s[h] == s[t]:
                    h -= 1
                    t += 1
                cur = s[h+1:t]
                res = cur if len(cur) > len(res) else res
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                h, t = i-1, i
                while h >= 0 and t < len(s) and s[h] == s[t]:
                    h -= 1
                    t += 1
                cur = s[h+1:t]
                res = cur if len(cur) > len(res) else res
        return res


if __name__ == "__main__":
    input = "bb"
    solution = Solution()
    print(solution.longestPalindrome(input))
