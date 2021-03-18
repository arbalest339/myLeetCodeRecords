class Solution:
    def findKthLargest(self, nums, k) -> int:
        import heapq
        heap = []
        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            elif n > heap[0]:
                heapq.heapreplace(heap, n)
        return heap[0]


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    solution.findKthLargest(nums, k)
