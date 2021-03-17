class Solution:
    def minArray(self, numbers) -> int:     # 有序想到二分查找换皮
        head = 0
        tail = len(numbers) - 1
        mid = (head + tail) // 2
        headTailList = [[head, tail]]
        valley = numbers[0]
        while True and headTailList:
            head, tail = headTailList.pop()
            mid = (head + tail) // 2
            if head + 1 == tail:
                valley = min(valley, numbers[head], numbers[tail])
            elif head == tail:
                valley = min(valley, numbers[head])
            elif numbers[mid] < numbers[head]:
                headTailList.append([head, mid])
            elif numbers[mid] > numbers[tail]:
                headTailList.append([mid, tail])
            else:
                headTailList.append([head, mid])
                headTailList.append([mid, tail])
        
        return valley


if __name__ == "__main__":
    numbers = [10,10,1,10,10]
    solution = Solution()
    print(solution.minArray(numbers))