class Solution:
    def reverse(self, x: int) -> int:
        flag = True
        if x < 0:
            if x < -2147483648:
                return 0
            x = -x
            flag = False
        else:
            if x > 2147483647:
                return 0
        y = 0
        while x:
            remain = x % 10
            y = y*10+remain
            x = x // 10

        if not flag:
            return -y if -y >= -2147483648 else 0
        else:
            return y if y <= 2147483647 else 0


if __name__ == "__main__":
    solution = Solution()
    x = -2147483648
    print(solution.reverse(x))
