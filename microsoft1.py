class item:
    def __init__(self, dis, cost) -> None:
        self.dis = dis
        self.cost = cost
    
    def __lt__(self, o: object) -> bool:
        if self.dis < o.dis:
            return True
        elif self.dis == o.dis and self.cost < o.cost:
            return True
        elif self.dis == o.dis and self.cost == o.cost:
            return True
        else:
            return False

def solution(D,C,P):
    itemList = []
    for d,c in zip(D,C):
        itemList.append(item(d,c))
    itemList = sorted(itemList)

    res = 0
    for i in itemList:
        if i.cost <= P:
            P -= i.cost
            res += 1
        else:
            break
    return res
    # write your code in Python 3.6


if __name__ == "__main__":
    D = [5,5,5,5]
    C = [8,3,3,4]
    P = 6
    solution(D,C,P)