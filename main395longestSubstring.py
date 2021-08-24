class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        分治算法，如果字符串里存在不满足要求的字符，则可以这些字符做分割

        Args:
            s (str): [description]
            k (int): [description]

        Returns:
            int: [description]
        """
        charMap = {}
        for c in s:
            if c not in charMap:
                charMap[c] = 1
            else:
                charMap[c] += 1
        
        splitChars = []
        for c, n in charMap.items():
            if n < k:
                splitChars.append(c)
        
        if not splitChars:
            return len(s)
        
        splits = [s]
        for c in splitChars:
            new_splits = []
            for subs in splits:
                subs = subs.split(c)
                new_splits += subs
            splits = new_splits
        
        splits = sorted(splits, key= lambda x:len(x), reverse=True)

        max_res = 0
        for subs in splits:
            if len(subs)< max_res:
                break
            res = self.longestSubstring(subs, k)
            max_res = max(max_res, res)
        return max_res
        


if __name__ == "__main__":
    solution = Solution()
    s = "ababbc"
    k = 2
    print(solution.longestSubstring(s, k))