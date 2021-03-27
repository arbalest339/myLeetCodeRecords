import sys

def main(cards):
    profit = 0
    res = 0
    pulled = False
    i = 0
    nextbegin = 0
    while i < len(cards):
        if cards[i] == 0 and not pulled:
            nextbegin = i
            pulled = True
        elif cards[i] == 0 and pulled:
            res = max(profit, res)
            i = nextbegin
            profit = 0
            pulled = False
        else:
            profit += 1
        i += 1
    res = max(res, profit)
    if res == len(cards):
        res -= 1
    return res

if __name__ == "__main__":
    cards = [1,1,1,1,1,1,1]
    main(cards)
    # 命令行读取用代码
    # t = int(next(sys.stdin))
    # for i in range(t):
    #     lenght = int(next(sys.stdin))
    #     cards = next(sys.stdin).split(" ")
    #     cards = [int(c) for c in cards]
    #     print(main(cards))