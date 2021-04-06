class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])  # 当内部扩增出现时，将现有的字串保存，这是必须的，否则无法解决嵌套问题
                res, multi = "", 0  # 清空状态重新投入当前的使用
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)            
            else:
                res += c
        return res


if __name__ == "__main__":
    s = "3[a2[c]ss]ac2[p]"
    solution = Solution()
    solution.decodeString(s)