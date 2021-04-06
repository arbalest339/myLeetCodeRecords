class Solution:
    def sumSubarrayMins(self, arr) -> int:
        MOD = 10**9 + 7
        N = len(arr)

        # prev has i* - 1 in increasing order of arr[i* - 1]
        # where i* is the answer to query j
        stack = []
        prev = [None] * N
        for i in range(N):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)

        # next has k* + 1 in increasing order of arr[k* + 1]
        # where k* is the answer to query j
        stack = []
        next_ = [None] * N
        for k in range(N-1, -1, -1):
            while stack and arr[k] < arr[stack[-1]]:
                stack.pop()
            next_[k] = stack[-1] if stack else N
            stack.append(k)

        # Use prev/next array to count answer
        return sum((i - prev[i]) * (next_[i] - i) * arr[i]
                   for i in range(N)) % MOD


if __name__ == "__main__":
    solution = Solution()
    arr = [71,55,82,55]
    res = solution.sumSubarrayMins(arr)
    print(res)
