class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastStart = 0
        maxLen = 0
        for i in range(len(s)):
            if s[i] in s[lastStart:i]:
                curLen = i-lastStart
                if curLen > maxLen:
                    maxLen = curLen
                lastStart = s[lastStart:i].index(s[i])+1+lastStart
        curLen = len(s)-lastStart
        if curLen > maxLen:
            maxLen = curLen
        return maxLen


if __name__ == "__main__":
    solution = Solution()
    s = "abcabcbb"
    solution.lengthOfLongestSubstring(s)
