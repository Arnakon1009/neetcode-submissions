class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * (len(temp))
        stk = []
        for i, temp in enumerate(temp):
            while stk and temp > stk[-1][0]:
                stkT, stkI = stk.pop()
                res[stkI] = i - stkI
            stk.append((temp, i))
        return res