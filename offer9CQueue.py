class CQueue:   # 一个管进，倒出来管出

    def __init__(self):
        self.appendStack = []
        self.deleteStack = []


    def appendTail(self, value: int) -> None:
        while self.deleteStack:
            self.appendStack.append(self.deleteStack.pop())
        self.appendStack.append(value)


    def deleteHead(self) -> int:
        while self.appendStack:
            self.deleteStack.append(self.appendStack.pop())
        if not self.deleteStack:
            return -1
        else:
            return self.deleteStack.pop()


if __name__ == "__main__":
    obj = CQueue()
    param_2 = obj.deleteHead()
    obj.appendTail(5)
    obj.appendTail(2)
    param_2 = obj.deleteHead()
    param_2 = obj.deleteHead()
    param_2 = obj.deleteHead()