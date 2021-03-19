class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        if len(pushed) == 0:
            return True
        stack = [pushed[0]]
        i = 1
        j = 0
        while stack:
            while i < len(pushed) and stack[-1] != popped[j]:
                stack.append(pushed[i])
                i += 1

            while j < len(popped) and stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

            if i == len(pushed):
                break

            if not stack and i == j:
                stack.append(pushed[i])
                i += 1

        if not stack:
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()
    pushed = [1, 0]
    popped = [1, 0]
    print(solution.validateStackSequences(pushed, popped))
