class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 2:
            return self.commonPrefix(strs[0], strs[1])
        new_strs = []
        for i in range(0, len(strs), 2):
            if i+1 < len(strs):
                common = self.commonPrefix(strs[i], strs[i+1])
                new_strs.append(common)
            else:
                new_strs.append(strs[i])
        return self.longestCommonPrefix(new_strs)
    
    def commonPrefix(self, s1, s2):
        common = ""
        for i, c in enumerate(s1):
            if i > len(s2) - 1 or c != s2[i]:
                return common
            common += c
        return common


if __name__ == "__main__":
    solution = Solution()
    strs = ["baab","bacb","b","cbc"]
    print(solution.longestCommonPrefix(strs))