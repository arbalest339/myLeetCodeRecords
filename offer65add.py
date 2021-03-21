class Solution:
    def neg(self, bn):
        forward = 1
        bn = ['0' if bn[-i]=='1' else '1' for i in range(1, len(bn)+1)]
        for i in range(len(bn)):
            if forward == 0:
                break
            if bn[i] == '1':
                bn[i] = '0'
            else:
                bn[i] = '1'
                forward = 0
        remain = 32 - len(bn)
        for _ in range(remain):
            bn += '1'
        return bn

    def pos(self, bn):
        bn = [bn[-i] for i in range(1, len(bn)+1)]
        remain = 32 - len(bn)
        for _ in range(remain):
            bn += '0'
        return bn

    def add(self, a: int, b: int) -> int:
        ba = bin(a)[2:]
        bb = bin(b)[2:]
        
        if ba.startswith("b"):
            ba = self.neg(ba[1:])
        else:
            ba = self.pos(ba)
        if bb.startswith("b"):
            bb = self.neg(bb[1:])
        else:
            bb = self.pos(bb)
        
        forward = 0
        ans = ""
        for i in range(32):
            if ba[i] == '1' and bb[i] == '1':
                if forward == 1:
                    ans += '1'
                else:
                    ans += '0'
                forward = 1
            elif ba[i] == '0' and bb[i] == '0':
                if forward == 1:
                    ans += '1'
                else:
                    ans += '0'
                forward = 0
            else:
                if forward == 1:
                    ans += '0'
                else:
                    ans += '1'
                    forward = 0
        ans = [ans[-i] for i in range(1, len(ans)+1)]
        ans = "".join(ans)
        res = int(ans[1:], 2)
        if ans[0] == '1':
            res += -2**31
        
        return res
    
    def officialAdd(self, a: int, b: int) -> int:
        x = 0xffffffff  # Python 没有 int , long 等不同长度变量，即在编程时无变量位数的概念。
        a, b = a & x, b & x  # 舍去此数字 32 位以上的数字
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x    # a成为第一次异或的结果，此时a中没有考虑进位，但是b保存了进位的情况，<<1以将进位传递到前一位
        return a if a <= 0x7fffffff else ~(a ^ x)

if __name__ == "__main__":
    solution = Solution()
    a = 7
    b = -5
    solution.officialAdd(a,b)