class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = 10^6 + 1
        while l <= r:
            k = (l+r) // 2
            hours = 0
            for i in piles: hours += ((i // k)+1 if i % k != 0 else i // k)
            if hours == h: 
                ans = k
                r = k - 1
            elif hours < h:
                ans = k
                r = k - 1
            elif hours > h: l = k + 1 
        return ans