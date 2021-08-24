class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = n
        j = 0
        k = 0
        for i in range(m+n-1, n-1, -1):
            nums1[i] = nums1[i-n]
        while i <m+n or j < n:
            if i <m+n and (j >= n or nums1[i]<nums2[j]):
                nums1[k] = nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        print("sss")


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 3, 7, 9, 11, 15, 0, 0, 0, 0, 0]
    nums2 = [2, 6, 8, 12, 14]
    solution.merge(nums1, 6, nums2, 5)
