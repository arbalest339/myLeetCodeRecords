class Solution:
    def getLeastNumbers(self, arr, k: int):
        import heapq
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans


if __name__ == "__main__":
    solution = Solution()
    arr = [0, 1, 2, 1, 3, 4, 5, 6, 4, 3, 2, 0, 1]
    k = 5
    solution.getLeastNumbers(arr, k)
