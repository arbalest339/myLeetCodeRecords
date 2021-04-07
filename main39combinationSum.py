class Solution:
    def __init__(self) -> None:
        self.paths = []
    
    def combinationSum(self, candidates, target: int):
        for i, c in enumerate(candidates):
            if c == target:
                self.paths.append([c])
            elif c < target:
                self.dfs(candidates[i:], target-c, [c])
        return self.paths
    
    def dfs(self, candidates, target, path):
        for i, c in enumerate(candidates):
            if c == target:
                self.paths.append(path+[c])
            elif c < target:
                self.dfs(candidates[i:], target-c, path+[c])

if __name__ == "__main__":
    solution = Solution()
    candidates = [2,3,5]
    target = 8
    solution.combinationSum(candidates, target)