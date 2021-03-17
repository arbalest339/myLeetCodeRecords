class Solution:
    def genNext(self, word):  # KMP算法生成next数组，本题可以用KMP加速但是需要耗费大量的存储空间
        next = [0] * len(word)
        i, j = 1, 0
        while i <len(word):
            if word[i] == word[j]:
                next[i] = j+1 
                i += 1
                j += 1
            elif j != 0:
                j = next[j-1]
            else:
                next[j] = 0
                i += 1
        
        return next

    def exist(self, board, word) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False


    
if __name__ == "__main__":
    solution = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(solution.exist(board, word))
