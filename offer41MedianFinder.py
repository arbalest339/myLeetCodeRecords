import heapq
import bisect


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.orderList = []
        self.median = 0

    def addNum(self, num: int) -> None:
        if not self.orderList:
            self.orderList.append(num)
        else:
            bisect.insort_left(self.orderList, num)
        self.median = len(self.orderList) // 2

    def findMedian(self) -> float:
        if not self.orderList:
            return None
        if len(self.orderList) % 2 == 1:
            return self.orderList[self.median]
        else:
            return (self.orderList[self.median] + self.orderList[self.median-1]) / 2


if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(-1)
    param_2 = obj.findMedian()
    obj.addNum(-2)
    param_2 = obj.findMedian()
    obj.addNum(-3)
    param_2 = obj.findMedian()
    obj.addNum(-4)
    param_2 = obj.findMedian()
    obj.addNum(-5)
    param_2 = obj.findMedian()
