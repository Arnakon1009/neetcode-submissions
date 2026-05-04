class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * (len(temp))
        for i in range(0, len(temp)):
            for j in range(i, len(temp)):
                if i == j: continue
                if temp[i] < temp[j]:
                    res[i] = j-i
                    break
        return res