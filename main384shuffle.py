from random import shuffle


class Solution:

    def __init__(self, nums):
        self.origin = nums
        self.cur = self.origin.copy()

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.cur = self.origin.copy()
        return self.cur

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        import random
        times = random.randint(0, 5)

        shuffled = []
        for _ in range(times):
            cut = len(self.origin) // 2
            offset = 0
            while offset < cut:
                shuffled.append(self.cur[cut + offset])
                shuffled.append(self.cur[offset])
                offset += 1
            if len(shuffled) < len(self.cur):
                shuffled.append(self.cur[-1])
            self.cur = shuffled.copy()
            shuffled = []
        return self.cur


if __name__ == "__main__":
    nums = [1, 2, 3]
    obj = Solution(nums)
    param_2 = obj.shuffle()
    param_1 = obj.reset()
    param_2 = obj.shuffle()
