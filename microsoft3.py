def solution(S):
    # write your code in Python 3.6
    l = 0
    while l != len(S):
        l = len(S)
        S = S.replace("AB", "")
        S = S.replace("BA", "")
        S = S.replace("CD", "")
        S = S.replace("DC", "")
    return S

if __name__ == "__main__":
    S = "BCDABA"
    solution(S)